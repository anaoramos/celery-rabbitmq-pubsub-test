from celery_app import app


@app.task(queue="data-validation")
def data_validation(data):
    # Perform data validation logic here
    return data
