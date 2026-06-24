# URL Shortener

A simple URL shortening web application built using Flask and SQLite.

## Overview

This project allows users to convert long URLs into shorter, easier-to-share links. Users can create custom short codes and use them to access the original URL through a shortened route.

The project was built as a learning exercise to understand:

* Flask web development
* HTTP requests and responses
* Routing
* HTML forms
* SQLite databases
* URL redirection

## Features

* Create short URLs from long URLs
* Custom short codes
* Store URL mappings in a database
* Redirect users from short URLs to original URLs
* Simple and lightweight interface

## Tech Stack

* Python
* Flask
* SQLite
* HTML

## How It Works

1. User enters a long URL.
2. User provides a custom short code.
3. The application stores the mapping in a database.
4. When a user visits the shortened URL, the application looks up the corresponding long URL.
5. The user is redirected to the original website.

## Project Structure

```text
project/
│
├── app.py
│
├── templates/
│   └── index.html
│
└── database/
```

## Future Improvements

* Automatic short code generation
* Click analytics
* User accounts
* URL validation
* Custom dashboard
* QR code generation

## Purpose

This project was created to gain practical experience with backend web development and understand how web applications process user requests, interact with databases, and perform URL redirection.

