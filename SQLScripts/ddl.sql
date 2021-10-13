use user_pref;

drop table if exists user_profile;

create table user_profile
(
	id int NOT NULL auto_increment,
    movie VARCHAR(1000) NULL,
    hobby VARCHAR(1000) NULL,
    book VARCHAR(1000) NULL,
    music VARCHAR(1000) NULL,
    sports VARCHAR(1000) NULL,
    major VARCHAR(1000) NULL,
    created_at timestamp DEFAULT current_timestamp,
    CONSTRAINT pk_user_profile PRIMARY KEY (ID)
);

insert into user_profile (movie, hobby, book, music, sports, major)
values ('Guardians of the Galaxy', 'Anime', NULL, 'Pop', 'Basketball', 'CS'),
       ('Harry Potter', 'Skateboarding', 'The Swallows', 'Rock', 'Hockey', 'Math');