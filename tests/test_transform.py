import pandas as pd
from etl.transform import transform

def test_transform_sums_by_city():
    df = pd.DataFrame({
        "city": ["A", "A", "B"],
        "total": [10, 20, 30]
    })
    out = transform(df)

    # ska innehålla exakt två rader (A och B)
    assert set(out["city"]) == {"A", "B"}
    # ska heta total_sales och ha rätt summering
    a_sum = out.loc[out["city"] == "A", "total_sales"].iloc[0]
    b_sum = out.loc[out["city"] == "B", "total_sales"].iloc[0]
    assert a_sum == 30
    assert b_sum == 30