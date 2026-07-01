from flask import Flask, render_template, request, redirect, url_for, session, flash

from products import PRODUCTS, CATEGORIES, CATEGORY_MAP, get_product, get_products, category_count

app = Flask(__name__)
app.secret_key = "abzaristan-dev-secret-key"


def format_price(price: int) -> str:
    return f"{price:,}".replace(",", "٬") + " تومان"


def render_stars(rating: float) -> str:
    full = int(rating)
    half = rating - full >= 0.5
    stars = "★" * full
    if half:
        stars += "½"
    stars += "☆" * (5 - len(stars.replace("½", "")))
    return stars


def discount_percent(product: dict) -> int:
    if not product.get("old_price"):
        return 0
    return round((1 - product["price"] / product["old_price"]) * 100)


def get_cart() -> dict:
    return session.get("cart", {})


def cart_count() -> int:
    return sum(get_cart().values())


def cart_items():
    cart = get_cart()
    items = []
    for pid_str, qty in cart.items():
        product = get_product(int(pid_str))
        if product:
            items.append({"product": product, "quantity": qty, "line_total": product["price"] * qty})
    return items


def cart_total() -> int:
    return sum(item["line_total"] for item in cart_items())


app.jinja_env.globals.update(
    format_price=format_price,
    render_stars=render_stars,
    discount_percent=discount_percent,
    CATEGORY_MAP=CATEGORY_MAP,
    CATEGORIES=CATEGORIES,
    cart_count=cart_count,
    category_count=category_count,
)


@app.route("/")
def index():
    featured = PRODUCTS[:8]
    return render_template("index.html", featured=featured)


@app.route("/products")
def products():
    category = request.args.get("category", "all")
    search = request.args.get("q", "")
    sort = request.args.get("sort", "default")
    items = get_products(category, search, sort)
    return render_template(
        "products.html",
        products=items,
        current_category=category,
        search=search,
        sort=sort,
    )


@app.route("/product/<int:product_id>")
def product_detail(product_id):
    product = get_product(product_id)
    if not product:
        flash("محصول مورد نظر یافت نشد.", "error")
        return redirect(url_for("products"))
    related = [p for p in PRODUCTS if p["category"] == product["category"] and p["id"] != product_id][:4]
    return render_template("product_detail.html", product=product, related=related)


@app.route("/cart")
def cart():
    items = cart_items()
    return render_template("cart.html", items=items, total=cart_total())


@app.route("/cart/add/<int:product_id>", methods=["POST"])
def cart_add(product_id):
    product = get_product(product_id)
    if not product:
        flash("محصول یافت نشد.", "error")
        return redirect(url_for("products"))

    quantity = max(1, min(99, request.form.get("quantity", 1, type=int)))
    cart = get_cart()
    cart[str(product_id)] = cart.get(str(product_id), 0) + quantity
    session["cart"] = cart
    flash(f"«{product['name']}» به سبد خرید اضافه شد.", "success")
    return redirect(request.referrer or url_for("cart"))


@app.route("/cart/update/<int:product_id>", methods=["POST"])
def cart_update(product_id):
    quantity = request.form.get("quantity", 1, type=int)
    cart = get_cart()
    pid = str(product_id)

    if quantity <= 0:
        cart.pop(pid, None)
    else:
        cart[pid] = min(99, quantity)

    session["cart"] = cart
    return redirect(url_for("cart"))


@app.route("/cart/remove/<int:product_id>", methods=["POST"])
def cart_remove(product_id):
    cart = get_cart()
    cart.pop(str(product_id), None)
    session["cart"] = cart
    flash("محصول از سبد خرید حذف شد.", "success")
    return redirect(url_for("cart"))


if __name__ == "__main__":
    app.run(debug=True, port=5000)