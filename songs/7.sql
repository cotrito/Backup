select avg(energy) from songs a inner join artists b on a.artist_id = b.id where b.name ='Drake';
