from sqlalchemy import create_engine
import os


class DbConnecter:
    def __init__(self, config):
        """Initialize the attributes with the given config. Tries to establish connection."""
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
        """Closes the connection on class destructor."""
        self.db_con.close()
        print("Connection has been closed.")

    def _establish_connection_(self):
        """Establish connection and makes the cursor and connection attributes."""
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
        """
        Executes a query in the database. Because of how sqlalchemy works, 
        the transaction is committed automatically. Autocommit can be set 
        to off manually.
        """
        print(query)
        self.db_cur.execute(query)

    def read_query(self, query):
        """Returns the result of a query."""
        self.db_cur.execute(query)
        result = self.db_cur.fetchall()

        return result


def connect_to_database(config=None):
    """
    Returns an object with a connection to the specified database.
    If config is not specified it tried to check in the environment
    for the database configuration.
    """
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
