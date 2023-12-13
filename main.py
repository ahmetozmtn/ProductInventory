from flask import Flask, render_template, request, redirect, url_for
from models import Product, app, db
import os
import secrets


with app.app_context():
    db.create_all()


@app.route("/products")
def products():
    products = Product.query.all()
    return render_template("products.html", products=products)


@app.route("/productadd")
def productadd():
    return render_template("productadd.html", error="")


if __name__ == '__main__':
    app.run(debug=True)
