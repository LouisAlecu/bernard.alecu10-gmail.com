from push import flatten_df
import pandas as pd


def test_flatten_df():
    """
    Does it flatten the columns for a json string column? 
    It is a string because that is how we read it from csv as it is dumped
    with json library in order to be able to upload it to postgres array literals.
    """
    x = pd.DataFrame(
        {
            "col1": [1, 2, 3],
            "col2": [
                '{"values": {"a": 1, "b": 2, "c": 3}}',
                '{"values": {"a": 4, "b": 5, "c": 6}}',
                '{"values": {"a": 7, "b": 8, "c": 9}}',
            ],
        }
    )
    x = flatten_df(x, "col2")
    assert len(x.columns) == 4
