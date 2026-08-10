# Legacy Employee Portal

A beginner-friendly SQL Injection CTF challenge inspired by classic picoCTF-style web exploitation challenges.

## Challenge Description

The IT department recently migrated to a new authentication system, but one forgotten employee portal was left running.

The developers believed only employees knew about the portal and focused more on functionality than security.

Can you prove them wrong?

Your goal is to gain administrator access and retrieve the flag hidden in the admin dashboard.

**Category:** Web Exploitation

**Difficulty:** Easy

---

## Learning Objectives

This challenge teaches:

- SQL Injection fundamentals
- Authentication bypass attacks
- Login form exploitation
- SQL comments and query manipulation
- Understanding insecure database queries

---

## Vulnerability

The application constructs SQL queries using unsanitized user input.

Example:

```sql
SELECT * FROM users
WHERE username='<user_input>'
AND password='<password_input>'
```

Because user input is directly concatenated into the query, an attacker can manipulate the SQL statement and bypass authentication.

---

## Challenge Goal

1. Access the login portal.
2. Bypass authentication using SQL Injection.
3. Reach the administrator dashboard.
4. Capture the flag.

---

## Tech Stack

- Python
- Flask
- SQLite
- HTML/CSS

---

## Project Structure

```text
legacy-employee-portal/
│
├── app.py
├── init_db.py
├── flag.txt
├── requirements.txt
│
├── database/
│   ├── init.sql
│   └── employee.db
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   ├── admin.html
│   └── error.html
│
└── README.md
```

---

## Local Setup

### Clone the Repository

```bash
git clone <repository-url>
cd legacy-employee-portal
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Initialize Database

```bash
python init_db.py
```

### Run Application

```bash
python app.py
```

Application will be available at:

```text
http://127.0.0.1:5000
```

---

## Railway Deployment

1. Push the repository to GitHub.
2. Create a new Railway Project.
3. Select **Deploy from GitHub Repo**.
4. Choose this repository.
5. Set the start command:

```bash
gunicorn app:app
```

6. Wait for deployment to complete.
7. Go to **Settings → Networking**.
8. Click **Generate Domain**.
9. Open the generated Railway URL.

---

## Default Credentials

### Employee Account

```text
Username: john
Password: john123
```

### Administrator Account

```text
Username: admin
Password: ADMIN
```

---

## Flag Location

The flag is displayed on the administrator dashboard after successful authentication.

---

## Intended Solution

The intended solution is to identify and exploit the SQL Injection vulnerability in the login form to gain administrator access.

Example payloads:

```sql
' OR 1=1 --
```

```sql
admin' --
```

```sql
' OR role='admin' --
```

---

## Example Challenge Description (CTFd / picoCTF Style)

### Legacy Employee Portal

The IT department recently migrated to a new authentication system, but one forgotten employee portal was left online.

Rumor has it the developers were more concerned with functionality than security.

Can you find a way into the administrator dashboard and recover the flag?

**Category:** Web Exploitation

**Difficulty:** Easy

**Hint:** Sometimes the fastest way through a login form isn't knowing the password.

---

## Disclaimer

This application intentionally contains security vulnerabilities for educational and CTF purposes.

Do not deploy this application in production environments.

---

## Author

Created for cybersecurity training, workshops, and Capture The Flag (CTF) competitions.