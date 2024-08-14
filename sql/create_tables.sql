DROP TABLE IF EXISTS deck;
DROP TABLE IF EXISTS card;

-- Creation of deck table
-- still need to create foreign key constraints
CREATE TABLE IF NOT EXISTS deck (
  id INT NOT NULL,
  title varchar(250) NOT NULL,
  creation_date TIMESTAMP,
  PRIMARY KEY (id)
);

-- Creation of deck table
-- still need to create foreign key constraints

CREATE TABLE IF NOT EXISTS card (
  id INT NOT NULL,
  deck_id INT NOT NULL,
  front varchar(250) NOT NULL,
  back varchar(250) NOT NULL,
  creation_date TIMESTAMP,
  PRIMARY KEY (id)
  FOREIGN KEY (deck_id) REFERENCES deck(id)
);