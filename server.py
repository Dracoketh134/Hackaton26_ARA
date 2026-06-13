#!/usr/bin/env python3
"""
Simple Flask server to save game scores to JSON file.
Run: python server.py
Then open: http://127.0.0.1:5000
"""

import json
import os
from datetime import datetime
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

SCORES_FILE = 'scores.json'

def load_scores():
    """Load scores from JSON file."""
    if not os.path.exists(SCORES_FILE):
        return {
            "meta": {
                "version": "1.0",
                "title": "Catalan Picture Quiz - Scores",
                "description": "Game scores saved every 10 seconds",
                "created": datetime.now().isoformat()
            },
            "scores": []
        }
    with open(SCORES_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_scores(data):
    """Save scores to JSON file."""
    with open(SCORES_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@app.route('/')
def index():
    """Serve the main HTML file."""
    return send_from_directory('.', 'Javasc.html')

@app.route('/vocab.json')
def vocab():
    """Serve the vocabulary JSON file."""
    return send_from_directory('.', 'vocab.json')

@app.route('/scores.json')
def scores_file():
    """Serve the scores JSON file."""
    data = load_scores()
    return jsonify(data)

@app.route('/save-score', methods=['POST'])
def save_score():
    """Save a score entry."""
    try:
        data = request.get_json()
        scores_data = load_scores()
        
        if not isinstance(scores_data.get('scores'), list):
            scores_data['scores'] = []
        
        entry = {
            "timestamp": data.get('timestamp', datetime.now().isoformat()),
            "correct": data.get('correct', 0),
            "total": data.get('total', 0),
            "percentage": data.get('percentage', 0)
        }
        scores_data['scores'].append(entry)
        scores_data['meta']['updated'] = datetime.now().isoformat()
        
        save_scores(scores_data)
        return jsonify({"status": "ok", "entry": entry}), 201
    except Exception as err:
        return jsonify({"status": "error", "message": str(err)}), 400

@app.route('/<path:filename>')
def serve_static(filename):
    """Serve static files (images, etc)."""
    try:
        return send_from_directory('.', filename)
    except Exception:
        return jsonify({"error": "File not found"}), 404

if __name__ == '__main__':
    print("Starting Catalan Quiz Server on http://127.0.0.1:5000")
    print("Press Ctrl+C to stop")
    print()
    print("Make sure you have Flask installed:")
    print("  pip install flask flask-cors")
    print()
    app.run(debug=False, host='127.0.0.1', port=5000)
