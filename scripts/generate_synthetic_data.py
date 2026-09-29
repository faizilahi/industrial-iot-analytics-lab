import pandas as pd, numpy as np
from pathlib import Path
RNG=np.random.default_rng(15)
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data"; DATA.mkdir(parents=True, exist_ok=True)
rows=[]
for m in range(1,11):
  for t in range(100):
    temp=float(RNG.normal(70,5)); vib=float(RNG.normal(0.4,0.1))
    if m==7 and t>80: temp+=15; vib+=0.5
    rows.append({"machine_id":f"M{m:02d}","ts":t,"temp_c":round(temp,2),"vibration":round(vib,3)})
pd.DataFrame(rows).to_csv(DATA/"sensors.csv",index=False)
print("Wrote industrial sensors")

