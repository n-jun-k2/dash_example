from os import getenv
from celery import Celery
from dash.long_callback import CeleryLongCallbackManager


REDIS_PORT = getenv("REDIS_PORT")

celery_app = Celery(
    __name__,
    broker=f"redis://redis:{REDIS_PORT}/0",
    backend=f"redis://redis:{REDIS_PORT}/0"
)

LONG_CALLBACK_MANAGER = CeleryLongCallbackManager(celery_app)