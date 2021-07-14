# Django-Authentication-Template
Project template to handle user authentication in Django. It handles login, logout, sign up (creating new user), changing password and password reset (Forgot password).

## Technologies
Project is created with:
* Python version:  3.6.9
* Django version: 3.1.7

## Key Note
### 1. Configuring the settings.py to send emails
I added the EMAIL_BACKEND listed below to the settings file so we can send the email to the CLI (Command Line Interface). 
```
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```
This is only for testing purposes, For production, the backend is changed to an email sending service.
