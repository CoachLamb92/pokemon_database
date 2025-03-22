DROP DATABASE IF EXISTS pokemon_db;
CREATE DATABASE pokemon_db;

\c pokemon_db;
DROP TABLE IF EXISTS pokemon;
CREATE TABLE IF NOT EXISTS pokemon
(
    pokemon_id INT PRIMARY KEY,
    pokemon_name VARCHAR(20),
    base_experience INT,
    type_1 VARCHAR(10),
    type_2 VARCHAR(10) DEFAULT NULL,
    hp_stat INT,
    attack_stat INT,
    defense_stat INT,
    special_attack_stat INT,
    special_defense_stat INT,
    speed_stat INT
);

DROP TABLE IF EXISTS pokemon_moves;
CREATE TABLE IF NOT EXISTS pokemon_moves
(
    pokemon_id INT,
    move_id INT,
    level_learnt INT,
    learn_method VARCHAR(50)
);

DROP TABLE IF EXISTS moves;
CREATE TABLE IF NOT EXISTS moves
(
    move_id INT PRIMARY KEY,
    move_name VARCHAR(20),
    move_description VARCHAR(100),
    move_type VARCHAR(10),
    powerpoints INT,
    accuracy INT,
    power INT, 
    category VARCHAR(10)
);

ALTER TABLE pokemon_moves
    ADD FOREIGN KEY (pokemon_id) REFERENCES pokemon(pokemon_id) ON DELETE CASCADE;

ALTER TABLE moves
    ADD FOREIGN KEY (move_id) REFERENCES moves(move_id) ON DELETE CASCADE;
