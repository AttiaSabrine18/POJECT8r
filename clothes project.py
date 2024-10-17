from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  

@app.route('/cart')  
def cart():
    return render_template('cart.html')  

@app.route('/p2')  
def p2():
    return render_template('p2.html')  

@app.route('/p3')  
def p3():
    return render_template('p3.html')

@app.route('/p4')  
def p4():
    return render_template('p4.html')  

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9080)  # 'host=0.0.0.0' permet l'accès sur le réseau local
