# 本文件为配置文件，会被__init__.py加载



# 数据库相关配置
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'test'
USERNAME = 'root'
PASSWORD = '123456'

# 数据库连接拼接，基本不用动
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD, host=HOST,port=PORT, db=DATABASE)

# 数据库连接指定为我们拼接好的连接
SQLALCHEMY_DATABASE_URI = DB_URI
# 会追踪对象的修改并且发送信号，TRUE会占用内存，非必须就关闭
SQLALCHEMY_TRACK_MODIFICATIONS = False
# 是否打印sql语句
SQLALCHEMY_ECHO = True
# 数据库连接池大小
SQLALCHEMY_POOL_SIZE = 10


# JSON数据不强制转换中文，设置为true时中文数据会变成ASCII码
JSON_AS_ASCII = False

# 密钥，说是很重要
SECRET_KEY = "jjdurenfs_4df-sed"