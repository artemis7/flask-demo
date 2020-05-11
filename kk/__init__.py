# -*- coding: utf-8 -*-
import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


# 全局数据库对象
db = SQLAlchemy()

# 创建一个FLASK应用，一个FLASK应用包括配置数据/后端接口
app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev',
    # DATABASE=os.path.join(app.instance_path, 'kk.sqlite'),
)

from . import configs
# 读取配置文件
app.config.from_object(configs)
# 跨域设置
CORS(app, resources=r'/*')

# 保证实例文件夹存在
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

# 导入模型（即数据库表实体）
from . import models
# 初始化数据库对象
db.init_app(app)


# 注册蓝图（类似控制器，可以控制页面跳转/响应请求）
from . import auth
app.register_blueprint(auth.bp)
    
from . import testdb
app.register_blueprint(testdb.bp)