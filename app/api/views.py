import json

import requests
from fastapi import HTTPException
from pydantic import BaseModel

from app.tasks.data_aggregation import data_aggregation
from app.tasks.data_validation import data_validation


class ProcessingJob(BaseModel):
    dataset: str


def schedule_data_processing(data):
    data_validation.apply_async(data, link=data_aggregation.s())


def send_get_request(url: str):
    request_header = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }

    response = requests.get(
        url=url,
        headers=request_header,

    )

    response.raise_for_status()
    response_json = json.loads(response.content)
    return response_json


def create_processing_job(processing_job: ProcessingJob):
    dataset = processing_job.dataset
    data = send_get_request(url=dataset)

    if data is None:
        raise HTTPException(status_code=400, detail="Failed to retrieve data")

    schedule_data_processing([data])

    return {200: "Job Submited!"}
