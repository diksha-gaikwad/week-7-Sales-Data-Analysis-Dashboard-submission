import pandas as pd

def export_report(stats, output="data/reports/sales_report.xlsx"):

    df = pd.DataFrame([stats])

    df.to_excel(output, index=False)

    print("Report saved:", output)