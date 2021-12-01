drop schema if exists user_pref;
create schema user_pref;
use user_pref;

drop table if exists user_profile;

create table user_profile
(
	id int NOT NULL,
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

-- insert into user_profile (id, movie, hobby, book, music, sport, major)
-- values (10000, 'Guardians of the Galaxy', 'Anime', NULL, 'Pop', 'Basketball', 'CS'),
--        (10001, 'Harry Potter', 'Skateboarding', 'The Swallows', 'Rock', 'Hockey', 'Math');