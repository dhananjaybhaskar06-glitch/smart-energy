# ⚡ Smart Energy Monitoring System (PRO)

🚀 A **software-based IoT simulation project** that tracks energy usage, sends data to the cloud, and displays a real-time interactive dashboard.

---

## 📌 Features

* ⚡ Real-time energy simulation using Python
* ☁️ Cloud integration with ThingSpeak API
* 📊 Interactive dashboard using Streamlit
* 🚨 Smart alert system for high power usage
* 📅 Date filtering for analytics
* 📥 Downloadable CSV reports
* 🔄 Auto-refresh live data

---

## 🛠 Tech Stack

* Python 🐍
* Streamlit 📊
* Pandas 📁
* Requests 🌐
* ThingSpeak API ☁️

---

## 📂 Project Structure

```
smart-energy/
│
├── cloud_main.py          # Data simulation + cloud upload
├── pro_dashboard.py       # Streamlit dashboard UI
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
└── data/
    └── cloud_energy.csv   # Generated data logs
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/YOUR_USERNAME/smart-energy.git
cd smart-energy
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ How to Run

### 🔹 Step 1: Run simulation

```
python cloud_main.py
```

### 🔹 Step 2: Run dashboard

```
streamlit run pro_dashboard.py
```

---

## 📊 Output

* 📈 Live energy graphs
* ⚡ Power usage tracking
* 💰 Cost calculation
* 🚨 Alerts for high consumption

---

## 🔐 Note

Replace your API key in `cloud_main.py`:

```
API_KEY = "YOUR_API_KEY"
```

⚠️ Do not upload your real API key to GitHub.

---

## 💼 Use Case

This project demonstrates:

* IoT simulation without hardware
* Real-time data processing
* Dashboard development
* Cloud API integration

Perfect for:

* Student portfolios 🎓
* Internship projects 💼
* Resume showcase 🚀

---

## 👨‍💻 Author

**Dhananjay Bhaskar**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
