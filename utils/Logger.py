import logging.handlers
import os


class Logger:
    LEVEL = logging.INFO
    MAX_BYTES = 10 * 1024 * 1024
    BACKUP_COUNT = 10
    FORMAT = "%(asctime)s [%(levelname)s] [%(name)s,%(lineno)s] %(message)s"


def get_logger(name):
    logger = logging.getLogger(name)

    if len(logger.handlers) > 0:
        return logger

    formatter = logging.Formatter(Logger.FORMAT)
    stream_handler = logging.StreamHandler()
    file_handler = logging.handlers.RotatingFileHandler(
        filename="/Users/yjkim/PycharmProjects/my_project_logs/my_project.log",
        maxBytes=Logger.MAX_BYTES,
        backupCount=Logger.BACKUP_COUNT
    )

    # 핸들러 & 포매터 결합
    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # 로거 & 핸들러 결합
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    # 로거 레벨 설정
    logger.setLevel(Logger.LEVEL)

    return logger
