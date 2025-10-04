class Config():
    DEBUG=True
    SQLALCHEMY_DATABASE_URI="sqlite:///mydb.db" 
class Development(Config):
    pass
class Testing(Config):
    pass
class Production(Config):
    DEBUG=False