from flask import Flask, render_template, redirect, url_for, request, session, flash
from models import db, Product, Order, OrderItem, Category, ContactMessage
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = "devkey"

db.init_app(app)

# --- HOME ---
@app.route('/')
def home():
    return redirect(url_for('view_products'))

# --- PRODUCTS ---
@app.route('/products')
def view_products():
    sort_option = request.args.get('sort', 'name_asc')

    if sort_option == 'price_asc':
        products = Product.query.order_by(Product.price.asc()).all()
    elif sort_option == 'price_desc':
        products = Product.query.order_by(Product.price.desc()).all()
    elif sort_option == 'stock_asc':
        products = Product.query.order_by(Product.stock.asc()).all()
    elif sort_option == 'stock_desc':
        products = Product.query.order_by(Product.stock.desc()).all()
    elif sort_option == 'name_desc':
        products = Product.query.order_by(Product.name.desc()).all()
    else: 
        products = Product.query.order_by(Product.name.asc()).all()

    categories = Category.query.all()

    return render_template(
        'products.html',
        categories=categories,
        products=products,
        sort_option=sort_option
    )

@app.route('/products/new', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        product = Product(
            name=request.form['name'],
            description=request.form['description'],
            price=float(request.form['price']),
            stock=int(request.form['stock']),
            image_url=request.form['image_url'],
            category_id=int(request.form['category_id'])
        )
        db.session.add(product)
        db.session.commit()
        flash("Product added successfully.")
        return redirect(url_for('view_products'))

    categories = Category.query.all()
    return render_template('add_product.html', categories=categories)

# --- SEARCH ---
@app.route('/search')
def search():
    query = request.args.get('q', '')
    results = []
    if query:
        results = Product.query.filter(Product.name.ilike(f'%{query}%')).all()
    return render_template(
        'products.html',
        categories=Category.query.all(),
        results=results,
        query=query
    )


# --- CART ---
@app.route('/cart')
def view_cart():
    cart = session.get('cart', {})
    products, total = [], 0
    for product_id, quantity in cart.items():
        product = Product.query.get(int(product_id))
        if product:
            subtotal = product.price * quantity
            total += subtotal
            products.append({
                'id': product.id,
                'name': product.name,
                'price': product.price,
                'quantity': quantity,
                'subtotal': subtotal
            })
    return render_template('cart.html', products=products, total=total)

@app.route('/cart/add/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    cart = session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    session['cart'] = cart
    flash("Product added to cart!")
    return redirect(url_for('view_products'))

@app.route('/cart/remove/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    cart = session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        session['cart'] = cart
        flash("Product removed from cart.")
    return redirect(url_for('view_cart'))

# --- CHECKOUT ---
@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    cart = session.get('cart', {})
    products, total = [], 0

    for product_id, quantity in cart.items():
        product = Product.query.get(int(product_id))
        if product:
            subtotal = product.price * quantity
            total += subtotal
            products.append({
                'id': product.id,
                'name': product.name,
                'price': product.price,
                'quantity': quantity,
                'subtotal': subtotal
            })

    if request.method == 'POST' and products:
        order = Order(
            customer_name=request.form['customer_name'],
            customer_email=request.form['customer_email'],
            customer_address=request.form['customer_address'],
            customer_phone=request.form.get('customer_phone', ''),
            total_price=total
        )
        db.session.add(order)
        db.session.flush()  

        for item in products:
            order_item = OrderItem(
                order_id=order.id,
                product_id=item['id'],
                quantity=item['quantity']
            )
            db.session.add(order_item)

            product = Product.query.get(item['id'])
            if product.stock >= item['quantity']:
                product.stock -= item['quantity']
            else:
                flash(f"Not enough stock for {product.name}.")
                db.session.rollback()
                return redirect(url_for('view_cart'))

        db.session.commit()
        session['cart'] = {}
        flash("Order placed successfully!")
        return redirect(url_for('order_success', order_id=order.id))

    return render_template('checkout.html', products=products, total=total)

    product = Product.query.get(item['id'])
    if product.stock >= item['quantity']:
        product.stock -= item['quantity']
    else:
        flash(f"Not enough stock for {product.name}.")
        db.session.rollback()
        return redirect(url_for('view_cart'))


        db.session.commit()
        session['cart'] = {}
        flash("Order placed successfully!")
        return redirect(url_for('order_success', order_id=order.id))

    return render_template('checkout.html', products=products, total=total)

@app.route('/order/<int:order_id>/success')
def order_success(order_id):
    order = Order.query.get_or_404(order_id)
    return render_template('order_success.html', order=order)

# --- CONTACT ---
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        msg = ContactMessage(
            name=request.form['name'],
            email=request.form['email'],
            message=request.form['message']
        )
        db.session.add(msg)
        db.session.commit()
        flash("Message received. Thank you.")
        return redirect(url_for('contact'))
    return render_template('contact.html')

# --- ABOUT ---
@app.route('/about')
def about():
    return render_template('about.html')

# --- ADMIN DASHBOARD ---
@app.route('/admin/dashboard')
def admin_dashboard():
    orders = Order.query.order_by(Order.timestamp.desc()).all()
    messages = ContactMessage.query.order_by(ContactMessage.created_at.desc()).all()

    total_revenue = db.session.query(db.func.sum(Order.total_price)).scalar() or 0
    total_orders = Order.query.count()
    total_items = db.session.query(db.func.sum(OrderItem.quantity)).scalar() or 0
    best_seller = db.session.query(
        Product.name, db.func.sum(OrderItem.quantity).label("sold")
    ).join(OrderItem).group_by(Product.id).order_by(db.desc("sold")).first()

    return render_template(
        'admin_dashboard.html',
        orders=orders,
        messages=messages,
        total_revenue=total_revenue,
        total_orders=total_orders,
        total_items=total_items,
        best_seller=best_seller
    )


@app.route('/admin/sales_report')
def admin_sales_report():
    total_revenue = db.session.query(db.func.sum(Order.total_price)).scalar() or 0

    total_orders = Order.query.count()

    total_items = db.session.query(db.func.sum(OrderItem.quantity)).scalar() or 0

    best_seller = db.session.query(
        Product.name, db.func.sum(OrderItem.quantity).label("sold")
    ).join(OrderItem).group_by(Product.id).order_by(db.desc("sold")).first()

    return render_template(
        'admin_sales_report.html',
        total_revenue=total_revenue,
        total_orders=total_orders,
        total_items=total_items,
        best_seller=best_seller
    )


if __name__ == '__main__':
    app.run(debug=True)
