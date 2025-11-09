import pandas as pd
from pathlib import Path
import json

DATA_PATH = Path("data/processed")
DATA_PATH.mkdir(parents=True, exist_ok=True)

def save_csv(data: list[dict], filename: str):
  df = pd.DataFrame(data)
  df.to_csv(DATA_PATH / f"{filename}.csv", index=False)
  
def save_json(data: list[dict], filename: str):
  with open(DATA_PATH / f"{filename}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)