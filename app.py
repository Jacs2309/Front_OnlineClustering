from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/config")
def get_config():
    """Endpoint que devuelve la URL del backend desde variables de entorno"""
    backend_url = os.environ.get("BACKEND_URL", "http://localhost:5001")
    return {"api_base_url": backend_url}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_ENV") == "development"
    app.run(host="0.0.0.0", port=port, debug=debug)