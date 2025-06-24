# 📝 Notes API

A minimal Flask-based REST API for creating, retrieving, and deleting notes—powered by MySQL, SQLAlchemy, and Flask-Migrate.

---

## 🚀 Features

- Create new notes (`POST /add-note`)
- Fetch all notes (`GET /notes`)
- Delete a note by ID (`DELETE /delete-note/<id>`)
- Environment-based configuration
- Graceful error handling with logging

---

## 🏗️ Tech Stack

- Python 3.x
- Flask
- SQLAlchemy
- MySQL
- Flask-Migrate
- python-dotenv
- Logging via RotatingFileHandler

---

## ⚙️ Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/notes_api.git
   cd notes_api
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure environment variables**
   Create a '.env' file:

   ```Dotenv
   FLASK_APP=run.py
   FLASK_ENV=development
   SQLALCHEMY_DATABASE_URI="mysql+pymysql://username:password@localhost/notes_db"
   SECRET_KEY="your-secret-key"
   ```

4. **Initialize the Database**

   ```Bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

5. **Run the application**
   ```Bash
   python run.py
   ```
