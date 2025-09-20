# Shopeasy – Online Store (Flask + PostgreSQL)

Shopeasy is a simple e-commerce web application built using **Flask**, **PostgreSQL**, and **SQLAlchemy**.  
It allows customers to browse products, add them to a shopping cart, place orders, and contact the store.  
Admins can manage products and view sales reports through a dashboard.

---

## Features

### Customer-facing
- Browse products by **category** with Tesco-style section banners.  
- Product cards with images, stock levels, and prices.  
- Add/remove items from the **shopping cart** with JavaScript confirmation.  
- Auto-calculating cart totals with live updates.  
- Checkout form with order summary.  
- Contact page for customer messages.  
- Responsive design with modern UI styling (blue + golden-beige accents).  

### Admin-facing
- Dashboard displaying:
  - Recent orders (with line-item details).  
  - Customer contact messages.  
  - Sales report: revenue, total orders, best-selling product, items sold.  
- Ability to add products (CRUD).  

---

## Technologies Used

- **Backend**: Flask (Python), SQLAlchemy ORM  
- **Database**: PostgreSQL (local + Render cloud)  
- **Frontend**: HTML5, CSS3, JavaScript (vanilla JS for interactivity)  
- **Deployment**: Render (Heroku-compatible Procfile)  
- **Version Control**: Git & GitHub  

---

## Installation & Setup (Local)

1. **Clone this repo**:
   ```bash
   git clone https://github.com/feliciaotieno/database_assignment.git
   cd shopeasy
