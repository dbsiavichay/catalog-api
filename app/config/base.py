from environs import Env

env = Env()


class BaseConfig:
    ENVIRONMENT = env("ENVIRONMENT", "local")

    #
    # AWS config
    #

    AWS_REGION_NAME = env("AWS_REGION_NAME", "")

    AWS_WALLET_QUEUE_NAME_MS = env("AWS_WALLET_QUEUE_NAME_MS", "")
    AWS_QUEUE_GROUP_ID_MS = env("AWS_QUEUE_GROUP_ID_MS", "")
    AWS_QUEUE_MAX_LIMIT_MESSAGES = env.int("AWS_QUEUE_MAX_LIMIT_MESSAGES", 10)
