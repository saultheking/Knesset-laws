from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def scrape_knesset():
    try:
        # מריץ את הסקרייפר ושומר את הפלט
        result = subprocess.run(['python', 'knesset_scraper.py'], capture_output=True, text=True)
        return jsonify({"status": "success", "message": result.stdout}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
