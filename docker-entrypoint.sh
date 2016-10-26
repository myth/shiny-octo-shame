#!/usr/bin/env sh

echo "Initializing database"
cd /srv/app
rm -f db.db
python initmodels.py

echo Starting uwsgi.
exec uwsgi --chdir=/srv/app \
    --callable=app \
    --wsgi-file=app.py \
    --master --pidfile=/tmp/project-master.pid \
    --socket=0.0.0.0:8080 \
    --http=0.0.0.0:8081 \
    --processes=5 \
    --harakiri=20 \
    --max-requests=5000 \
    --offload-threads=4 \
    --static-map=/static=./static \
    --vacuum
