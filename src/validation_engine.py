import pandas as pd


def validate_dataframe(df, name="Dataset"):
    print(f"\n========== {name} ==========")

    # Row count
    print(f"Rows: {len(df)}")

    # Missing values
    missing = df.isnull().sum()
    missing = missing[missing > 0]
    print("\nMissing Values:")
    print(missing if len(missing) > 0 else "No missing values")

    # Duplicate rows
    duplicates = df.duplicated().sum()
    print(f"\nDuplicate Rows: {duplicates}")

    # Null %
    null_percent = (df.isnull().sum() / len(df)) * 100
    null_percent = null_percent[null_percent > 0]
    print("\nNull %:")
    print(null_percent if len(null_percent) > 0 else "No nulls")

    print("====================================\n")