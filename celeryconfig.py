default_user = 'admin'
default_pass = 'admin'
broker_url = 'amqp://admin:admin@rabbitmq:5672'
result_backend = 'rpc://'

task_serializer = 'json'
result_serializer = 'json'
timezone = 'Europe/Lisbon'
enable_utc = True

accept_content = ["application/json"]
# task_acks_late = True
# task_acks_on_failure_or_timeout = False
# task_reject_on_worker_lost = True
# worker_enable_remote_control= False
# worker_hijack_root_logger = False
# worker_max_tasks_per_child = 1
# worker_prefetch_multiplier = 1

# Import and register the tasks
from app.tasks import data_validation, data_aggregation

# task_routes = {
#     'app.tasks.data_validation.data_validation': {'queue': 'data-validation'},
#     'app.tasks.data_aggregation.data_aggregation': {'queue': 'data-aggregation'},
# }


# from kombu import Exchange, Queue
#
# data_validation_exchange = Exchange("data-validation-ex", type="direct")
# data_validation_queue = Queue(
#     name="data-validation",
#     exchange=data_validation_exchange,
#     routing_key="data-validation-rk",
# )
#
# data_aggregation_exchange = Exchange("data-aggregation-ex", type="direct")
# data_aggregation_queue = Queue(
#     name="data-aggregation",
#     exchange=data_aggregation_exchange,
#     routing_key="data-aggregation-rk",
# )
#
# task_queues = (
#     data_validation_queue,
#     data_aggregation_queue,
# )
