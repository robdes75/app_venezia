import pandas as pd
import json
import os

input_file = "punti.xlsx"
output_dir = "data"
output_file = os.path.join(output_dir, "punti.json")

os.makedirs(output_dir, exist_ok=True)

df = pd.read_excel(input_file)

records = []

for _, r in df.iterrows():
    records.append({
        "lat": float(r["LAT"]),
        "lon": float(r["LON"]),
        "tipo": str(r["TIPO"]).lower(),
        "nome": str(r["NOME"]),
        "desc": {
            "it": str(r["DESC_IT"]),
            "en": str(r["DESC_EN"])
        }
    })

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(records, f, ensure_ascii=False)

print("Creato data/punti.json")
