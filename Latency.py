class Latency:
    Description = "Detects if model prediction latency exceeds the STL time bound."
    Formalism = "stl"
    Formula = "always (time_delta < 0.5)"
    Variables = ["time_delta"]
    Creation_Events = ["predict_start"]
    Events = {
        "Before": { "predict_start": [["model", "predict_transaction"]] },
        "After": { "predict_end": [["model", "predict_transaction"]] }
    }
    Parameters = ["transaction_id"]
    Handlers = { "Violation": "print('LATENCY VIOLATION: Transaction took too long!')" }
