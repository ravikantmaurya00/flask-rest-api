# 🧩 Flask REST API — User Management System

A simple **RESTful API** built using **Flask** that performs CRUD (Create, Read, Update, Delete) operations on user data.  
This project is designed to demonstrate **API development fundamentals** using Python and Flask and can be tested using **Postman** or **Curl**.

---

## 📘 Overview

This project implements a basic **User Management REST API** that allows clients to:
- View all users
- View a single user by ID
- Add a new user
- Update existing user information
- Delete a user

Data is temporarily stored in an in-memory list (you can later connect it to a database like SQLite or MongoDB).

---

## ⚙️ Features

✅ **GET** all users  
✅ **GET** single user by ID  
✅ **POST** create a new user  
✅ **PUT** update existing user details  
✅ **DELETE** remove user  
✅ **Error handling** for invalid or missing data  
✅ **Clean, modular code** using Flask  

---

## 🧱 Project Structure

flask-rest-api/
│
├── app.py # Main Flask application file
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── users.json # (Optional) For data persistence

yaml
Copy code

---

## 🚀 Setup Instructions

Follow these steps to run the project locally.

### 1️⃣ Clone the Repository
```
       git clone https://github.com/<your-username>/flask-rest-api.git
        cd flask-rest-api
```
###2️⃣ Create a Virtual Environment
```
Copy 
python -m venv venv
```
####Activate it:
       Windows
```venv\Scripts\activate```
       Mac/Linux
  ```source venv/bin/activate```
####3️⃣ Install Dependencies
```pip install -r requirements.txt```
###4️⃣ Run the Application
```python app.py```
