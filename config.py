import os
basedir=os.path.abspath(os.path.dirname(__file__))

class Config:
	pass

class DevelopmentConfig(Config):
	DEBUG=True

class TestingConfig(Config):
	pass

class ProductionConfig(Config):
	pass

config={
	'development':DevelopmentConfig,
	'testing':TestingConfig,
	'production':ProductionConfig,
	'default':DevelopmentConfig
}