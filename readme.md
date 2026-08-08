# Legacy Employee Portal

## Challenge Information

| Field          | Value                  |
| -------------- | ---------------------- |
| Challenge Name | Legacy Employee Portal |
| Category       | Web Exploitation       |
| Difficulty     | Easy                   |
| Author         | Priyanshi              |
| Platform       | Flask + SQLite         |

---

## Description

The IT department recently migrated to a new authentication system, but one forgotten web application was left running.

The developers were more focused on functionality than security, and they believed only employees knew about this portal.

Can you prove them wrong?

Gain access to the administrator dashboard and capture the flag.

---

## Objective

Your goal is to:

1. Analyze the login functionality.
2. Gain administrator access.
3. Capture the flag hidden within the admin dashboard.

---

## Skills Tested

* Web Application Enumeration
* Authentication Bypass
* SQL Injection
* Basic Session Management
* SQLite Query Analysis

---





---

### Build and Run



The application will be available at:

```text
http://localhost:5000
```

---



## Project Structure

```text
legacy-employee-portal/
│
├── app.py
├── init_db.py
├── flag.txt
├── requirements.txt
|
|
├── .gitignore
├
│
├── database/
│   └── init.sql
│
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   └── admin.html
│
└── static/
    └── css/
        └── style.css
```

---

## Flag Location

The flag is accessible only after successfully obtaining administrator privileges.

---





---

## Intended Learning Outcomes

Participants should learn:

* Why dynamic SQL queries are dangerous
* How SQL Injection can bypass authentication
* The importance of parameterized queries
* Basic web application security concepts

---

## Disclaimer

This application intentionally contains security vulnerabilities for educational and training purposes only.

Do not deploy this application in a production environment.

---

## License

Educational Use Only
