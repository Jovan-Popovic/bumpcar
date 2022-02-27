CREATE DATABASE bumpcar;
CREATE USER bumpadmin WITH PASSWORD 'FH9jpP4$WF5MKCZ^-sKTdj-!%qYFFyYKY3Eht_UD!3Fxs3yXA-BtaRHfFn=AjG5$';
ALTER ROLE bumpadmin SET client_encoding TO 'utf8';
ALTER ROLE bumpadmin SET default_transaction_isolation TO 'read committed';
ALTER ROLE bumpadmin SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE bumpcar TO bumpadmin;
