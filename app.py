from flask import Flask, render_template

app = Flask(__name__)

# Global product data
products = {
    "paver-blocks": {
        "Square Block": ["Red", "Grey", "Yellow"],
        "Zigzag Block": ["Grey", "Brown", "Red"]
    },

    "fly-ash-bricks": {
        "Standard Size": []
    },

    "aac-blocks": {
        "4 inch": [],
        "6 inch": [],
        "8 inch": [],
        "9 inch": []
    }
}

category_display_name = {
    "paver-blocks": "Paver Blocks",
    "fly-ash-bricks": "Fly Ash Bricks",
    "aac-blocks": "AAC Blocks"
}

@app.route('/')
def home():
    return render_template('home.html', categories=category_display_name)


@app.route('/category/<category_name>')
def show_category(category_name):
    if category_name not in products:
        return "Category Not Found", 404
    varieties = list(products[category_name].keys())
    display_name = category_display_name[category_name]

    return render_template('category.html', category=display_name, varieties=varieties)


@app.route('/products/<category_name>/<variety_name>')
def variety_detail(category_name, variety_name):
    if category_name not in products:
        return "Category Not Found", 404
    
    category_products = products[category_name]

    if variety_name not in category_products:
        return "Variety Not Found", 404

    display_name = category_display_name[category_name]

    colors_or_sizes = category_products[variety_name]  # Could be colors (list) or empty

    details = {
        "description": f"{variety_name} is a type of {display_name.lower()}",
        "available_colors": colors_or_sizes if category_name == "paver-blocks" else [],
        "available_sizes": colors_or_sizes if category_name == "aac-blocks" else []
    }

    return render_template('variety_detail.html',
                           category=display_name,
                           variety=variety_name,
                           details=details)




if __name__ == '__main__':
    app.run(debug=True, port=8000)