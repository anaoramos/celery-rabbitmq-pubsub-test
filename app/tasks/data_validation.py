import logging
import time

from celery_app import app

logger = logging.getLogger(__name__)


@app.task(queue="data-validation")
def data_validation(data):
    logger.info("Starting data validation")
    # Perform data validation logic here
    time.sleep(20)

    return None
