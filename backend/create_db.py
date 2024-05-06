import os
from app.Managers.ConfigManager import ConfigManager
from app.Managers.LogManager import LogManager
from app.Managers.DbManager import DbManager

DIR = os.path.dirname(__file__)


config_manager = ConfigManager(DIR)
log_manager = LogManager(config_manager)
db_manager = DbManager(config_manager, log_manager)

db_manager.create_tables()
