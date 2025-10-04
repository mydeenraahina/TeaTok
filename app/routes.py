from flask import jsonify,render_template,request

products = [
    {"image": "/static/tea.jpg", "product_name": "Ooty Tea", "price": 10,
     "description": "Famous Nilgiri tea with a strong aroma and smooth flavor."},
    
    {"image": "/static/tea (1).jpg", "product_name": "Chennai Tea", "price": 20,
     "description": "Classic South Indian style tea, strong and refreshing."},
    
    {"image": "/static/tea (2).jpg", "product_name": "Madurai Tea", "price": 30,
     "description": "Rich and bold tea known for its strong taste and deep color."},
    
    {"image": "/static/tea (3).jpg", "product_name": "Darjeeling Tea", "price": 25,
     "description": "Light, floral flavor, often called the 'Champagne of Teas'."},
    
    {"image": "/static/tea (4).jpg", "product_name": "Assam Tea", "price": 22,
     "description": "Strong, malty tea perfect for breakfast blends."},
    
    {"image": "/static/tea (5).jpg", "product_name": "Munnar Tea", "price": 18,
     "description": "Smooth tea grown in the misty hills of Kerala."},
    
    {"image": "/static/tea (6).jpg", "product_name": "Kolkata Masala Tea", "price": 28,
     "description": "Spiced milk tea with ginger, cardamom, and cinnamon."},
    
    {"image": "/static/tea (7).jpg", "product_name": "Kashmiri Kahwa", "price": 35,
     "description": "Traditional green tea with saffron, almonds, and spices."},
    
    {"image": "/static/tea (8).jpg", "product_name": "Sikkim Temi Tea", "price": 27,
     "description": "Delicate and flavorful tea from Sikkim’s famous Temi estate."},
    
    {"image": "/static/tea (9).jpg", "product_name": "Mysore Herbal Tea", "price": 20,
     "description": "Aromatic herbal blend with natural healing properties."},
    
    {"image": "/static/tea (10).jpg", "product_name": "Coorg Green Tea", "price": 24,
     "description": "Fresh green tea with a slightly grassy and smooth flavor."},
    
    {"image": "/static/tea (11).jpg", "product_name": "Rajasthan Spiced Tea", "price": 32,
     "description": "Bold black tea infused with traditional Rajasthani spices."},
    
    {"image": "/static/tea (12).jpg", "product_name": "Hyderabad Irani Chai", "price": 30,
     "description": "Strong, creamy tea with a hint of cardamom, served in small cups."},
    
    {"image": "/static/tea (13).jpg", "product_name": "Nagaland Organic Tea", "price": 26,
     "description": "Organic tea grown in the clean, green hills of Nagaland."},
    
    {"image": "/static/tea (14).jpg", "product_name": "Bengal Lemon Tea", "price": 15,
     "description": "Refreshing black tea with tangy lemon and a hint of sugar."},


    {"image": "/static/tea (9).jpg", "product_name": "Goa Masala Chai", "price": 29,
     "description": "Sweet and spicy chai infused with local Goan spices."},
    
    {"image": "/static/tea (8).jpg", "product_name": "Kerala Ginger Tea", "price": 21,
     "description": "Strong black tea with a zesty kick of ginger."},
    
    {"image": "/static/tea (6).jpg", "product_name": "Punjab Chai", "price": 24,
     "description": "Rich, robust tea with a hint of cardamom, popular in Punjab."},
    
    {"image": "/static/tea (3).jpg", "product_name": "Mumbai Cutting Chai", "price": 19,
     "description": "Classic street-style chai, small cup, strong flavor."},
    
    {"image": "/static/tea (4).jpg", "product_name": "Tamil Nadu Filter Tea", "price": 23,
     "description": "Creamy South Indian filter coffee-style tea but with strong leaves."},
    
    {"image": "/static/tea (10).jpg", "product_name": "Himachal Green Tea", "price": 28,
     "description": "Fresh mountain tea with subtle green notes and low bitterness."},
    
    {"image": "/static/tea (2).jpg", "product_name": "Bihar Sattu Tea", "price": 18,
     "description": "Unique tea with roasted gram powder, earthy and hearty flavor."},
    
    {"image": "/static/tea (1).jpg", "product_name": "Nagpur Orange Tea", "price": 26,
     "description": "Black tea with a refreshing citrus twist from Nagpur oranges."},
    {"image": "/static/tea.jpg", "product_name": "Bihar Sattu Tea", "price": 18,
     "description": "Unique tea with roasted gram powder, earthy and hearty flavor."},



]

def routing(app):

    @app.route('/')
    def get_products():
        page=int(request.args.get("page"))
        per_page=8
        start_item=(page-1)*8
        end_item=start_item+per_page

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