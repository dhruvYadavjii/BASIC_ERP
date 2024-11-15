from flask import Flask, render_template, request, redirect, url_for
from models import add_product, get_all_products
from database import init_db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_product', methods=['GET', 'POST'])
def add_product_view():
    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        price = request.form['price']
        add_product(name, quantity, price)
        return redirect(url_for('view_products'))
    return render_template('add_product.html')

@app.route('/view_products')
def view_products():
    products = get_all_products()
    return render_template('view_products.html', products=products)

if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)