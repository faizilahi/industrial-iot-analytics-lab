from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"output"; OUT.mkdir(parents=True, exist_ok=True)
df=pd.read_csv(ROOT/"data"/"sensors.csv")
thr={"temp_c":85,"vibration":0.8}
df["alert"]=(df["temp_c"]>=thr["temp_c"])|(df["vibration"]>=thr["vibration"])
summary=df.groupby("machine_id",as_index=False).agg(alerts=("alert","sum"),avg_temp=("temp_c","mean"),avg_vib=("vibration","mean"))
summary["avg_temp"]=summary["avg_temp"].round(2); summary["avg_vib"]=summary["avg_vib"].round(3)
summary.to_csv(OUT/"summary.csv",index=False)
print(summary.sort_values("alerts",ascending=False).head())

