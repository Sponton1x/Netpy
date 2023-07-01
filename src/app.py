from flask import Flask, request

app = Flask(__name__)

stored_data = None

@app.route("/", methods=['POST'])
def process_data():
    global stored_data
    data = request.get_json()
    stored_data = data  # Przechowaj otrzymane dane
    return 'Success'

@app.route("/", methods=['GET'])
def display_data():
    global stored_data
    if stored_data is not None:
        return str(stored_data)  # Wyświetl przechowywane dane
    else:
        return 'No data available'

if __name__ == "__main__":
    app.run()
