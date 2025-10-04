# TeaTok – Tea Ordering Backend with Flask 🍵

**TeaTok** is a lightweight Flask backend for a tea ordering platform.  
It demonstrates **paginated product listing, search functionality, and a dummy order confirmation feature**.  
Perfect for learning **Flask routes, query parameters, JSON responses, and basic frontend integration**.

---

## Features ✨

- Paginated product listing (8 products per page)
- Search teas by name using query parameters
- Dummy order confirmation endpoint
- 25+ Indian tea varieties included
- Works with TailwindCSS frontend

---

## Backend Routes 🔗

| Route        | Method | Description |
|--------------|--------|-------------|
| `/`          | GET    | Returns paginated products (`?page=1`) |
| `/html`      | GET    | Renders the frontend HTML page |
| `/click`     | GET    | Dummy order endpoint; returns confirmation message |
| `/search`    | GET    | Search products by name (`?products_name=Ooty Tea`) |

---

Installation & Setup

---
# Clone the repository
git clone https://github.com/yourusername/teatok.git
cd teatok

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv/Scripts/activate
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the backend
python app.py

# Open in browser
http://127.0.0.1:5000/html

## Screenshots

### Homepage
![Homepage](screenshots/homepage.png)

### Search Results
![Search Results](screenshots/search.png)

### Order Confirmation
![Order Confirmation](screenshots/order.png)

---

## Technologies

- **Backend:** Python, Flask  
- **Database:** SQLite via SQLAlchemy
- **Frontend:** TailwindCSS (optional integrated HTML)

---





