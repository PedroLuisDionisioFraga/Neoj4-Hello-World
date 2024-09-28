@echo off

type .env

(
echo NEO4J_URI=bolt://YOUR.IP.NEO4J.HERE:PORT
echo NEO4J_USERNAME=USERNAME
echo NEO4J_PASSWORD=PASSWORD
echo NEO4J_DATABASE=DB_NAME
) > .env

echo .env file created successfully.
exit /b 0
