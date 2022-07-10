-- settings.sql
CREATE DATABASE soccer;
CREATE USER socceruser WITH PASSWORD 'soccer';
GRANT ALL PRIVILEGES ON DATABASE soccer TO socceruser;