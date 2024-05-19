import os
import json
from app.Managers.ConfigManager import ConfigManager
from app.Managers.LogManager import LogManager
from app.Managers.DbManager import DbManager

from app.Managers.UserManager import UserManager


DIR = os.path.dirname(__file__)


config_manager = ConfigManager(DIR)
log_manager = LogManager(config_manager)
db_manager = DbManager(config_manager, log_manager)

user = UserManager(config_manager, log_manager, db_manager)
with open('backend/test_data/users.json', 'r') as us:
    us = json.load(us)
user.create_user(us[0])




db_manager.drop_all_tables()
db_manager.create_tables()

db_manager.insert_in_db(user)

# 1. parse json
# 2. add to db (by add userManager functions)