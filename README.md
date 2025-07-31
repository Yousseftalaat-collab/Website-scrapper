<h1 align="center">📚 Book Rating Scraper - Python (Web Scraping)</h1>

<p align="center">
  A simple Python script that scrapes book titles and star ratings from <a href="https://books.toscrape.com" target="_blank">books.toscrape.com</a> using BeautifulSoup and requests.  
  Perfect for beginners learning web scraping!
</p>

<p align="center">
  <img src="https://media.giphy.com/media/3o7TKxOH8ZC0dskjCM/giphy.gif" width="300" alt="Scraping gif"/>
</p>

---
<ol>
<h2>## 🧠 How It Works </h2>

 <li>ends an HTTP GET request to `https://books.toscrape.com/`</li>
   <li> Parses the HTML using `BeautifulSoup`</li>
 <li>
Loops through each book element:
   - Extracts the book title
   - Extracts the star rating (e.g., Three, Five)</li>
<li>
 Prints the result in the format:  
   `Book titled: The Book Name has a rating of: Four stars`</li>

---
</ol>
<h3>## ▶️ How to Run</h3>
<p>### 💻 Requirements

- Python 3
- `requests` and `beautifulsoup4` modules

### 📦 Install Dependencies
```bash
pip install requests beautifulsoup4
📥 Run the Script

python book_scraper.py
</p>

<h3>🔍 Example Output</h3>
<p>
Book titled: A Light in the Attic has a rating of: Three stars
Book titled: Tipping the Velvet has a rating of: One stars
Book titled: Soumission has a rating of: One stars
...
</p>

<ol>🛠 Technologies Used
<li>🐍 Python 3</li>

<li>🌐 requests — for sending HTTP requests</li>
</ol>

<h3>👨‍💻 Author</h3>
<p> Made with by Youssef Talaat</p>
