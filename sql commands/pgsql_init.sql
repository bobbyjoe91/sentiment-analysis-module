DROP TABLE IF EXISTS Lastscraping;
DROP TABLE IF EXISTS Sentiment;
DROP TABLE IF EXISTS Tweet;
DROP TABLE IF EXISTS TwitterUser;

CREATE TABLE Lastscraping (
    scraping_id SERIAL PRIMARY KEY NOT NULL,
    last_get    TEXT    NOT NULL,
    status      INT NOT NULL
);

CREATE TABLE TwitterUser (
    userid INT PRIMARY KEY NOT NULL,
    name TEXT,
    screenname TEXT,
    location TEXT,
    acccreated TEXT,
    follower INT,
    friend INT,
    verified INT
);

CREATE TABLE Tweet (
    tweetid INT PRIMARY KEY NOT NULL,
    userid  INT NOT NULL,
    createddate TIMESTAMP NOT NULL,
    tweet TEXT,
    cleantweet TEXT,
    scraping_id INT,
    CONSTRAINT fk_user FOREIGN KEY(userid) REFERENCES TwitterUser(userid),
    CONSTRAINT fk_lastscraping FOREIGN KEY(scraping_id) REFERENCES Lastscraping(scraping_id)
);

CREATE TABLE Sentiment (
    tweetid   INT,
    sentiment INT NOT NULL,
    CONSTRAINT fk_tweet FOREIGN KEY(tweetid) REFERENCES Tweet(tweetid)
);