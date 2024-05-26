# -*- coding:utf-8 -*-
# Author: Zachary

import os
from pathlib import Path

from dotenv import load_dotenv


class Config:
    def __init__(self):
        dotenv_path = Path(__file__).parent.parent / ".env"
        load_dotenv(dotenv_path=dotenv_path)
        self._env = dict(os.environ)

    @property
    def env(self):
        return self._env


config = Config()
