#!/bin/sh

# Create .env file with environment variables
cat <<EOL > .env
NEO4J_URI=bolt://YOUR.IP.NEO4J.HERE:PORT
NEO4J_USERNAME=USERNAME
NEO4J_PASSWORD=PASSWORD
NEO4J_DATABASE=DB_NAME
EOL

echo ".env file created successfully."

exit 0
