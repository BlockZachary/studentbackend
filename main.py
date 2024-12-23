# -*- coding:utf-8 -*-
# Author: Zachary
import uvicorn
from api import app
from common.constant import HOST, PORT
from common.log import Loggers

if __name__ == '__main__':
    Loggers.init_config()
    uvicorn.run("main:app", host=HOST, port=int(PORT), reload=True, log_config=None)
