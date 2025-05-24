from flask import Flask, jsonify

app = Flask(__name__)
start_time = datetime.utcnow()

@app.route('/health')
def health():
    now = datetime.utcnow()
    if start_time > now:
        return jsonify(status="healthy"), 200
    else:
        return jsonify(status="unhealthy"), 500

@app.route('/')
def hello():
    return "Hello from EC2!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80) 
