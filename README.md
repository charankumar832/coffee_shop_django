# Kafe` with K - Coffee Shop Project

## About the Project

**Kafe` with K** is a Django-based coffee shop web application designed to showcase products, provide contact options, and offer a pleasant browsing experience.  

Key features of the project:

- **Home Page:**  
  - A carousel with 3 images of the coffee shop and inspiring quotes.  
  - A preview of some of the products offered.  
  - Footer with social media links (Facebook, Instagram, Twitter X, Pinterest).  

- **Navbar:**  
  - The coffee shop name "Kafe`" links to the home page.  
  - Links to **Home**, **Products**, and **Contact Us** pages.  

- **Products Page:**  
  - Displays all products with images, names, descriptions, and categories.  
  - Pagination is implemented to navigate through products easily.  
  - Navbar and footer are consistent with the home page.  

- **Contact Page:**  
  - Displays coffee shop address, phone number, email, and a map.  
  - Contact form with **Name**, **Email**, and **Message** fields to send messages.  
  - Messages will be replied to via the provided email.  

- **Search Functionality:**  
  - Allows users to search for products easily.  

This project demonstrates **Django best practices**, responsive design using **Bootstrap 5**, and CRUD management of products through the admin panel.

---

## Project Setup Instructions

Follow these steps to get the project running locally:

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd <project-folder>

### 2. create virtual environment
# Windows
python -m venv env

# Mac/Linux
python3 -m venv env

### 3.Activate virtual environment
# Windows
env\Scripts\activate

# Mac/Linux
source env/bin/activate

### 4. Install project dependencies

pip install -r requirements.txt

### 5. Run migrations to create the database

python manage.py migrate

### 6. Create a superuser

python manage.py createsuperuser

### 7. Add initial product entries

Log in to the Django admin panel: http://127.0.0.1:8000/admin/
Add some product entries (e.g., coffee, burgers) so that products are visible on both the homepage and products page.

### 8. Run the development server

python manage.py runserver








