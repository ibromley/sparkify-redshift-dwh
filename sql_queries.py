import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs"
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

staging_events_table_create= ("""
    CREATE TABLE staging_events (
        artist_name         VARCHAR(100),
        auth                VARCHAR(20),
        first_name          VARCHAR(100) NOT NULL,
        gender              CHARACTER,
        itemInSession       INT,
        last_name           VARCHAR(100) NOT NULL,
        level               VARCHAR(20),
        location            VARCHAR(100),
        method              VARCHAR(10),
        page                VARCHAR(20),
        registration        NUMERIC(12,5),
        sessionId           INT,
        song                VARCHAR(200) NOT NULL,
        status              INT,
        ts                  INT,
        userAgent           TEXT,
        userID              INT
    )
""")

staging_songs_table_create = ("""
    CREATE TABLE staging_songs (
        song_id             VARCHAR(20) NOT NULL,
        num_songs           INT,
        title               VARCHAR(200) NOT NULL,
        artist_name         VARCHAR(100),
        artist_latitude     NUMERIC(12,5),
        year                INT,
        duration            NUMERIC(12,5),
        artist_id           VARCHAR(20) NOT NULL,
        artist_longitude    NUMERIC(12,5),
        artist_location     VARCHAR(100)
    );
""")

songplay_table_create = ("""
    CREATE TABLE songplays ( 
        songplays_id        INT IDENTITY(0,1) PRIMARY KEY,
        ts                  TIMESTAMP REFERENCES time(ts),
        user_id             INT REFERENCES users(user_id),
        level               VARCHAR(20),
        song_id             VARCHAR(20) REFERENCES songs(song_id),
        artist_id           VARCHAR(20) REFERENCES artists(artist_id),
        session_id          INT NOT NULL,
        location            VARCHAR(100),
        user_agent          TEXT
    )
""")

user_table_create = ("""
    CREATE TABLE users (
        user_id             INT PRIMARY KEY,
        first_name          VARCHAR(100) NOT NULL,
        last_name           VARCHAR(100) NOT NULL,
        gender              CHARACTER,
        level               VARCHAR(20)
    )
""")

song_table_create = ("""
    CREATE TABLE songs (
        song_id             VARCHAR(20) PRIMARY KEY,
        title               VARCHAR(200) NOT NULL,
        artist_id           VARCHAR(20) REFERENCES artists(artist_id),
        year                INT,
        duration            NUMERIC(12,5)
    )
""")

artist_table_create = ("""
    CREATE TABLE artists (
        artist_id           VARCHAR(20) PRIMARY KEY,
        artist_name         VARCHAR(100) NOT NULL,
        artist_location     VARCHAR(100),
        artist_latitude     NUMERIC(12,5),
        artist_longitude    NUMERIC(12,5) 
    )
""")

time_table_create = ("""
    CREATE TABLE time (
        ts                  TIMESTAMP PRIMARY KEY,
        hour                INT NOT NULL,
        day                 INT NOT NULL,
        week_of_year        INT NOT NULL,
        month               INT NOT NULL,
        year                INT NOT NULL,
        weekday             INT NOT NULL
    )
""")

# STAGING TABLES

staging_events_copy = ("""
    copy staging_events from {}
    credentials 'aws_iam_role={}'
    compupdate off region 'us-west-2';
""").format(config.get("S3","LOG_DATA"), config.get("IAM_ROLE","ARN"))

staging_songs_copy = ("""
    copy staging_events from {}
    credentials 'aws_iam_role={}'
    compupdate off region 'us-west-2';
""").format(config.get("S3","SONG_DATA"), config.get("IAM_ROLE","ARN"))

# FINAL TABLES

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")

time_table_insert = ("""
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create,  user_table_create, artist_table_create, song_table_create, time_table_create, songplay_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
