import numpy as np
import pandas as pd


# Helper functions
def _clamp(value: float) -> float:
    # Clamp value to [0, 1] range and round to 2 decimal places
    return round(max(0.0, min(1.0, value)), 2)


def _require_columns_(df: pd.DataFrame, cols: list[str], name: str) -> bool:
    missing = [c for c in cols if c not in df.columns]
    if missing:
        print(f"Missing columns for {name}: {missing} -- skipping")
        return False
    return True


# disposition effect
def detect_dispoition_effect(df: pd.DataFrame) -> dict:

    required = ["BB_lower", "BB_upper", "BB_middle", "Close", "Open"]
    if not _require_columns_(df, required, "disposition effect"):
        return {"score": None, "label": "N/A", "explanation": "Insufficient data."}
