import os

SETTINGS_DIR = 'regions'
DEFAULT_REGION = 'oregon-b'
DEFAULT_ENV = 'dev'
TEMPLATE_DIR = os.path.join(
    os.sep,
    os.path.dirname(
        os.path.realpath(__file__)),
    'templates')

# template names
SUMO_WEB_TEMPLATE = 'sumo-web.yaml.j2'
SUMO_NODEPORT_TEMPLATE = 'sumo-nodeport.yaml.j2'
SUMO_CELERY_TEMPLATE = 'sumo-celery.yaml.j2'
SUMO_CRON_TEMPLATE = 'sumo-cron.yaml.j2'
