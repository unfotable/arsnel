"""groupby, merge and pivot_table."""

# requires: pandas

import pandas as pd

sales = pd.DataFrame(
    {
        "region": ["north", "south", "north", "east", "south", "north"],
        "product": ["pen", "pen", "book", "book", "lamp", "lamp"],
        "units": [10, 4, 2, 5, 3, 1],
        "price": [1.5, 1.5, 12.0, 12.0, 25.0, 25.0],
    }
)
sales["revenue"] = sales["units"] * sales["price"]

by_region = sales.groupby("region")["revenue"].sum().sort_values(ascending=False)
print(by_region)
print(sales.groupby("product").agg(units=("units", "sum"), avg_price=("price", "mean")))

managers = pd.DataFrame({"region": ["north", "south"], "manager": ["Ada", "Grace"]})
merged = sales.merge(managers, on="region", how="left")  # 'east' gets NaN
print(merged[["region", "manager"]].drop_duplicates())

print(
    sales.pivot_table(
        index="region", columns="product", values="revenue", aggfunc="sum", fill_value=0
    )
)
