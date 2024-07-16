from environs import Env

env = Env()


class BaseConfig:
    ENVIRONMENT = env("ENVIRONMENT", "local")

    #
    # AWS config
    #

    AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID", "test")
    AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY", "test")
    AWS_REGION_NAME = env("AWS_REGION_NAME", "us-east-1")
    AWS_ENDPOINT_URL = env("AWS_ENDPOINT_URL", "http://localstack:4566")
