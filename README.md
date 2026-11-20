# SWISH & CO – Sneaker Store Website

A front-end prototype for an online sneaker and streetwear store, built with Python's Flask web framework, HTML and CSS.

## Pages

| Page | URL | What it shows |
|---|---|---|
| Entry | `/` | Full-screen background video with the SWISH & CO logo and an animated **ENTER** button |
| Shop | `/shop` | Navigation bar and a grid of featured collections: Nike SB, Adidas Tennis and Carhartt |
| Footwear | `/footwear` | Product cards for four sneakers with prices and an **Add to Cart** button: Nike Air Max, Adidas Forum, Puma RS-X and New Balance 550 |

## How it works

- **Flask routes:** `app.py` defines one route per page and renders an HTML template for each.
- **Product data:** the sneakers are a list in Python that is passed to `footwear.html`. A Jinja2 loop turns each item into a product card, so a product is added by adding one line in `app.py`.
- **Layout and effects:** the layout uses CSS Grid, so the product cards rearrange to fit the screen width. Collections and product cards zoom slightly on hover.
- **Background video:** the video on the entry page fills the screen at any window size.

## Status

This is a front-end prototype. The cart and the New Arrivals, Apparel and Brands pages are not built yet. Their links are placeholders, and **Add to Cart** doesn't save anything.

## Built with

- Python 3
- Flask
- Jinja2 templates
- HTML
- CSS

## How to run

1. Install Python 3 from [python.org](https://www.python.org/downloads/).
2. Install Flask:
   ```
   pip install flask
   ```
3. In the project folder, run:
   ```
   python app.py
   ```
   On a Mac, use `python3 app.py`.
4. Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Project structure

```
shoes_co/
├── app.py                  # Flask app: routes and product list
├── templates/
│   ├── entry.html          # Landing page with background video
│   ├── shop.html           # Featured collections
│   └── footwear.html       # Sneaker product cards
└── static/
    ├── css/styles.css      # All styling
    ├── images/             # Product and collection images
    └── videos/video.mp4    # Entry page background video
```
