class UserManager:
    def __init__(self, config_manager, log_manager, db_manager):
        self.config = config_manager
        self.log = log_manager
        self.db = db_manager

    def create_user(self, user):
        return None