drop table if exists alarm;
drop table if exists light;

create table alarm (
    id integer primary key autoincrement,
    datetime text unique not null,
    length integer,
    brightness integer
);

create table light (
    id integer primary key check (id = 0),
    brightness integer not null,
    red integer not null,
    green integer not null,
    blue integer not null,
);



