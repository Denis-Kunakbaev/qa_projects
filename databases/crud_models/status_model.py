from constants.queries import StatusModelQueries


class Status:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def get_by_name(self, name=None):
        if name:
            self.db_manager.execute(StatusModelQueries.SELECT_BY_NAME, (name,))
            return self.db_manager.fetchone()
        else:
            self.db_manager.execute(StatusModelQueries.SELECT_ALL)
            return self.db_manager.fetchall()
