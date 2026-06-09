import streamlit as st
import pandas as pd
import time
import os

st.set_page_config(page_title="Smart Energy Dashboard", layout="wide")

st.title("⚡ Smart Energy Monitoring Dashboard")

file_path = "data/cloud_energy.csv"

# Auto refresh
refresh_interval = 5  # seconds

placeholder = st.empty()

while True:
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)

        # Convert time column
        df["Time"] = pd.to_datetime(df["Time"])

        with placeholder.container():

            # KPIs
            col1, col2, col3 = st.columns(3)

            col1.metric("🔌 Current Power (W)", f"{df['Power'].iloc[-1]:.2f}")
            col2.metric("⚡ Total Energy (kWh)", f"{df['Energy'].iloc[-1]:.4f}")
            col3.metric("💰 Total Cost (INR)", f"{df['Cost'].iloc[-1]:.2f}")

            # Alert
            if df["Alert"].iloc[-1] == "HIGH":
                st.error("🚨 High Power Usage Detected!")
            else:
                st.success("✅ System Normal")

            st.divider()

            # Charts
            st.subheader("📊 Power Usage Over Time")
            st.line_chart(df.set_index("Time")["Power"])

            st.subheader("⚡ Energy Consumption")
            st.line_chart(df.set_index("Time")["Energy"])

            st.subheader("💰 Cost Over Time")
            st.line_chart(df.set_index("Time")["Cost"])

            # Raw data
            st.subheader("📄 Data Log")
            st.dataframe(df.tail(20))

    else:
        st.warning("No data found. Run cloud_main.py first.")

    time.sleep(refresh_interval)