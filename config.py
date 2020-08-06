class Config:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@localhost/admin'
    SECRET_KEY = 'PEL$97PVG4v$tr#cyG$A#u77?n25QXL2*nUWyhD5Wbug5x-@PV'


class DevConfig(Config):
    DEBUG = True
