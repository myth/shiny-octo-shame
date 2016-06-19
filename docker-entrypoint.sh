#!/usr/bin/env sh

cd /srv/app
python3 initmodels.py

rm /tmp/project-master.pid

echo Starting uwsgi.
exec uwsgi --chdir=/srv/app \
    --callable=app \
    --wsgi-file=app.py \
    --master --pidfile=/tmp/project-master.pid \
    --socket=0.0.0.0:8080 \
    --processes=5 \
    --harakiri=20 \
    --max-requests=5000 \
    --offload-threads=4 \
    --static-map=/static=./static \
    --vacuum
