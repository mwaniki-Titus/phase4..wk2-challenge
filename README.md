# phase4..wk2-challenge
# SuperHeroes API

SuperHeroes API is a RESTful web service built with Flask, SQLAlchemy, and Flask-RESTful. It allows you to manage information about superheroes and their powers. This README provides an overview of the API, its features, and instructions for setting it up and using it.

# Table of Contents

Features
Getting Started
Prerequisites
Installation
Usage
Running the Application
API Endpoints
Contributing
License

# Features

Heroes: Retrieve a list of all heroes or a specific hero by ID.
Powers: Retrieve a list of all powers or a specific power by ID. Update power details using PATCH request.
Hero-Power Relationships: Create hero-power relationships.

# Getting Started

# Prerequisites


Before running the SuperHeroes API, ensure you have the following prerequisites installed on your system:

Python 3
Flask
SQLAlchemy
Flask-Migrate
Flask-RESTful
SQLite (or another database of your choice)
Installation
Clone the repository to your local machine:

bash
Copy code
git clone 


bash
Copy code
cd superheroes-api
Create a virtual environment (recommended):

bash
Activate the virtual environment:

bash
Copy code
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Usage

# Running the Application

Ensure you are in the project directory with the virtual environment activated.

Initialize the SQLite database (you can modify the database configuration in app.py if needed):

bash
Copy code
flask db init
flask db migrate
flask db upgrade
Start the Flask development server:

bash
Copy code
python app.py
The API should now be running locally

# API Endpoints

GET /heroes: Get a list of all heroes.
GET /heroes/<int:id>: Get a specific hero by ID.
GET /powers: Get a list of all powers.
GET /powers/<int:id>: Get a specific power by ID.
PATCH /powers/<int:id>: Update a specific power by ID.
POST /hero_powers: Create a new hero-power relationship.

# Contributing

Contributions to this project are welcome. You can contribute by opening issues, providing feedback, or submitting pull requests. Please review our Contribution Guidelines for more details.

# License

This project is licensed under the MIT License - @mwaniki-Titus.

