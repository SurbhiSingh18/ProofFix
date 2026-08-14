import pickle
import pandas as pd

_bundle = None


def _load_bundle(
    model_path: str = "flaky_detector/model.pkl"
):
    global _bundle

    if _bundle is None:
        with open(model_path, "rb") as f:
            _bundle = pickle.load(f)

    return _bundle


def is_flaky(
    feature_dict: dict,
    test_name: str = "unknown"
) -> dict:

    bundle = _load_bundle()

    model = bundle["model"]
    feature_cols = bundle["feature_columns"]

    row = {
        col: feature_dict.get(col, 0)
        for col in feature_cols
    }

    X = pd.DataFrame([row])[feature_cols]

    pred = model.predict(X)[0]

    confidence = max(
        model.predict_proba(X)[0]
    )

    return {
        "test_name": test_name,
        "is_flaky": bool(pred),
        "confidence": float(confidence)
    }


if __name__ == "__main__":

    bundle = _load_bundle()

    print(
        "Model expects these features:",
        bundle["feature_columns"]
    )

    sample = {
        col: 0
        for col in bundle["feature_columns"]
    }

    sample["numAsserts"] = 1
    sample["ExecutionTime"] = 50

    print(
        is_flaky(
            sample,
            test_name="sample_test"
        )
    )