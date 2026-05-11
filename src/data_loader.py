import pandas as pd
import os

def save_dataset(df: pd.DataFrame, path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)


def load_dataset(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def dataset_exists(path: str) -> bool:
    return os.path.exists(path)