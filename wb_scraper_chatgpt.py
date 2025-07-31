import requests
from bs4 import BeautifulSoup

# Target URL
url = "https://books.toscrape.com/"

# Send request to the website
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find all book containers
books = soup.find_all("article", class_="product_pod")

# Loop through each book and extract info
for book in books:
    # Title
    title = book.h3.a["title"]
    
    # Price
    price = book.find("p", class_="price_color").text.strip()
    
    # Rating (stored in class name like "star-rating Three")
    rating_class = book.find("p", class_="star-rating")["class"]
    rating = rating_class[1]  # It's like ["star-rating", "Three"]
    
    print(f"📖 Title: {title}")
    print(f"⭐ Rating: {rating}")
    print(f"💰 Price: {price}")
    print("-" * 40)
