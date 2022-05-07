CREATE TABLE "players" (
  "id" SERIAL PRIMARY KEY,
  "full_name" varchar,
  "batting_avg" numeric,
  "team_name" string,
  "hasInjury" boolean,
  "age" int,
  "handness" varchar
);

CREATE TABLE "games" (
  "id" int,
  "date" datetime,
  "home" string,
  "vistor" string,
  "home_score" int,
  "vistor_score" int,
  "attendance" int,
  "victor" varchar,
  "victor_team" varchar,
  "losing_team" varchar
);

CREATE TABLE "teams" (
  "id" int,
  "name" string,
  "stadium" string,
  "city" string,
  "state" string
);

CREATE TABLE "weather" (
  "id" int,
  "date" datetime,
  "city" string,
  "state" string,
  "temp" numeric
);

CREATE TABLE "injury" (
  "id" int,
  "players_name" string,
  "injury_type" string
);

ALTER TABLE "players" ADD FOREIGN KEY ("team_name") REFERENCES "teams" ("name");

ALTER TABLE "weather" ADD FOREIGN KEY ("date") REFERENCES "games" ("date");

ALTER TABLE "teams" ADD FOREIGN KEY ("city") REFERENCES "weather" ("city");

ALTER TABLE "teams" ADD FOREIGN KEY ("state") REFERENCES "weather" ("state");

ALTER TABLE "players" ADD FOREIGN KEY ("id") REFERENCES "injury" ("players_name");
