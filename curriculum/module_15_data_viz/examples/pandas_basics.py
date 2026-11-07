"""pandas basics: Series, DataFrame, selection, filtering and missing data."""

# requires: pandas

import io

import pandas as pd

CSV = """region,product,units,price
north,pen,10,1.5
south,pen,4,1.5
north,book,2,12.0
east,book,,12.0
south,lamp,3,25.0
"""

df = pd.read_csv(io.StringIO(CSV))
print(df.head(3))
print(df.dtypes)
print(df.shape, list(df.columns))

print(df["units"].mean(), df["price"].max())  # Series operations skip NaN
print(df.loc[df["price"] > 10, ["product", "price"]])  # label based
print(df.iloc[0:2, 0:2])  # position based

df["revenue"] = df["units"] * df["price"]
print(df.sort_values("revenue", ascending=False).head(3))
print(df.isna().sum())
print(df.fillna({"units": 0}).loc[3, "units"], df.dropna().shape)
