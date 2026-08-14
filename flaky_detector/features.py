import pandas as pd

# Columns that identify a test but are NOT model features
ID_COLUMNS = [
    "Unnamed: 0",
    "test_name",
    "project",
    "testClassName",
    "testMethodName"
]

LABEL_COLUMN = "flaky"


def get_feature_columns(df: pd.DataFrame) -> list:
    return [
        c for c in df.columns
        if c not in ID_COLUMNS + [LABEL_COLUMN]
    ]


def load_and_clean(csv_path: str):
    """
    Loads FlakeFlagger's processed_data.csv,
    separates features (X) and label (y),
    and cleans missing/non-numeric values.
    """

    df = pd.read_csv(csv_path)

    feature_cols = get_feature_columns(df)
    X = df[feature_cols].copy()

    # Convert boolean/string values to numeric values
    for col in X.columns:
        if X[col].dtype == object:
            X[col] = X[col].map({
                "True": 1,
                "False": 0,
                True: 1,
                False: 0
            }).fillna(X[col])

        X[col] = pd.to_numeric(X[col], errors="coerce")

    X = X.fillna(0)

    y = df[LABEL_COLUMN]

    if y.dtype == object:
        y = y.map({
            "True": 1,
            "False": 0,
            True: 1,
            False: 0
        })

    y = y.fillna(0).astype(int)

    return X, y, feature_cols


if __name__ == "__main__":
    X, y, cols = load_and_clean(
        "data/flakeflagger_processed_data.csv"
    )

    print("Feature columns:", cols)
    print("X shape:", X.shape)
    print("y distribution:")
    print(y.value_counts())