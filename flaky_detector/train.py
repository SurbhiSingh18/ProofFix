import pickle
import os

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

from features import load_and_clean


def train_model(
    csv_path: str,
    model_out_path: str = "flaky_detector/model.pkl"
):

    X, y, feature_cols = load_and_clean(csv_path)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    clf = RandomForestClassifier(
        n_estimators=200,
        random_state=42,
        class_weight="balanced"
    )

    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    os.makedirs(
        os.path.dirname(model_out_path),
        exist_ok=True
    )

    with open(model_out_path, "wb") as f:
        pickle.dump(
            {
                "model": clf,
                "feature_columns": feature_cols
            },
            f
        )

    print(f"Model + feature list saved to {model_out_path}")


if __name__ == "__main__":
    train_model(
        "data/flakeflagger_processed_data.csv"
    )