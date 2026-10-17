from flask import Flask, render_template, request
app = Flask(__name__, template_folder='.')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/job', methods=['POST'])
def process_data():
    user_input = request.form.get('name')
    proccessed_data = user_input.upper()
    return f"the data in capital letters is: {proccessed_data}"

if __name__ == '__main__':
    app.run(debug=True)
