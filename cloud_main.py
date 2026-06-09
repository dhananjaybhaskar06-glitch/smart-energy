import random
import time
import csv
import requests
from datetime import datetime
import os

# ===== SETTINGS =====
API_KEY = "USEG72QOW5AW1C5L"   # ✅ your ThingSpeak API key
VOLTAGE = 230
COST_PER_UNIT = 6

# Create data folder
os.makedirs("data", exist_ok=True)

energy = 0
file_path = "data/cloud_energy.csv"

# Create CSV file
with open(file_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Time","Voltage","Current","Power","Energy","Cost","Alert"])

    while True:
        # Simulated current
        current = round(random.uniform(0.5, 5.0), 2)

        # Calculations
        power = VOLTAGE * current
        energy += power / 1000 / 3600
        cost = energy * COST_PER_UNIT

        # Alert logic
        alert = "NORMAL"
        if power > 800:
            alert = "HIGH"

        now = datetime.now()

        # Print output
        print(f"{now} | {power:.2f}W | {energy:.4f}kWh | {cost:.2f} INR | {alert}")

        # Save to CSV
        writer.writerow([now, VOLTAGE, current, power, energy, cost, alert])
        f.flush()

        # Send to ThingSpeak
        url = "https://api.thingspeak.com/update"
        payload = {
            "api_key": "USEG72QOW5AW1C5L",     # ✅ FIXED
            "field1": VOLTAGE,      # ✅ FIXED (capital)
            "field2": current,
            "field3": power,
            "field4": energy,
            "field5": cost
        }

        try:
            response = requests.get(url, params=payload)
            print("Sent to cloud:", response.status_code)
        except Exception as e:
            print("Internet error:", e)

        # Wait 15 seconds (ThingSpeak limit)
        time.sleep(15)