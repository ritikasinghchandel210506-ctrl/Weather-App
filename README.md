# ☁️ Modern Flask Weather Dashboard

A beautiful, light-weight, responsive weather application built with Python using the Flask framework. The application interfaces with the OpenWeatherMap API to provide real-time atmospheric metrics based on dynamic global location inputs. 

The interface features a custom dark-mode aesthetic utilizing glassmorphism styling parameters.

---

## ✨ Features

* **Global Search Capabilities:** Integrates an asynchronous two-step API handshake (Geocoding API + Current Weather API) to locate and retrieve metrics for any city globally.
* **Modern UI Engine:** Styled with an elegant dark glassmorphism layout, dropping blocky system frameworks for a responsive, clean look.
* **Robust Error Mitigation:** Gracefully catches network connectivity issues, API time-outs, and unrecognized or misspelled city inquiries using native Flask session flashing.
* **Auto-refresh Environment:** Automatically formats dynamic custom assets and rounds floats into legible integers.

---

## 🛠️ Tech Stack & Dependencies

* **Backend core:** Python 3.x, Flask (Routing, Engine, Sessions)
* **API Communications:** Requests library (HTTP protocol payload operations)
* **Frontend layout:** Jinja2 templates, standard HTML5, custom CSS3, Pico.css base layer

---

## 📁 Repository Directory Structure

```text
flask-weather-app/
│
├── static/
│   └── style.css       # Core styling & glassmorphism customization
│
├── templates/
│   └── index.html      # Jinja2 presentation layout view
│
├── app.py              # Application runner and core processing controller
├── requirements.txt    # Frozen dependency configuration catalog
└── README.md           # Documentation manifest