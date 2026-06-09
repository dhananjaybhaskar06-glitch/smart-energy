import pandas as pd
import os

os.makedirs("outputs", exist_ok=True)

df = pd.read_csv("data/energy_log.csv")

total_energy = df["Energy(kWh)"].iloc[-1]
total_cost = df["Cost(INR)"].iloc[-1]
max_power = df["Power"].max()

report = f"""
SMART ENERGY REPORT

Total Energy Used: {total_energy:.4f} kWh
Total Cost: {total_cost:.2f} INR
Maximum Power: {max_power:.2f} W
"""

with open("outputs/report.txt", "w", encoding="utf-8") as f:
    f.write(report)

print(report)