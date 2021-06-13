-- select users, groupped by first letter of name, return letter and count of users

select substr(name, 1, 1) as alpha, count(id)
from users
group by substr(name, 1, 1);


-- return count of users in each group
select groups.name, count(group_id)
from groups
left join users u
on groups.id = u.group_id
group by groups.name, u.group_id;


explain analyse select u.id, p.id, p.text from users u
left join friends f on u.id = f.usr_id
left join posts p on f.friend_usr_id = p.usr_id
where u.id = 1
order by p.timestamp desc
limit 7;


-- not efficient
explain analyse select p.*
  from friends f, lateral(select p.* from posts p where p.usr_id=f.friend_usr_id order by p.timestamp desc) p
where f.usr_id=1
order by p.timestamp desc
limit 10;


-- replace char_lenght with correct func
select case when char_length('(') = char_length(')') then TRUE else FALSE end as balance from posts
where posts.id in (17, 18);


select cast((now() + INTERVAL '1 day') as date)