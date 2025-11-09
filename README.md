# COMP3005-Assignment3
Students CRUD Application 
This application connects to a PostgreSQL database and performs the required CRUD (Create, Read, Update, Delete) operations for the Assignment 3 instructions.

Setup Instructions
 Install PostgreSQL/ pgAdmin4
 Install **Python 3.11+**
Create and Activate a Virtual Environment (Windows PowerShell)
python -m venv .venv . .\.venv\Scripts\Activate.ps1
Install the psyccopg binary dependency using: pip install psycopg2-binary==2.9.11
Run the SQL provided in the database scripts
Set environment variables in your terminal and replace the password portion with your actual pgAdmin password.
$env:PGHOST="localhost"
$env:PGPORT="5432"
$env:PGDATABASE="postgres"
$env:PGUSER="postgres"
$env:PGPASSWORD="Ankara200514"
Run the Python script by using ; python .\database.py
