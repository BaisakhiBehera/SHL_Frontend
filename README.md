# SHL Assessment Recommender – Streamlit Frontend

This repository contains the **frontend code** for the SHL Assessment Recommendation System. It is built using **Streamlit** and provides an interactive UI where users can enter a job description or natural language query to receive relevant SHL assessment suggestions.

live link: https://shlfrontend-1.streamlit.app/

> 🛰️ The backend logic and recommendation engine is hosted separately in the https://github.com/BaisakhiBehera/SHL_Backend repository, which is exposed via a REST API.

## 🌐 Hosted On

- ✅ **Frontend:** Streamlit Cloud
- ✅ **Backend:** Render (accepts only POST requests)

## 💡 How It Works

1. The user inputs a job description or query into the Streamlit UI.
2. A POST request is sent to the backend API (`/api/recommend/` endpoint).
3. The backend processes the query using content-based filtering and returns 1–10 relevant assessments.
4. The frontend displays the results in a neat and readable table format.

## 📦 Technologies Used

- **Python 3.11+**
- **Streamlit**
- **Requests**
- **Pandas**

📁 Related Repository
👉 Backend Code: https://github.com/BaisakhiBehera/SHL_Backend
