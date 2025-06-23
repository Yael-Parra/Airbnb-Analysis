<p align="center">
  <img src="img/logo2.png" alt="Airbnb Logo" width="200"/>
</p>

<h1 align="center" style="color: #FF5A5F;">Comprehensive Airbnb Market Analysis</h1>

<p align="center">
  Global & Madrid Focus • Business-Oriented Insights • Free Deployment via Docker & Power BI
</p>

---

## 🧭 Table of Contents

- [📌 Project Overview](#-project-overview)
- [📊 Key Insights](#-key-insights)
- [🎯 Strategic Takeaways](#-strategic-takeaways)
- [🛠️ Tools & Technologies](#-tools-&-technologies)
- [✍ Instructions](#-instructions)
- [📁 Project Structure](#-project-structure)
- [🌍 Dashboard Deployment](#-dashboard-deployment)
- [⚠️ Data Reliability](#️-data-reliability)
- [👩‍💻 Contributors](#-contributors)

---

## 📌 Project Overview

This repository presents an executive-level analysis of over **220,000 Airbnb listings** from **six global cities** (Madrid, Milan, London, New York, Sydney, Tokyo) spanning **2010–2020**.  
The goal: to extract actionable insights for **hosts, guests, and investors** by exploring pricing, availability, demand signals, and property types.

The final output includes a **Power BI dashboard**, **free-to-deploy with Docker & Nginx**, designed to make exploration intuitive and scalable.

---

## 📊 Key Insights

### 💡 Market Dynamics

- **Availability Drives Price**  
  Listings with >180 days availability are priced higher — hosts favor revenue per stay over occupancy volume.

- **Location = Value**  
  In Madrid, areas like **Retiro**, **Centro**, and **Arganzuela** command the highest prices. **Chamartín** and **Latina** are more budget-friendly.

- **Type Influences Revenue**  
  Hotel rooms top the price ladder, followed by entire homes. Private and shared rooms are significantly cheaper.

- **Popularity ≠ Premium**  
  More reviews don’t mean higher prices. Affordable listings often have higher review counts — popularity stems from accessibility, not exclusivity.

### 🌍 Global Perspective

- **Average Price:** ~$158 USD, with wide dispersion
- **Most Listings:** London leads volume; Tokyo is the most affordable
- **New York:** Higher prices, more reviews
- **Private Rooms:** High review rates, budget-friendly
- **Hotels:** Expensive but not necessarily well-reviewed

---

## 🎯 Strategic Takeaways

- **Hosts:** Price higher in premium locations and offer entire units for better ROI.
- **Guests:** Choose shared/private rooms and non-central zones for better value.
- **Investors:** Target full-home listings in high-demand neighborhoods for maximum yield.

---

## 🛠️ Tools & Technologies

### 🔎 Data Analysis & Cleaning

![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/-Pandas-150458?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/-NumPy-013243?logo=numpy&logoColor=white)
![SciPy](https://img.shields.io/badge/-SciPy-8CAAE6?logo=scipy&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/-Scikit--learn-F7931E?logo=scikit-learn&logoColor=white)

### 📈 Visualization & Reporting

![Matplotlib](https://img.shields.io/badge/-Matplotlib-11557C?logo=matplotlib&logoColor=white)
![Seaborn](https://img.shields.io/badge/-Seaborn-2D3E50?logo=seaborn&logoColor=white)
![Power BI](https://img.shields.io/badge/-Power%20BI-F2C811?logo=powerbi&logoColor=black)

### 🐳 Deployment

![Docker](https://img.shields.io/badge/-Docker-2496ED?logo=docker&logoColor=white)
![Nginx](https://img.shields.io/badge/-Nginx-009639?logo=nginx&logoColor=white)
- Interactive dashboard exported as **HTML from Power BI**
- Served via **Dockerized Nginx**
- 100% free to deploy locally or in cloud with no Power BI license required

### 🖥️ Architecture Diagram
![Architecture Diagram](https://media.discordapp.net/attachments/1379054411472699496/1386683211152752752/Pizarron_de_diagrama_de_flujo_en_estilo_de_bloques_de_colores_espaciados_en_azul_oscuro_y_azul_4.png?ex=685a98e0&is=68594760&hm=9aee8d28a7aa059663c9068aaba0ad94f49e7f93472613f593bd9ec43df7e3d9&=&format=webp&quality=lossless&width=1227&height=614)
---
## ✍ Instructions

In order for you to be able to check the dashboard in the web:
- Clone the repository in your device
```
git clone https://github.com/Yael-Parra/Airbnb-Analysis.git           # Better go check at the link
cd Airbnb-Analysis
```
- You need to have Docker
- You need to have a Nginx account
  - Then you need to put your token as in the .env file example
    
- Now, run as follows from the root of the project:
```
docker-compose --env-file .env up --build      # This is to build it
docker-compose down --rmi all                  # This is to eliminate it
```

---

## 📁 Project Structure

```
Airbnb-Analysis/
├── data/                         # Raw CSV files per city
├── eda/                          # Jupyter notebooks for analysis
├── img/                          # Visual assets (e.g. logo, dashboard screenshots)
├── powerbi-web/
├── processed_data/               # Cleaned and merged datasets
├── scripts/                      # Python scripts for data processing and merging
├── .env.example                  # You must change this with your own token
├── .gitignore
├── Airbnb Dashboard.pbix         # Power BI report source file
├── Dockerffile
├── Report Analysis Airbnb.pdf    # Executive PDF report (optional shareable version)
├── README.md
├── docker-compose.yaml
└── requirements.txt              # Python dependenciesREADME.md

```

---

## 🌍 Dashboard Deployment

<p align="center">
  <table>
    <tr>
      <td><img src="img/dashboard1.png" alt="Main Dashboard" height="400"/></td>
      <td><img src="img/Dashboard-movil.gif" alt="Mobile View" height="400"/></td>
    </tr>
  </table>
</p>

- Dashboard features filters by **city**, **neighborhood**, **accommodation type**, **price ranges**, and **availability**
- Mobile-optimized, highly visual, business-ready

> 🧪 `.pbix` and exported HTML included — no Power BI service needed.

---

## ⚠️ Data Reliability

The dataset has undergone **extensive cleaning**: missing data handling, price normalization, text unification, and suspicious entry filtering.  
However, variables like `last_review` and some geo fields are partially imputed — interpret with light caution.

---
## 👩‍💻 Contributors

We’re open to **collaborations**, **freelance opportunities**, or simply connecting to share ideas and perspectives.  
🤝 *Let’s connect and explore data possibilities together. Whether it's a creative project or a bold idea, we’d love to hear from you.*


| Name | GitHub | LinkedIn |
|------|--------|----------|
| **Abigail Masapanta** | [![GitHub](https://img.shields.io/badge/GitHub-f56a79?logo=github&logoColor=white)](https://github.com/abbyenredes) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/abigailmasapanta/) |
| **Andrea Alonso** | [![GitHub](https://img.shields.io/badge/GitHub-f56a79?logo=github&logoColor=white)](https://github.com/andalons) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/andrea-alonso-g/) |
| **Andreina Suescum** | [![GitHub](https://img.shields.io/badge/GitHub-f56a79?logo=github&logoColor=white)](https://github.com/mariasuescum) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/andreina-suescum/) |
| **Yael Parra** | [![GitHub](https://img.shields.io/badge/GitHub-f56a79?logo=github&logoColor=white)](https://github.com/Yael-Parra) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/yael-parra/) |




