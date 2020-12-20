CREATE TABLE Lastscraping (
    scraping_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    last_get    TEXT    NOT NULL,
    status      INTEGER NOT NULL
);

CREATE TABLE Sentiment (
    tweetid   INTEGER,
    sentiment INTEGER NOT NULL,
    FOREIGN KEY (tweetid) REFERENCES Tweet (tweetid)
);

CREATE TABLE Tweet (
    tweetid INTEGER PRIMARY KEY NOT NULL,
    userid  INTEGER NOT NULL,
    createddate TEXT NOT NULL,
    tweet TEXT,
    cleantweet TEXT,
    scraping_id INTEGER,
    FOREIGN KEY (userid) REFERENCES TwitterUser (userid),
    FOREIGN KEY (scraping_id) REFERENCES Lastscraping (scraping_id)
);

CREATE TABLE TwitterUser (
    userid INTEGER PRIMARY KEY NOT NULL,
    name TEXT,
    screenname TEXT,
    location TEXT,
    acccreated TEXT,
    follower INTEGER,
    friend INTEGER,
    verified INTEGER
);