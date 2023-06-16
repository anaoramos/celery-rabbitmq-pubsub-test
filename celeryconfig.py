default_user = 'admin'
default_pass = 'admin'

accept_content = ["application/json"]
broker_url = "amqp://admin:admin@rabbitmq:5672"
enable_utc = True

imports = [
    'app.tasks.data_aggregation',
    'app.tasks.data_validation',
]
