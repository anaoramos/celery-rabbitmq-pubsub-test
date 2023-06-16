"""
Celery setup.
"""
from celery import Celery
from kombu import Exchange, Queue

data_aggregation_exchange_name = "data_aggregation-queue-ex"
data_aggregation_queue_name = "data-aggregation"
data_aggregation_routing_key = "data-aggregation-queue-rk"

data_validation_exchange_name = "data-validation-queue-ex"
data_validation_queue_name = "data-validation"
data_validation_routing_key = "data-validation-queue-rk"

dead_letter_queue_name = "safevox-api-dlq"
dead_letter_exchange_name = "safevox-api-dlq-ex"
dead_letter_routing_key = "safevox-api-dlq-rk"

data_aggregation_exchange = Exchange(data_aggregation_exchange_name, type="direct")
data_aggregation_queue = Queue(
    name=data_aggregation_queue_name,
    exchange=data_aggregation_exchange,
    routing_key=data_aggregation_routing_key,
)

data_validation_exchange = Exchange(data_validation_exchange_name, type="direct")
data_validation_queue = Queue(
    name=data_validation_queue_name,
    exchange=data_validation_exchange,
    routing_key=data_validation_routing_key,
)

app = Celery("app")
app.conf.task_queues = (data_aggregation_queue, data_validation_queue)

app.config_from_object('celeryconfig')
