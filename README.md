# Flask Application

A basic Flask application with Docker support.

## Setup

1. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### Local Development
```bash
python app.py
```

### Using Docker
1. Build the Docker image:
```bash
docker build -t flask-app .
```

2. Run the container:
```bash
docker run -p 5000:5000 flask-app
```

The application will be available at `http://localhost:5000`
