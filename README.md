# Flask Task Master App

A simple todo application built with Flask and SQLAlchemy for managing tasks.

## What This Project Does

This is a web-based todo list application where users can:
- Add new tasks
- Edit existing tasks
- Delete tasks (with confirmation modal)
- View all tasks with creation timestamps

## Technologies Used

- **Flask** - Python web framework for the backend
- **SQLAlchemy** - Database ORM for data management
- **SQLite** - Lightweight database for storing tasks
- **HTML/Jinja2** - Frontend templating
- **CSS** - Styling 

## Project Structure

- `app.py` - Main Flask application with routes and database model
- `templates/index.html` - Main page displaying todo list
- `templates/update.html` - Page for editing tasks 
- `templates/base.html` - Base template
- `static/css/main.css` - Styling

## Database Model

Uses a `Todo` model with:
- `id` - Primary key
- `content` - Task text (max 200 characters)
- `completed` 
- `date_created` - Automatic timestamp
