select title from(
select title,name from movies a inner join stars b on a.id = b.movie_id inner join people c on b.person_id = c.id where name = 'Bradley Cooper' or name = 'Jennifer Lawrence') a
group by title having count(1) >1;
