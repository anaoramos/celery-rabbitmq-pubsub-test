from app.tasks.data_validation import data_validation
from app.tasks.data_aggregation import data_aggregation

from pydantic import BaseModel
import requests
import json
from fastapi import HTTPException


class ProcessingJob(BaseModel):
    dataset: str


def schedule_data_processing(data):
    data_validation.apply_async(args=data, link=data_aggregation.s())


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
