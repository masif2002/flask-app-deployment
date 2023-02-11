#! /bin/bash

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for PostgreSQL ... "

    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
    done

    echo " voilà!! PostgreSQL has started ..."
fi

# In production, we create tables only during the intial launch

exec "$@"