from flask import Flask,request,jsonify,render_template
app=Flask(__name__)

products=[{"product_name":"Ooty Tea","price":10},
    {"product_name":"Chennai Tea","price":20},
    {"product_name":"Madurai Tea","price":30}]

@app.route('/')
def get_products():
    return jsonify(products),200
@app.route('/click',methods=["GET"])
def clicked_product():
    return jsonify({"message":"Thanks For Ordering We will get back soonwith your order"})

@app.route('/html')
def page():
    return render_template("index.html")
if __name__=="__main__":
    app.run(debug=True)

