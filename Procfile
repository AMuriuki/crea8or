web: flask db upgrade; flask translate compile; gunicorn creatives:app
worker: rq worker creatives-tasks
