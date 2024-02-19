select distinct name from(
select title,a.id from movies a inner join stars b on a.id = b.movie_id inner join people c on b.person_id = c.id where name = 'Kevin Bacon' and birth = 1958
group by title,a.id
) a inner join stars b on a.id = b.movie_id inner join people c on b.person_id = c.id where name not in ('Kevin Bacon');
