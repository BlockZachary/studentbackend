# -*- coding:utf-8 -*-
# Author: Zachary
from pathlib import Path


class Profile:
    __file_path = None

    @staticmethod
    def get_files_path():
        project_path = Path(__file__).parent.parent  # 获取项目根目录
        file_path = project_path.joinpath("files")
        if not file_path.exists():
            file_path.mkdir(parents=True)
        Profile.__file_path = file_path
        return file_path

    @staticmethod
    def get_logfiles_path():
        project_path = Path(__file__).parent.parent  # 获取项目根目录
        file_path = project_path.joinpath("log_files")
        if not file_path.exists():
            file_path.mkdir(parents=True)
        Profile.__file_path = file_path
        return file_path

