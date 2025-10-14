from flask import jsonify,render_template,request,json
from app.models import Product_item

def routing(app):
    products=[]
    @app.route('/')
    def get_products():
        
        page=int(request.args.get("page"))
        per_page=8
        start_item=(page-1)*8
        end_item=start_item+per_page
        data=Product_item.query.all()
        for i in data:
            products.append({"image":i.image,
                             "product_name":i.product_name,
                             "price":i.price,
                             "description":i.description})


        return jsonify(products[start_item:end_item]),200
    
    @app.route('/html')
    def page():
        return render_template("index.html")
    @app.route('/click',methods=["GET"])
    def clicked_product():
        return jsonify({"message":"Thanks For Ordering We will get back soon with your order"})
    @app.route('/search')
    def searching_products():
        matched_products=[]
        name=request.args.get("products_name")
        for i in products:
            if name in i["product_name"].lower():  
                matched_products.append(i)

        if matched_products:
            return jsonify(matched_products), 200
        else:
            return jsonify({"message": "No data found"}), 404
