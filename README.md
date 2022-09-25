# Simple Money Account Management System

This Simple Money Account Management System consist of four operations made
- Create New Investments Account
- View Accounts
- Transfer Balances to different Accounts
- Delete Investment Account

Frontend Framework and Dependency Packages
- VueJS Framework
- Bootstrap v5.2
- Vue-Router for Routing Pages
- Font-Awesome Icons

Backend Framework and Dependency Packages
- Python 3.10
- Flask-CORS
- Flask-Restful for REST API
- SQLAlchemy - ORM (Object Relational Mapper) for accessing and updating database
- mariadb - Connecting to MariaDB Databases
- pymysql - Connecter and extension for mariadb connector

All the requirements can be obtained in the requirements.txt in the backend-python folder

## Installing and Starting The Frontend and Backend
- Frontend
  1. Once forked, navigate to the frontend-vuejs folder
  2. Open your terminal/command prompt and type in `npm install` and it will install the required dependency packages
  3. To run, simply type in `npm run dev` or if you want to build it for production, `npm run build`

- Backend
  1. Once forked, navigate to the backend-python folder
  2. You will need to create your virtual environment from here, open Terminal/CMD and type int
    `python -m venv venv`
  3. Once created, activate the virtual environment by typing 
     `venv\Scripts\activate`
  4. It will activated when you have a `(base)` at the left side of terminal/CMD
  5. Next, install the required packages from the requirements.txt by typing in `pip install -r requirements.txt`
  6. Once successfully installed, type in `python main.py` to start the Flask App server
  - Note: Make sure to configure the database before starting the main server

## Configuring Backend API access in VueJS
In order to change the backend API URL, just change the server proxy located in the `vite.config.js`, 

## Configuring Database Connection
You can do so in `database.ini` to change the database configuration
