# -*- coding:utf-8 -*-
# Author: Zachary
import mimetypes
from datetime import datetime

from fastapi import APIRouter, UploadFile
from fastapi.encoders import jsonable_encoder
from starlette.responses import FileResponse
from fastapi.responses import StreamingResponse
from werkzeug.utils import secure_filename

from api import app
from common.constant import HOST, PORT
from common.profile import Profile
from common.result import ResultModel, Result
from exception.customException import FileNotFoundException

file_router = APIRouter(prefix='/files')


@file_router.post("/upload", response_model=ResultModel)
async def upload(file: UploadFile):
    original_filename = secure_filename(file.filename)
    timestamp = int(datetime.now().timestamp())
    unique_filename = f"{timestamp}_{original_filename}"
    file_save_path = Profile.get_files_path()

    # 创建保存文件的完整路径
    file_final_path = file_save_path.joinpath(unique_filename)

    # 将文件保存到指定位置
    with open(file_final_path, 'wb') as buffer_file:
        content = await file.read()
        buffer_file.write(content)

    # 构建文件访问URL
    url = f"http://{HOST}:{PORT}/files/download?filename={unique_filename}"
    return Result.success(jsonable_encoder({"url": url}))


@file_router.get("/download")
async def download(filename: str):
    file_save_path = Profile.get_files_path()
    file_path = file_save_path.joinpath(filename)

    if not file_path.exists():
        raise FileNotFoundException("文件不存在")
    # # 用于触发下载文件的
    # return FileResponse(file_path, media_type='image/png', filename=filename)

    mime_type, _ = mimetypes.guess_type(file_path)

    # 创建一个StreamingResponse，以便流式传输大文件，同时设置正确的MIME类型
    response = StreamingResponse(
        open(file_path, 'rb'),
        media_type=mime_type,
    )
    # 不设置Content-Disposition，避免浏览器触发下载
    return response


app.include_router(file_router)
