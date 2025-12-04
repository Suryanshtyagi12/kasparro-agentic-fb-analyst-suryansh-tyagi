# src/utils/schema_validator.py
from typing import Dict, Any
import pandas as pd

EXPECTED_SCHEMA = {
    "campaign_name": str,
    "adset_name": str,
    "date": "datetime",
    "spend": float,
    "impressions": float,
    "clicks": float,
    "ctr": float,
    "purchases": float,
    "revenue": float,
    "roas": float,
    "creative_type": str,
    "creative_message": str,
    "audience_type": str,
    "platform": str,
    "country": str
}

class SchemaValidationError(Exception):
    pass

def validate_and_normalize(df: pd.DataFrame) -> pd.DataFrame:
    missing = [c for c in EXPECTED_SCHEMA if c not in df.columns]
    if missing:
        raise SchemaValidationError(f"Missing required columns: {missing}")

    # Coerce types where possible, track issues
    df = df.copy()
    # date
    if EXPECTED_SCHEMA["date"] == "datetime":
        try:
            df["date"] = pd.to_datetime(df["date"], errors="coerce")
        except Exception:
            df["date"] = pd.to_datetime(df["date"], errors="coerce")
    # numeric columns
    numeric_cols = ["spend","impressions","clicks","ctr","purchases","revenue","roas"]
    for c in numeric_cols:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    # basic checks
    nan_cols = {c: int(df[c].isna().sum()) for c in df.columns if df[c].isna().any()}
    if any(df[numeric_cols].isna().all(axis=1)):
        # rows that lost all numeric metrics
        raise SchemaValidationError("Some rows have all numeric metrics missing.")
    # Optional: drop rows with essential NaNs
    df = df.dropna(subset=["date","campaign_name","impressions","clicks"], how="any")
    return df
