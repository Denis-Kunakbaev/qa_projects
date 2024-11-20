class ProjectModelQueries:
    SELECT_ALL = "SELECT * FROM Project"
    SELECT_BY_ID = "SELECT * FROM Project WHERE ID = %s"


class StatusModelQueries:
    SELECT_ALL = "SELECT * FROM Status"
    SELECT_BY_NAME = "SELECT * FROM Status WHERE Name = %s"


class TestModelQueries:
    SELECT_ALL = "SELECT * FROM Test"
    SELECT_BY_ID = "SELECT * FROM Test WHERE ID = %s"
    INSERT = "INSERT INTO Test (name, status_id, method_name, project_id, session_id, start_time, end_time, env, browser)\
     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    DELETE = "DELETE FROM Test WHERE ID = %s"
