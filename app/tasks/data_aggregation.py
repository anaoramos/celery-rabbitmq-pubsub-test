from celery_app import app


@app.task(queue="data-aggregation")
def data_aggregation(data):
    # Perform data validation logic here
    return data
