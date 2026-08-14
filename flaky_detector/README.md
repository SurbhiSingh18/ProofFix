# Flaky Test Classifier

## What it does
Predicts whether a test is flaky using FlakeFlagger's pre-computed
static + dynamic features (test smells, coverage, execution time, etc.)
and a Random Forest classifier.

## Data
Uses `data/flakeflagger_processed_data.csv`, sourced from the
FlakeFlagger dataset (AlshammariA/FlakeFlagger), containing 23 numeric
features per test and a binary `flaky` label.

## Setup
pip install -r requirements.txt

## Train
python flaky_detector/train.py
(reads data/flakeflagger_processed_data.csv, saves flaky_detector/model.pkl)

## Predict
from flaky_detector.predict import is_flaky
result = is_flaky(feature_dict, test_name="myTest")
# returns {"test_name": ..., "is_flaky": bool, "confidence": float}

feature_dict must contain the same feature names the model was trained on
(see model.pkl -> feature_columns, or print it via predict.py directly).

## Note
This model works on FlakeFlagger's pre-computed features, not raw source
code, since several features (execution time, coverage, modification
history) require dynamic analysis that can't be derived from static
source alone.

## Output format
Matches `flaky_result` in shared/schema.py

## Results

First trained version:

- Dataset: 22,236 tests
- Flaky tests: 811
- Non-flaky tests: 21,425
- Flaky class precision: 0.91
- Flaky class recall: 0.67
- Flaky class F1-score: 0.77
- Non-flaky class precision: 0.99
- Non-flaky class recall: 1.00
- Non-flaky class F1-score: 0.99