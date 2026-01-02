import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """
    Loads raw banking data.
    """
    return pd.read_csv(path)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and prepares data for risk analysis.
    """
    df = df.dropna()
    df["loan_to_income_ratio"] = df["loan_amount"] / df["annual_income"]
    return df

if __name__ == "__main__":
    print("Data pipeline module for Banking Risk Analytics")
