class UserManager:
    def __init__(self, config_manager, log_manager, db_manager):
        self.config = config_manager
        self.log = log_manager
        self.db = db_manager

    def create_user(self, user: dict):
        pass

    def update_user(self, user: dict):
        pass

    def delete_user(self, user: dict):
        pass

    def get_user_by_id(self):
        # return dict
        pass