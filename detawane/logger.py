from logging import DEBUG, INFO, getLogger, StreamHandler


def get_local_logger(module_name, log_level=INFO):
    logger = getLogger(module_name)
    logger.setLevel(log_level)
    logger.addHandler(StreamHandler())
    return logger
