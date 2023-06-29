# API-for-a-CMS-application

This repository contains the codebase for a CMS application API built with Django.

## Description

The Django CMS API provides a backend system for managing users, posts/blogs, and likes. It allows you to perform CRUD operations on these entities and includes various access control mechanisms.

## Features

- User Management: Create, read, update, and delete user accounts.
- Post/Blog Management: Create, read, update, and delete posts/blogs. Retrieve the number of likes for each post/blog.
- Like Management: Create, read, update, and delete likes for posts/blogs.
- Access Control: Restricted access to PUT/DELETE APIs for posts/blogs, private posts/blogs accessible only by the owner, and public posts/blogs accessible by any user.
- Single Query Retrieval: Efficient retrieval of both posts/blogs and their likes within a single query.

## Technologies Used

- Django: a high-level Python web framework.
- Django REST Framework: a powerful and flexible toolkit for building Web APIs.
- SQLite: a lightweight, serverless database used for development.

## Installation

1. Clone the repository:`https://github.com/python-hacked/API-for-a-CMS-application.git`


2. Set up a virtual environment:python -m venv venv


3. Install the dependencies:pip install -r requirements.txt


4. Apply database migrations:`python manage.py makemikgrations`
and migrate `python manage.py migrate`

5. The API will be accessible at `http://localhost:8000/`.





