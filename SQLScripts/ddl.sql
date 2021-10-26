use user_pref;

drop table if exists user_profile;

create table user_profile
(
	id int NOT NULL auto_increment,
    movie VARCHAR(1000) NULL,
    hobby VARCHAR(1000) NULL,
    book VARCHAR(1000) NULL,
    music VARCHAR(1000) NULL,
    sport VARCHAR(1000) NULL,
    major VARCHAR(256) NULL,
    orientation VARCHAR(16) NULL,
    created_at timestamp DEFAULT current_timestamp,
    CONSTRAINT pk_user_profile PRIMARY KEY (ID)
);

insert into user_profile (movie, hobby, book, music, sport, major)
values ('Guardians of the Galaxy', 'Anime', NULL, 'Pop', 'Basketball', 'CS'),
       ('Harry Potter', 'Skateboarding', 'The Swallows', 'Rock', 'Hockey', 'Math');