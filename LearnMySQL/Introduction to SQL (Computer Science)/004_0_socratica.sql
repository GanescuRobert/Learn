/* CREATE TABLE public.earthquake
(
    earthquake_id integer NOT NULL,
    occurred_on timestamp without time zone,
    latitude numeric,
    longitude numeric,
    depth numeric,
    magnitude numeric,
    calculation_method character varying,
    network_id character varying,
    place character varying,
    cause character varying,
    CONSTRAINT earthquake_pkey PRIMARY KEY (earthquake_id)
)
WITH (
    OIDS = FALSE
) */

SELECT * FROM earthquake;
SELECT COUNT(*) FROM earthquake;

SELECT magnitude,place,occurred_on FROM earthquake;

