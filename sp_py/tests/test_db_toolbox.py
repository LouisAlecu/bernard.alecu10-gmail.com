from sp_py.db_toolbox import connect_to_database
import os


def test_connection():
    """Does it actually connect to the database?"""
    config = {
        "db_host": "localhost",
        "db_name": "sp",
        "db_user": "postgres",
        "db_port": 5433,
        "db_pass": "",
    }

    try:
        con = connect_to_database(config)
    except:
        assert False


def test_read_query():
    """Does it actually connect to the database?"""
    config = {
        "db_host": "localhost",
        "db_name": "sp",
        "db_user": "postgres",
        "db_port": 5433,
        "db_pass": "",
    }
    con = connect_to_database(config)

    assert len(con.read_query("Select now()")) > 0
