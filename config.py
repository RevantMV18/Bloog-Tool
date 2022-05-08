##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
