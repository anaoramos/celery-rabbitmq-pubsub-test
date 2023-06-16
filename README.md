# FastAPI Job Submission

This repository contains a simple implementation of a job submission endpoint using FastAPI. The endpoint receives POST requests with a dataset URL in the request body. The implementation utilizes Celery and RabbitMQ to handle dummy tasks for data aggregation and data validation.

## Features

- Submit a job by sending a POST request to the `/submit_job` endpoint with the dataset URL in the request body.
- Celery is used to asynchronously process the submitted job by executing dummy tasks.
- RabbitMQ acts as the message broker for task queueing and distribution.
- Docker Compose is provided for easy setup and deployment.

## Prerequisites

- Docker and Docker Compose should be installed on your system.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/anaoramos/fastapi-celery-docker-job-submission.git
   cd fastapi-job-submission

2. ```bash
   docker-compose up --build

3. This command will start the FastAPI application, Celery worker, and RabbitMQ.

Once the containers are up and running, you can access the RabbitMQ management console by visiting http://localhost:15672/#/queues in your web browser. Use the following credentials to log in:
```
Username: admin
Password: admin
```

## Usage
To submit a job, send a POST request to the /submit_job endpoint with the following JSON payload:
```json
{
  "dataset": "https://example.com/dataset.json"
}
```
The application will enqueue the job and process it asynchronously using Celery and RabbitMQ. The dummy tasks for data aggregation and data validation will be executed in the background.

## Customization
You can modify the implementation of the dummy tasks (data_aggregation.py and data_validation.py) according to your requirements.
Update the FastAPI route handlers (main.py) to include additional functionality if needed.
