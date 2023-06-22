from flask import Flask  
app = Flask(__name__)   
@app.route('/')         
def hola_mundo():
    return 'Hola Mundo!'  

@app.route("/dojo")
def mensaje_dojo():
    return "¡Dojo!"  
    
@app.route('/hola/<name>')
def hola(name):
    if name.isalpha():
        return f"¡Hola, {name}!" 
    else:
        return "Proporcione un String"

@app.route('/repetir/<word>/<num>')
def repetir(word, num):
    return ' '.join([word] * int(num))

if __name__=="__main__":   
    app.run(debug=True)  
    
