# Shopeasy – Database Assignment Project

This project was created as part of a **school Database Assignment** for the Full Stack Software Development course (2025).  
It is a Flask-based e-commerce web application with product categories, shopping cart, checkout system, contact form, and an admin dashboard.

---

## Features

- **Product Browsing**
  - View all products grouped by category (Books & Stationery, Groceries, Health & Wellness, Home & Cleaning).
  - Category banners for a modern "Tesco/Dunnes" look.
  - Products styled with category-specific color themes.

- **Shopping Cart**
  - Add/remove products to/from cart.
  - Auto-calculated totals with alternating row colors.
  - JavaScript confirmation before removing items.

- **Checkout**
  - Enter customer details (name, email, address, optional phone).
  - Place orders which are saved in the database.
  - Automatic stock reduction after purchase.
  - Order success confirmation page.

- **Contact**
  - Contact form with name, email, and message.
  - Messages stored in the database for admin review.

- **Admin Dashboard**
  - View all orders and contact messages.
  - Each order shows its line items.
  - Sales report including:
    - Total revenue
    - Total orders
    - Total items sold
    - Best-selling product

- **Database**
  - Seed script pre-populates 4 categories with 10 products each.
  - Uses SQLAlchemy ORM with SQLite (local) or PostgreSQL (deployment-ready).

- **Frontend Enhancements**
  - CSS with two-tone gradients (blue + golden beige).
  - Responsive grid for product cards.
  - Flash messages for user feedback.
  - JavaScript interactivity for smoother UX.

---

## How It Works (App Flow)

1. **Products Page** – Browse products by category.  
2. **Add to Cart** – Users can add multiple products.  
3. **Cart Page** – Shows items, quantities, and total. Remove confirmation via JS.  
4. **Checkout** – Enter customer info and confirm the order.  
5. **Order Success** – Order saved in database and stock reduced.  
6. **Contact Page** – Users send inquiries; stored in DB.  
7. **Admin Dashboard** – Staff view orders, contact messages, and sales report.

---

## Installation & Setup (Local)

1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/database_assignment.git
   cd database_assignment/shopeasy
