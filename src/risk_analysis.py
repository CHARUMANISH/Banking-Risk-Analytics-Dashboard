import pandas as pd

def calculate_risk_score(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates a simple risk score using statistical indicators.
    """
    df["risk_score"] = (
        0.4 * df["loan_to_income_ratio"] +
        0.3 * df["credit_utilization"] +
        0.3 * df["missed_payments"]
    )
    return df

def identify_high_risk(df: pd.DataFrame, threshold=0.7) -> pd.DataFrame:
    """
    Flags high-risk customers.
    """
    return df[df["risk_score"] > threshold]

if __name__ == "__main__":
    print("Risk analytics module")
