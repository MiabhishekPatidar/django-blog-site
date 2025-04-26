# Django Blog Project

A simple **Django Blog Project** that allows users to create, view, update, and delete blog posts. This project is beginner-friendly and designed to help you learn Django step by step.

## 🚀 Features

✅ **Create a Post**: Add new blog posts with a title and content.  
✅ **View All Posts**: List all blog posts.  
✅ **View a Post by ID**: View a single post by its ID.  
✅ **Update a Post**: Modify the details of an existing post.  
✅ **Delete a Post**: Remove a post from the blog.  
✅ **Admin Interface**: Manage posts through Django's built-in admin interface.  
✅ **URL Routing**: Set up routes for blog pages.  
✅ **Templates**: Render HTML templates for displaying posts.

## 🛠 Technologies Used

- **Django**: Python-based web framework used to build the backend.
- **SQLite**: Database used to store posts and comments.
- **Python**: Programming language used to write the backend logic.

## ⚙️ Getting Started

### 1. Clone the Repository

git clone https://github.com/MiabhishekPatidar/django-blog-site.git  
cd django-blog-site

### 2. Set up Virtual Environment

python -m venv venv  

Activate the environment:  
- **Windows**:  
  venv\Scripts\activate  
- **Mac/Linux**:  
  source venv/bin/activate

### 3. Install Dependencies

pip install django

### 4. Create Django Project and App

Create a Django project:  
django-admin startproject blogsite  
cd blogsite  

Create a Django app:  
python manage.py startapp blog

### 5. Set Up Database Models

Add models for Post and Comment in the `blog/models.py` file.

### 6. Register Models in Admin

Register models in `blog/admin.py` to manage them through Django's admin interface.

### 7. Create Views for Posts

In `blog/views.py`, create views for displaying posts.

### 8. Define URLs

Set up URL routes in `blogsite/urls.py` for the home and post views.

Then, create a `urls.py` file inside the `blog` app to define the individual blog URLs.

### 9. Create Templates for Post List and Details

Create a `templates/blog` folder inside the blog app and add `post_list.html` and `post_detail.html` files.

### 10. Apply Migrations

Make migrations for the models and apply them to the database.

python manage.py makemigrations  
python manage.py migrate

### 11. Create Superuser for Admin

Create a superuser to access the Django admin panel.

python manage.py createsuperuser

### 12. Run the Development Server

Start the development server.

python manage.py runserver

## 💡 Admin Panel

Access the admin panel at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/). Log in using the superuser credentials you created.

## 📜 License

This project is open-source and free to use.

## 🧑‍💻 Author

GitHub: [MiabhishekPatidar](https://github.com/MiabhishekPatidar)
