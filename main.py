from flask import Flask, render_template, request, redirect, url_for
from models import Product, app, db
import os
import secrets


with app.app_context():
    db.create_all()


UPLOAD_FOLDER = 'static/uploads'
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', "webp"}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/products")
def products():
    products = Product.query.all()
    return render_template("products.html", products=products)


@app.route("/productadd")
def productadd():
    return render_template("productadd.html", error="")


@app.route("/products/<string:id>")
def productsStockAdd(id):
    product_detail = Product.query.filter_by(id=id).first()
    return render_template("details.html", product_detail=product_detail)


@app.route("/productstockreduce/<string:id>")
def productsStockreduce(id):
    product_stockadd = Product.query.filter_by(id=id).first()
    product_stockadd.stockCount -= 1
    db.session.commit()
    return redirect(url_for("products"))


@app.route("/productstockadd/<string:id>")
def productsStockadd(id):
    product_stockadd = Product.query.filter_by(id=id).first()
    product_stockadd.stockCount += 1
    db.session.commit()
    return redirect(url_for("products"))


@app.route("/products/delete/<string:id>")
def deleteProduct(id):
    product = Product.query.filter_by(id=id).first()
    folder = "static"
    image = product.productImg
    image_folder = os.path.join(folder, image)
    if os.path.exists(image_folder):
        os.remove(image_folder)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for("products"))


@app.route("/paddtoDb", methods=["POST", "GET"])
def productAddToDB():
    if request.method == "POST":
        product_name = request.form.get("pname")
        product_stock = request.form.get("pstock")
        product_desc = request.form.get("pdesc")
        if "file" not in request.files:
            error = "Dosya seçmeniz gerek"
            return render_template("productadd.html", error=error)
        file = request.files['file']
        if file.filename == "":
            error = "Dosya seçmeniz gerek"
            return render_template("productadd.html", error=error)

        if file and allowed_file(file.filename):
            filename = file.filename
            random_name = secrets.token_hex(8)
            file_ext = os.path.splitext(filename)[1]
            new_filename = random_name + file_ext
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_filename))
            file_path = os.path.join("uploads/" + new_filename)
            print(file_path)
            new_product = Product(
                productName=product_name, stockCount=product_stock, productDesc=product_desc, productImg=file_path)
            db.session.add(new_product)
            db.session.commit()
            return redirect(url_for('products'))
        error = "Geçersiz dosya uzantısı! Desteklenen uzantılar: png, jpg, jpeg, gif, webp"
        return render_template("productadd.html", error=error)


if __name__ == '__main__':
    app.run(debug=True)
