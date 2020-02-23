-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS languages;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS songs;
DROP TABLE IF EXISTS users_songs;

CREATE TABLE languages (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL
);

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  fullname TEXT NOT NULL,
  password TEXT NOT NULL,
  main_lang INTEGER NOT NULL,
  want_lang INTEGER NOT NULL,
  FOREIGN KEY (main_lang) REFERENCES languages (id),
  FOREIGN KEY (want_lang) REFERENCES languages (id)
);

CREATE TABLE songs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  song_name TEXT NOT NULL,
  unique_words TEXT NOT NULL,
  match_words INTEGER NOT NULL,
  max_words INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS users_songs (
  user_id INTEGER,
  song_id INTEGER,
  FOREIGN KEY (user_id) REFERENCES users (id),
  FOREIGN KEY (song_id) REFERENCES songs (id)
);
