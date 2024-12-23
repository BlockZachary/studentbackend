# -*- coding:utf-8 -*-
# Author: Zachary
import logging
import os.path
import sys
from types import FrameType
from typing import cast

from loguru import logger

from common.profile import Profile


class Logger:
    def __init__(self):
        log_file_path = Profile.get_logfiles_path()
        # 文件的命名
        log_path = os.path.join(log_file_path, "FastAPI_{time:YYYY-MM-DD}.log")
        self.logger = logger
        # 清空所有设置
        self.logger.remove()
        # 添加控制台输出的格式，
        self.logger.add(sys.stdout,
                        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
                               "{process.name} | "
                               "{thread.name} | "
                               "<cyan>{module}</cyan>.<cyan>{function}</cyan>"
                               ":<cyan>{line}</cyan> | "
                               "<level>{level}</level>: "
                               "<level>{message}</level>",
                        )
        # 日志写入文件
        self.logger.add(log_path,
                        format="{time:YYYY-MM-DD HH:mm:ss} - "
                               "{process.name} | "
                               "{thread.name} | "
                               "{module}.{function}:{line} - {level} - {message}",
                        encoding="utf-8",
                        retention="7 days",
                        backtrace=True,
                        diagnose=True,
                        enqueue=True,
                        rotation="00:00", )

    def init_config(self):
        LOGGER_NAMES = {"uvicorn.asgi", "uvicorn.access", "uvicorn"}

        logging.getLogger().handlers = [InterceptHandler()]
        for logger_name in LOGGER_NAMES:
            logging_logger = logging.getLogger(logger_name)
            logging_logger.handlers = [InterceptHandler()]

    def get_logger(self):
        return self.logger


class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = str(record.levelno)

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = cast(FrameType, frame.f_back)
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage(), )

Loggers = Logger()
log = Loggers.get_logger()
