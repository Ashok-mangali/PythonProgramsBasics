-- create table query syntax
create table player(
	id integer not null primary key auto_increment, 
	name varchar(20), 
	age integer, 
	score integer, 
	created_by timestamp default current_timestamp
);


-- insert data into player table
insert into player(name, age, score) values('kishore kumar', 25, 100);

-- insert bulk data into player table
insert into player(name, age, score)
values('ashok kumar', 22, 100),
('raj', 40, 200),
('shilpa', 30, 500),
('ankur', 35, 100),
('pooja', 22, 100);


-- get all rows from player table
select * from player;

-- using like expression
select * from player where name like '%k%';

-- using order by
select * from player order by id desc;

