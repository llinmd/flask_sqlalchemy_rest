from sqlalchemy.engine.url import _rfc_1738_quote

class Config(object):
    DEBUG = False
    TESTING = False

    DB_DIALECT = "mysql"
    DB_DRIVER = "pymysql"
    DB_NAME = "yellowdog"
    DB_USERNAME = "root"
    DB_PASSWORD = "P@ssw0rd!"
    DB_HOST = "localhost"
    DB_PORT = 3306

    SQLALCHEMY_DATABASE_URI = '{dialect}+{driver}://{user}:{password}@{host}:{port}/{database}'.format(
        dialect=DB_DIALECT,
        driver=DB_DRIVER,
        user=DB_USERNAME,
        password=_rfc_1738_quote(DB_PASSWORD),
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
