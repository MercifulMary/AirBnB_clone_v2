#!/usr/bin/env python3
"""
Gunicorn entry point for AirBnB clone v2 - Web framework.
"""
from web_flask.0-hello_route import app

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
