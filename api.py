from flask import Flask, jsonify
from num2words import num2words
import yaml

app = Flask(__name__)

def load_number_from_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            config = yaml.safe_load(file)
            return config.get('number')
    except Exception as e:
        print(f"Error reading YAML file: {e}")
        return None

@app.route('/data', methods=['GET'])
def get_data():
    number = load_number_from_yaml('config.yaml')  # Specify your YAML file path here
    if number is None:
        return jsonify({'error': 'No valid number provided in YAML file'}), 400
    try:
        number = int(number)
        words = num2words(number)
        return jsonify({'value': words})
    except ValueError:
        return jsonify({'error': 'Invalid number provided in YAML file'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
