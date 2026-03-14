def basic_stats(df):

    stats = {
        "Total Sales": df["total_amount"].sum(),
        "Average Order": df["total_amount"].mean(),
        "Total Orders": len(df),
        "Unique Customers": df["customer_id"].nunique()
    }

    return stats


def sales_by_category(df):

    result = df.groupby("category")["total_amount"].sum()

    return result.sort_values(ascending=False)