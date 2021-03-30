-- select users, groupped by first letter of name, return letter and count of users

select substr(name, 1, 1) as alpha, count(id)
from users
group by substr(name, 1, 1);


-- return count of users in each group
select groups.name, count(group_id)
from groups
left join users u
on groups.id = u.group_id
group by groups.name, u.group_id
