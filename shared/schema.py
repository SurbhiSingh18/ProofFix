# shared/schema.py

# Output of flaky_detector
flaky_result = {
    "test_name": str,
    "is_flaky": bool,
    "confidence": float
}

# Output of fault_localization
localization_result = {
    "bug_id": str,
    "ranked_lines": [
        {
            "file": str,
            "line": int,
            "score": float
        }
    ]
}

# Output of repair_engine
patch_result = {
    "bug_id": str,
    "patch_diff": str,
    "attempt_number": int
}

# Output of verification
verification_result = {
    "bug_id": str,
    "passed": bool,
    "attempt_number": int
}