import logging

from celery_app import app

logger = logging.getLogger(__name__)


@app.task(queue="data-aggregation")
def data_aggregation(data):
    logger.info("Starting data validation")

    # Perform data aggregation logic here
    return None
