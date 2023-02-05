CREATE TABLE IF NOT EXISTS users
(
    id       integer primary key autoincrement,
    login    text,
    password text
);
CREATE TABLE IF NOT EXISTS tables
(
    id   integer primary key autoincrement,
    name text
);
CREATE TABLE IF NOT EXISTS player
(
    id          integer,
    username    text,
    avatar      text,
    DOB         text,
    telegram_id text
);
CREATE TABLE IF NOT EXISTS games
(
    id   integer primary key autoincrement,
    name text
);

CREATE TABLE IF NOT EXISTS gamefield
(
    id        integer primary key autoincrement,
    player_id text,
    word      text,
    letters   text,
    status    integer
);

CREATE TABLE IF NOT EXISTS words
(
    id   integer primary key autoincrement,
    word text
)
