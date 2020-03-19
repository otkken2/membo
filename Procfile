web: gunicorn membo.wsgi --log-file -
web2: daphne membo.routing:application --port $PORT --bind 0.0.0.0 -v2.4.1
worker: python manage.py runworker channel_layer -v2.4.0