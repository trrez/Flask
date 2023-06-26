from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(f"Cobrando a {request.form['first_name']} {request.form['last_name']} por {int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])} frutas")
    return render_template("checkout.html")

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    