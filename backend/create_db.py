import os
from app.Managers.ConfigManager import ConfigManager
from app.Managers.LogManager import LogManager
from app.Managers.DbManager import DbManager

DIR = os.path.dirname(__file__)


config_manager = ConfigManager(DIR)
log_manager = LogManager(config_manager)
db_manager = DbManager(config_manager, log_manager)

db_manager.drop_all_tables()
db_manager.create_tables()

# 1. parse json
# 2. add to db (by add userManager functions)
