from constants.queries import ProjectModelQueries


class Project:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def get(self, project_id=None):
        if project_id:
            self.db_manager.execute(ProjectModelQueries.SELECT_BY_ID, (project_id,))
            return self.db_manager.fetchone()
        else:
            self.db_manager.execute(ProjectModelQueries.SELECT_ALL)
            return self.db_manager.fetchall()
