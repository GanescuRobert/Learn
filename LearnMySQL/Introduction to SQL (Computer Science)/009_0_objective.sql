DROP TABLE song;
CREATE TABLE song (
    song_id integer,
    title character varying,
    artist character varying,
    album character varying,
    year_released integer,
    duration numeric,
    tempo numeric,
    loudness numeric
);