import os
from app.Managers.ConfigManager import ConfigManager
from app.Managers.LogManager import LogManager



DIR = os.path.dirname(__file__)


config_manager = ConfigManager(DIR)
log_manager = LogManager(config_manager)

