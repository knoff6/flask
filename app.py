from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        email = request.form['email']
        phone_number = request.form['phoneNumber']
        password = request.form['password']
        confirm_password = request.form['confirmPassword']
        return render_template('submit.html', first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, password=password, confirm_password=confirm_password)

if __name__ == '__main__':
    app.run(debug=True)
