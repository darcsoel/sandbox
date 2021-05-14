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
where v.vaccine is distinct from 'Rabies'
  and a.species <> 'Rabbit'
group by a.species, a.name, v.vaccine
having max(v.vaccination_time) < '20191001' or max(v.vaccination_time) is null
order by a.name

-- all breeds without adoptions
select animals.species, animals.breed
from animals
where (animals.species, animals.breed) not in (
    select a.species, a.breed from animals a
    join adoptions on adoptions.name = a.name and adoptions.species = a.species
    where a.breed is not null
    )
group by animals.species, animals.breed

select animals.species, animals.breed
from animals
except
select a.species, a.breed
from animals a
join adoptions on adoptions.name = a.name and adoptions.species = a.species
where a.breed is not null

-- statictics by year, stuff, year and stuff, species
select coalesce(cast(extract(year from v.vaccination_time) as varchar(10)), 'all years') as year,
       coalesce(v.species, 'all species') as species,
       coalesce(v.email, 'all emails') as email,
       case when grouping(v.email) = 0 then max(p.first_name) else '' end as first_name,
       case when grouping(v.email) = 0 then max(p.last_name) else '' end as last_name,
       count(*) as number_of_vaccinations,
       max(extract(year from v.vaccination_time)) as last_year
from vaccinations v
inner join persons p on v.email = p.email
group by grouping sets ((), v.vaccination_time, v.species, (v.vaccination_time, v.species), v.email, (v.email, v.species))
