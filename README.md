# 🌾 Smart Irrigation System

A modern, sensor-driven irrigation solution built to automate watering decisions, reduce water waste, and enhance crop yield — all from a sleek, real-time web dashboard.

---

## 🔧 Key Features

- 🌱 **Live Monitoring:** Soil moisture, temperature, and humidity data at your fingertips  
- 💧 **Smart Control:** Automated pump operation based on real-time conditions  
- 📊 **Data History:** Track and analyze sensor trends for efficient planning  
- 🌐 **Responsive UI:** Styled with Bootstrap and custom CSS for a smooth UX  
- 🔌 **IoT Integration:** MQTT-based communication for real-time updates  

---

## 🛠 Tech Stack

| Layer     | Tools Used                    |
|-----------|-------------------------------|
| Backend   | Python, Django, Django REST   |
| Frontend  | HTML, CSS, Bootstrap 5        |
| Database  | SQLite                        |
| IoT Comm  | MQTT (sensors to backend)     |

---

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/your-username/smart-irrigation-system.git
cd smart-irrigation-system

# Create a virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python manage.py runserver
