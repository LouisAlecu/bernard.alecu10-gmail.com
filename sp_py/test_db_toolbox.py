from db_toolbox import connect_to_database
import os


def test_config():
    """Do we have a database config anywhere?"""
    try:
        from config import config

        ok = True
    except:
        ok = False
        try:
            config = {
                "db_host": os.environ["SP_DB_HOST"],
                "db_name": os.environ["SP_DB_NAME"],
                "db_user": os.environ["SP_DB_USER"],
                "db_pass": os.environ["SP_DB_PORT"],
                "db_port": int(os.environ["SP_DB_PASS"]),
            }
            ok = True
        except:
            ok = False
    assert ok


def test_connection():
    """Does it actually connect to the database?"""
    from config import config

    try:
        con = connect_to_database(config)
    except:
        assert False


def test_read_query():
    """Does it actually connect to the database?"""
    from config import config

    con = connect_to_database(config)

    assert len(con.read_query("Select now()")) > 0
