from push import flatten_df
import pandas as pd


def test_flatten_df():
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
