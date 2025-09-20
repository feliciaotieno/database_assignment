from app import app, db
from models import Category, Product

def reset_and_seed():
    with app.app_context():
        db.drop_all()
        db.create_all()

        categories = {
            "Books & Stationery": {
                "banner_url": "images/categories/books.jpg",
                "products": [
                    {"name": "Notebook A5", "description": "Lined notebook for school or office use.", "price": 2.49, "stock": 100, "image_url": "images/products/notebook.jpg"},
                    {"name": "Ballpoint Pens (Pack of 10)", "description": "Smooth-writing blue pens.", "price": 3.99, "stock": 200, "image_url": "images/products/pens.jpg"},
                    {"name": "Office Desk Organizer", "description": "Keep your workspace tidy.", "price": 12.50, "stock": 50, "image_url": "images/products/organizer.jpg"},
                    {"name": "Stapler with Staples", "description": "Durable stapler with 1000 staples included.", "price": 5.99, "stock": 80, "image_url": "images/products/stapler.jpg"},
                    {"name": "Highlighter Set", "description": "Pack of 5 bright highlighters.", "price": 4.50, "stock": 120, "image_url": "images/products/highlighters.jpg"},
                    {"name": "Sketch Pad", "description": "A4 pad with 100 sheets for drawing.", "price": 6.99, "stock": 60, "image_url": "images/products/sketchpad.jpg"},
                    {"name": "Sticky Notes", "description": "Assorted colours, 400 sheets.", "price": 3.20, "stock": 150, "image_url": "images/products/sticky_notes.jpg"},
                    {"name": "Binder Folders (Set of 3)", "description": "Strong folders for organizing papers.", "price": 7.25, "stock": 70, "image_url": "images/products/folders.jpg"},
                    {"name": "Scientific Calculator", "description": "Ideal for students and professionals.", "price": 14.99, "stock": 40, "image_url": "images/products/calculator.jpg"},
                    {"name": "Desk Lamp", "description": "LED lamp with adjustable brightness.", "price": 19.99, "stock": 30, "image_url": "images/products/desk_lamp.jpg"},
                ]
            },
            "Groceries": {
                "banner_url": "images/categories/groceries.jpg",
                "products": [
                    {"name": "Bananas (1kg)", "description": "Fresh bananas by weight.", "price": 1.89, "stock": 120, "image_url": "images/products/bananas.jpg"},
                    {"name": "Organic Whole Milk (1L)", "description": "Creamy organic milk.", "price": 1.35, "stock": 80, "image_url": "images/products/milk.jpg"},
                    {"name": "Frozen Pizza", "description": "Cheese and tomato frozen pizza.", "price": 3.75, "stock": 60, "image_url": "images/products/pizza.jpg"},
                    {"name": "Irish Butter (250g)", "description": "Rich and creamy butter.", "price": 2.20, "stock": 70, "image_url": "images/products/butter.jpg"},
                    {"name": "Free Range Eggs (6 pack)", "description": "Freshly laid eggs.", "price": 2.99, "stock": 100, "image_url": "images/products/eggs.jpg"},
                    {"name": "Fresh Bread Loaf", "description": "Soft and crusty bakery bread.", "price": 2.50, "stock": 90, "image_url": "images/products/bread.jpg"},
                    {"name": "Cheddar Cheese (200g)", "description": "Mature cheddar block.", "price": 3.40, "stock": 60, "image_url": "images/products/cheese.jpg"},
                    {"name": "Crisps (150g)", "description": "Sea salt potato crisps.", "price": 1.80, "stock": 110, "image_url": "images/products/crisps.jpg"},
                    {"name": "Orange Juice (1L)", "description": "No added sugar, 100% juice.", "price": 2.10, "stock": 85, "image_url": "images/products/juice.jpg"},
                    {"name": "Chicken Breast (500g)", "description": "Fresh Irish chicken breast.", "price": 5.99, "stock": 50, "image_url": "images/products/chicken.jpg"},
                ]
            },
            "Health & Wellness": {
                "banner_url": "images/categories/health.jpg",
                "products": [
                    {"name": "Vitamin C Tablets (100 pack)", "description": "Immune support.", "price": 8.99, "stock": 40, "image_url": "images/products/vitamins.jpg"},
                    {"name": "Paracetamol (16 tablets)", "description": "Pain relief.", "price": 2.50, "stock": 90, "image_url": "images/products/paracetamol.jpg"},
                    {"name": "Reusable Water Bottle", "description": "Eco-friendly BPA-free bottle.", "price": 9.99, "stock": 30, "image_url": "images/products/water_bottle.jpg"},
                    {"name": "Yoga Mat", "description": "Non-slip exercise mat.", "price": 14.99, "stock": 25, "image_url": "images/products/yoga_mat.jpg"},
                    {"name": "Protein Powder (1kg)", "description": "Vanilla flavour supplement.", "price": 24.99, "stock": 20, "image_url": "images/products/protein_powder.jpg"},
                    {"name": "First Aid Kit", "description": "Compact kit with essentials.", "price": 12.50, "stock": 35, "image_url": "images/products/first_aid.jpg"},
                    {"name": "Hand Sanitizer (250ml)", "description": "Kills 99.9% of germs.", "price": 3.50, "stock": 100, "image_url": "images/products/sanitizer.jpg"},
                    {"name": "Face Masks (10 pack)", "description": "Disposable protective masks.", "price": 6.99, "stock": 70, "image_url": "images/products/masks.jpg"},
                    {"name": "Herbal Tea (20 bags)", "description": "Chamomile tea for relaxation.", "price": 4.25, "stock": 80, "image_url": "images/products/herbal_tea.jpg"},
                    {"name": "Digital Thermometer", "description": "Quick and accurate reading.", "price": 11.99, "stock": 40, "image_url": "images/products/thermometer.jpg"},
                ]
            },
            "Home & Cleaning": {
                "banner_url": "images/categories/home.jpg",
                "products": [
                    {"name": "All-Purpose Cleaner (1L)", "description": "Fresh citrus scent.", "price": 3.10, "stock": 60, "image_url": "images/products/cleaner.jpg"},
                    {"name": "Laundry Detergent (20 washes)", "description": "Effective stain removal.", "price": 7.49, "stock": 45, "image_url": "images/products/detergent.jpg"},
                    {"name": "Paper Towels (6 pack)", "description": "Strong and absorbent.", "price": 5.25, "stock": 50, "image_url": "images/products/paper_towels.jpg"},
                    {"name": "Dishwashing Liquid (500ml)", "description": "Cuts grease fast.", "price": 2.20, "stock": 75, "image_url": "images/products/dish_liquid.jpg"},
                    {"name": "Glass Cleaner (500ml)", "description": "Streak-free shine.", "price": 2.99, "stock": 65, "image_url": "images/products/glass_cleaner.jpg"},
                    {"name": "Floor Mop", "description": "Easy wring with refill head.", "price": 9.99, "stock": 40, "image_url": "images/products/mop.jpg"},
                    {"name": "Vacuum Cleaner Bags (5 pack)", "description": "Universal fit bags.", "price": 6.50, "stock": 55, "image_url": "images/products/vacuum_bags.jpg"},
                    {"name": "Air Freshener Spray", "description": "Lavender scent.", "price": 3.75, "stock": 70, "image_url": "images/products/air_freshener.jpg"},
                    {"name": "Bin Bags (20 pack)", "description": "Strong and leak-proof.", "price": 4.10, "stock": 90, "image_url": "images/products/bin_bags.jpg"},
                    {"name": "Bleach (1L)", "description": "Kills germs and whitens.", "price": 1.80, "stock": 100, "image_url": "images/products/bleach.jpg"},
                ]
            }
        }

        for cat_name, cat_data in categories.items():
            category = Category(name=cat_name, banner_url=cat_data["banner_url"])
            db.session.add(category)
            db.session.flush()

            for p in cat_data["products"]:
                product = Product(
                    name=p["name"],
                    description=p["description"],
                    price=p["price"],
                    stock=p["stock"],
                    image_url=p["image_url"],
                    category_id=category.id
                )
                db.session.add(product)

        db.session.commit()
        print("Database reset and seeded with banners + 10 products per category!")

if __name__ == "__main__":
    reset_and_seed()
