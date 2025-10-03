from flask import jsonify,render_template

products=[{"product_name":"Ooty Tea","price":10},
    {"product_name":"Chennai Tea","price":20},
    {"product_name":"Madurai Tea","price":30}]

def routing(app):

    @app.route('/')
    def get_products():
        return jsonify(products),200
    
    @app.route('/html')
    def page():
        return render_template("index.html")
    @app.route('/click',methods=["GET"])
    def clicked_product():
        return jsonify({"message":"Thanks For Ordering We will get back soonwith your order"})
