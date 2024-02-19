select distinct name from movies a inner join directors b on a.id = b.movie_id inner join people c on b.person_id = c.id inner join ratings d on a.id = d.movie_id where rating >=9;
