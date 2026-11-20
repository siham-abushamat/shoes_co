from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def entry():
    return render_template('entry.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/footwear')
def footwear():
    sneakers = [
        {"name": "Nike Air Max", "price": "$150", "image": "images/airmax/nike_airmax.jpg"},
        {"name": "Adidas Forum", "price": "$120", "image": "images/adidas/adidas_forum.jpg"},
        {"name": "Puma RS-X", "price": "$110", "image": "images/puma/puma_rsx.jpg"},
        {"name": "New Balance 550", "price": "$130", "image": "images/550/nb_550.jpg"},
    ]
    return render_template('footwear.html', sneakers=sneakers)

if __name__ == '__main__':
    app.run(debug=True)

    