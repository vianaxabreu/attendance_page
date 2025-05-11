# gunicorn_config.py

bind = "0.0.0.0:8080"
workers = 4
threads = 2
timeout = 120
loglevel = "info"
accesslog = "-"
errorlog = "_"
