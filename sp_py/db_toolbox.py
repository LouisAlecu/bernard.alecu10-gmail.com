from sqlalchemy import create_engine
import os


class DbConnecter:
    def __init__(self, config):
        self.config = config
        self.db_host = config["db_host"]
        self.db_name = config["db_name"]
        self.db_user = config["db_user"]
        self.db_pass = config["db_pass"]
        self.db_port = config["db_port"]
        self.engine = None
        self.db_con = None
        self.db_cur = None

        self._establish_connection_()

    def __del__(self):

        self.db_con.close()
        print("Connection has been closed.")

    def commit_changes(self):

        self.db_con.commit()

    def _establish_connection_(self):

        self.engine = create_engine(
            "postgresql://"
            + self.db_user
            + ":"
            + self.db_pass
            + "@"
            + self.db_host
            + ":"
            + str(self.db_port)
            + "/"
            + self.db_name,
            echo=False,
        )
        self.db_con = self.engine.raw_connection()
        self.db_cur = self.db_con.cursor()

    def execute_query(self, query):
        print(query)
        self.db_cur.execute(query)

    def read_query(self, query):

        self.db_cur.execute(query)
        result = self.db_cur.fetchall()

        return result


def connect_to_database(config=None):
    if config is None:
        config = {
            "db_host": os.environ["SP_DB_HOST"],
            "db_name": os.environ["SP_DB_NAME"],
            "db_user": os.environ["SP_DB_USER"],
            "db_pass": os.environ["SP_DB_PORT"],
            "db_port": int(os.environ["SP_DB_PASS"]),
        }
    db_con = DbConnecter(config)

    return db_con
