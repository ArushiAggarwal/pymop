class Drift:
    Description = "Detects concept drift in continuous PCA features."
    Formalism = "stl"
    Formula = "always (V1 > -10.0 and V1 < 10.0)"
    Variables = ["V1"]
    Creation_Events = ["transaction_processed"]
    Events = {
        "After": { "transaction_processed": [["model", "process_transaction_data"]] }
    }
    Parameters = ["User_ID"]
    Handlers = { "Violation": "print('DRIFT VIOLATION: Distribution shift detected! Retraining recommended.')" }
