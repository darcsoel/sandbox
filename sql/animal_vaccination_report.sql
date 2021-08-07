-- https://github.com/ami-levin/LinkedIn/tree/master/Query%20Processing/Demo%20Database

select *
from animals as a
         left outer join (
    vaccinations v
        inner join staff s on s.email = v.email
    ) on a.name = v.name


select a.name, a.species, v.vaccine, count(v.vaccine)
from animals as a
         left outer join vaccinations v on a.name = v.name
where v.vaccine is distinct
from 'Rabies'
    and a.species <> 'Rabbit'
group by a.species, a.name, v.vaccine
having max (v.vaccination_time) < '20191001' or max (v.vaccination_time) is null
order by a.name;

-- all breeds without adoptions
select animals.species, animals.breed
from animals
where (animals.species, animals.breed) not in (
    select a.species, a.breed
    from animals a
             join adoptions on adoptions.name = a.name and adoptions.species = a.species
    where a.breed is not null
)
group by animals.species, animals.breed;

select animals.species, animals.breed
from animals
    except
select a.species, a.breed
from animals a
         join adoptions on adoptions.name = a.name and adoptions.species = a.species
where a.breed is not null;

-- statictics by year, stuff, year and stuff, species
select coalesce(cast(extract(year from v.vaccination_time) as varchar(10)), 'all years') as year,
       coalesce(v.species, 'all species') as species,
       coalesce(v.email, 'all emails') as email,
       case when grouping(v.email) = 0 then max(p.first_name) else ''
end
as first_name,
       case when grouping(v.email) = 0 then max(p.last_name) else ''
end
as last_name,
       count(*) as number_of_vaccinations,
       max(extract(year from v.vaccination_time)) as last_year
from vaccinations v
inner join persons p on v.email = p.email
group by grouping sets ((), v.vaccination_time, v.species, (v.vaccination_time, v.species),
v.email, (v.email, v.species));


select name, cast(count(vaccine) over (order by extract(year from vaccination_time) asc range between 2 preceding and 1 preceding) as decimal(10, 2)) as vac_count from vaccinations group by name, vaccine, vaccination_time;


with annual_vaccinations as (
    select cast(extract(year from v.vaccination_time) as int) as year,
           count(*) as vaccinations_count
    from vaccinations v
    group by extract(year from v.vaccination_time)
), annual_vaccinations_for_2_prev_years as (
    select *, cast(avg(vaccinations_count) over (order by year asc range between 2 preceding and 1 preceding)
        as decimal(5,2)) as prev_2_years_average
    from annual_vaccinations
)
select *,
       cast((100 * vaccinations_count / prev_2_years_average) as decimal(5, 2)) as prev_2_years_vaccination_percentage
from annual_vaccinations_for_2_prev_years
order by year;


with vacc_counter as (
    select name, count('vaccine') vc, dense_rank() over (order by count('vaccine') desc) drank
    from vaccinations
    group by name
)
select name, vc, drank
from vacc_counter
where drank = 1;


with checkups_with_temo_diff as (
    select species, name, temperature,
    cast (avg (temperature) over (partition by species) as decimal (5, 2)) as checkups_with_temo_diff,
    cast (temperature - avg (temperature) over (partition by species) as decimal (5, 2)) as difference_from_avg_temp_by_species
    from routine_checkups
    ), temp_differences as (
    select *, case
    when abs(difference_from_avg_temp_by_species / checkups_with_temo_diff) >= 0.005 then 1 else 0 end
    as is_tempature_exception
    from checkups_with_temo_diff
    )
select *
from temp_differences
order by species;


-- statistical analysis
WITH checkups_with_temperature_differences
    AS
    (
        SELECT species,
               name,
               temperature,
               checkup_time,
               CAST(AVG(temperature)
                   OVER (PARTITION BY species)
                   AS DECIMAL (5, 2)
                   ) AS species_average_temperature,
               CAST(temperature - AVG(temperature)
                   OVER (PARTITION BY species)
                   AS DECIMAL (5, 2)
                   ) AS difference_from_average
        FROM routine_checkups
    )
-- SELECT * FROM checkups_with_temperature_differences ORDER BY species, difference_from_average;
   , temperature_differences_with_exception_indicator
    AS
    (
        SELECT *,
               CASE
                   WHEN ABS(difference_from_average / species_average_temperature) >= 0.005
                       THEN 1
                   ELSE 0
                   END AS is_temperature_exception
        FROM checkups_with_temperature_differences
    )
-- SELECT * FROM temperature_differences_with_exception_indicator ORDER BY species, difference_from_average;
   , grouped_animals_with_exceptions
    AS
    (
        SELECT species,
               name,
               SUM(is_temperature_exception) AS number_of_exceptions,
               MAX(CASE
                       WHEN is_temperature_exception = 1
                           THEN checkup_time
                       ELSE NULL
                   END
                   )                         AS latest_exception
        FROM temperature_differences_with_exception_indicator
        GROUP BY species,
                 name
    )
-- SELECT * FROM grouped_animals_with_exceptions ORDER BY species, number_of_exceptions;
   , animal_exceptions_with_ntile
    AS
    (
        SELECT *,
               NTILE(4)
                   OVER (	PARTITION BY species
				ORDER BY number_of_exceptions ASC, -- try DESC,
						 latest_exception DESC -- try ASC
			 ) AS ntile
        FROM grouped_animals_with_exceptions
    )
-- SELECT * FROM animal_exceptions_with_ntile ORDER BY species, number_of_exceptions, latest_exception DESC;
SELECT species,
       name,
       number_of_exceptions,
       latest_exception
FROM animal_exceptions_with_ntile
WHERE ntile = 1 -- try 4
ORDER BY species ASC,
         number_of_exceptions DESC,
         latest_exception DESC;



-- Write a query that returns the top 5 most improved quarters in terms of the number of adoptions, both per species, and overall.
-- Improvement means the increase in number of adoptions compared to the previous calendar quarter.
-- The first quarter in which animals were adopted for each species and for all species, does not constitute an improvement from zero, and should be treated as no improvement.
-- In case there are quarters that are tied in terms of adoption improvement, return the most recent ones.
--


SELECT EXTRACT('quarter' FROM CURRENT_TIMESTAMP),
       EXTRACT('year' FROM CURRENT_TIMESTAMP);

WITH adoption_quarters
    AS
    (
        SELECT Species,
               MAKE_DATE(CAST(DATE_PART('year', adoption_date) AS INT),
                         CASE
                             WHEN DATE_PART('month', adoption_date) < 4
                                 THEN 1
                             WHEN DATE_PART('month', adoption_date) BETWEEN 4 AND 6
                                 THEN 4
                             WHEN DATE_PART('month', adoption_date) BETWEEN 7 AND 9
                                 THEN 7
                             WHEN DATE_PART('month', adoption_date) > 9
                                 THEN 10
                             END,
                         1
                   ) AS quarter_start
        FROM adoptions
    )
-- SELECT * FROM adoption_quarters ORDER BY species, quarter_start;
   , quarterly_adoptions
    AS
    (
        SELECT COALESCE(species, 'All species') AS species,
               quarter_start,
               COUNT(*)                         AS quarterly_adoptions,
               COUNT(*) - COALESCE(
                   -- For quarters with no previous adoptions use 0, not NULL
                       FIRST_VALUE(COUNT(*))
                       OVER(PARTITION BY species
							 		  ORDER BY quarter_start ASC
								   	  RANGE BETWEEN 	INTERVAL '3 months' PRECEDING
														AND
														INTERVAL '3 months' PRECEDING
                           )
                   , 0)
                                                AS adoption_difference_from_previous_quarter,
               CASE
                   WHEN quarter_start = FIRST_VALUE(quarter_start) OVER (PARTITION BY species
										  ORDER BY quarter_start ASC
										  RANGE BETWEEN 	UNBOUNDED PRECEDING
															AND
															UNBOUNDED FOLLOWING
										 )
			THEN 0
                   ELSE NULL
                   END                          AS zero_for_first_quarter
        FROM adoption_quarters
        GROUP BY GROUPING SETS ((quarter_start, species),
                                (quarter_start)
            )
    )
-- SELECT * FROM quarterly_adoptions ORDER BY species, quarter_start;
   , quarterly_adoptions_with_rank
    AS
    (
        SELECT *,
               RANK()
                   OVER (	PARTITION BY species
				ORDER BY 	COALESCE (zero_for_first_quarter, adoption_difference_from_previous_quarter) DESC,
							-- First quarters are 0, all others NULL
							quarter_start DESC)
		AS quarter_rank
        FROM quarterly_adoptions
    )
-- SELECT * FROM quarterly_adoptions_with_rank ORDER BY species, quarter_rank, quarter_start;
SELECT species,
       CAST(DATE_PART('year', quarter_start) AS INT) AS year,
		CAST (DATE_PART ('quarter', quarter_start) AS INT) AS quarter,
		adoption_difference_from_previous_quarter,
		quarterly_adoptions
FROM quarterly_adoptions_with_rank
WHERE quarter_rank <= 5
ORDER BY species ASC,
    adoption_difference_from_previous_quarter DESC,
    quarter_start ASC;
