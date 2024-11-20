from constants.queries import TestModelQueries


class Test:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def get(self, test_id=None):
        if test_id:
            self.db_manager.execute(TestModelQueries.SELECT_BY_ID, (test_id,))
            return self.db_manager.fetchone()
        else:
            self.db_manager.execute(TestModelQueries.SELECT_ALL)
            return self.db_manager.fetchall()

    def create(self, name, status_id, method_name, project_id, session_id, start_time, end_time, env, browser):
        self.db_manager.execute(
            TestModelQueries.INSERT,
            (name, status_id, method_name, project_id, session_id, start_time, end_time, env, browser)
        )
        self.db_manager.commit()
        return self.db_manager.lastrowid()

    def delete(self, test_id):
        self.db_manager.execute(TestModelQueries.DELETE, (test_id,))
        self.db_manager.commit()
