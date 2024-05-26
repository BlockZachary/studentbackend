# -*- coding:utf-8 -*-
# Author: Zachary
import uvicorn
from api import app
from common.constant import HOST, PORT

if __name__ == '__main__':
    uvicorn.run("main:app", host=HOST, port=int(PORT), reload=True)
