import random
import time
import csv
from datetime import datetime
import os

# Ensure folder exists
os.makedirs("data", exist_ok=True)

VOLTAGE = 230
COST_PER_UNIT = 6

energy = 0
file_path = "data/energy_log.csv"

with open(file_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Time","Voltage","Current","Power","Energy(kWh)","Cost(INR)","Alert"])

    while True:
        current = round(random.uniform(0.5, 5.0), 2)
        power = VOLTAGE * current
        energy += power / 1000 / 3600

        cost = energy * COST_PER_UNIT

        alert = "NORMAL"
        if power > 800:
            alert = "HIGH"

        now = datetime.now()

        print(f"{now} | Power={power:.2f}W | Energy={energy:.4f}kWh | Cost={cost:.2f} INR | {alert}")

        writer.writerow([now, VOLTAGE, current, power, energy, cost, alert])
        f.flush()

        time.sleep(2)