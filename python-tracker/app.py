from flask import Flask, request, jsonify, render_template
import json
import os
import threading
import time

app = Flask(__name__)
DATA_FILE = 'data.json'

# Fungsi membaca data
def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Fungsi menyimpan data
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/expenses', methods=['GET', 'POST'])
def handle_expenses():
    if request.method == 'POST':
        data = request.json
        save_data(data)
        return jsonify({"message": "Data tersimpan!"})
    
    # Jika GET, kembalikan data
    return jsonify(load_data())

@app.route('/api/shutdown', methods=['POST'])
def shutdown():
    # Fungsi untuk mematikan terminal setelah 1 detik
    def kill_server():
        time.sleep(1)
        os._exit(0)
    
    threading.Thread(target=kill_server).start()
    return jsonify({"message": "Server dimatikan"})

if __name__ == '__main__':
    # Jalankan di localhost port 3000
    app.run(port=3000)