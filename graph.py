import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/energy_log.csv")

plt.plot(df["Power"])
plt.title("Power Usage Over Time")
plt.xlabel("Reading Number")
plt.ylabel("Power (W)")
plt.show()