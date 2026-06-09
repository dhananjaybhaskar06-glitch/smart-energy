import streamlit as st
import pandas as pd
import os
from streamlit_autorefresh import st_autorefresh

# ===== CONFIG =====
st.set_page_config(page_title="Smart Energy Pro Dashboard", layout="wide")

st.title("⚡ Smart Energy Monitoring System (PRO)")

file_path = "data/cloud_energy.csv"

# ===== SIDEBAR =====
st.sidebar.header("⚙️ Settings")

refresh_rate = st.sidebar.slider("Refresh Rate (sec)", 2, 30, 5)
power_limit = st.sidebar.slider("Alert Threshold (W)", 200, 2000, 800)

st.sidebar.markdown("---")
st.sidebar.info("💡 Adjust threshold to trigger alerts")

# ===== AUTO REFRESH =====
st_autorefresh(interval=refresh_rate * 1000, key="refresh")

# ===== LOAD DATA =====
if os.path.exists(file_path):
    df = pd.read_csv(file_path)

    df["Time"] = pd.to_datetime(df["Time"])

    latest = df.iloc[-1]

    # ===== KPIs =====
    st.subheader("📊 Live Metrics")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("🔌 Power (W)", f"{latest['Power']:.2f}")
    col2.metric("⚡ Energy (kWh)", f"{latest['Energy']:.4f}")
    col3.metric("💰 Cost (INR)", f"{latest['Cost']:.2f}")
    col4.metric("🔋 Current (A)", f"{latest['Current']:.2f}")

    # ===== ALERT =====
    if latest["Power"] > power_limit:
        st.error(f"🚨 High Usage! Power exceeded {power_limit}W")
    else:
        st.success("✅ System Running Normally")

    st.divider()

    # ===== FILTER =====
    st.subheader("📅 Filter Data")

    start_date = st.date_input("Start Date", df["Time"].min().date())
    end_date = st.date_input("End Date", df["Time"].max().date())

    filtered = df[
        (df["Time"].dt.date >= start_date) &
        (df["Time"].dt.date <= end_date)
    ]

    # ===== CHARTS =====
    st.subheader("📈 Power Usage")
    st.line_chart(filtered.set_index("Time")["Power"])

    st.subheader("⚡ Energy Consumption")
    st.line_chart(filtered.set_index("Time")["Energy"])

    st.subheader("💰 Cost Trend")
    st.line_chart(filtered.set_index("Time")["Cost"])

    # ===== DOWNLOAD =====
    st.subheader("📥 Export Data")

    csv = filtered.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download CSV Report",
        data=csv,
        file_name="energy_report.csv",
        mime="text/csv"
    )

    # ===== TABLE =====
    st.subheader("📄 Recent Logs")
    st.dataframe(filtered.tail(20), use_container_width=True)

else:
    st.warning("⚠️ No data found. Run cloud_main.py first.")