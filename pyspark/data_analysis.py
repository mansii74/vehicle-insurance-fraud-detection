from pyspark.sql.functions import col, sum

def basic_analysis(df):
    print(f"Total Rows: {df.count()}")
    print(f"Total Columns: {len(df.columns)}")

    missing_df = df.select([
        sum(col(c).isNull().cast("int")).alias(c) for c in df.columns
    ])
    missing_df.show()

def get_column_types(df):
    num_cols = [c for c, t in df.dtypes if t in ("int", "double", "float")]
    cat_cols = [c for c, t in df.dtypes if t == "string"]

    print("Numerical Columns:", num_cols)
    print("Categorical Columns:", cat_cols)

    return num_cols, cat_cols
