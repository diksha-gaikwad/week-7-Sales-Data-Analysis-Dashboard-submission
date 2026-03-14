import matplotlib.pyplot as plt
import os

def sales_chart(category_data):

    os.makedirs("data/reports", exist_ok=True)

    category_data.plot(kind="bar")

    plt.title("Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Sales")

    plt.tight_layout()

    plt.savefig("data/reports/category_sales.png")

    plt.show()