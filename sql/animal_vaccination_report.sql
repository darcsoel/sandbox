create table if not exists animals
(
    id
    serial
    primary
    key,
    name
    varchar
(
    50
) unique not null,
    species varchar
(
    50
),
    breed varchar
(
    50
),
    color varchar
(
    50
)
    );

create table staff
(
    id   serial primary key,
    name varchar(50) not null,
    role varchar(50) not null
);

create table if not exists animal_vaccinations
(
    id
    serial
    primary
    key,
    name
    varchar
(
    50
) not null,
    type varchar
(
    40
) not null
    );