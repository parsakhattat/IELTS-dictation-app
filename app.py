from flask import Flask, render_template, jsonify, request
import os
import random

app = Flask(__name__)


# Get list of category files (txt files in project root)
def get_categories():
    return [f for f in os.listdir('.') if f.endswith('.txt')]


# Load words from a category file
def load_words(category_file):
    if not os.path.exists(category_file):
        return []
    with open(category_file, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]


@app.route('/')
def index():
    categories = get_categories()
    return render_template('index.html', categories=categories)


@app.route('/get_word', methods=['POST'])
def get_word():
    category = request.json.get('category', '')
    words = load_words(category)
    if not words:
        return jsonify({'error': 'No words found for this category', 'total_words': 0})
    word = random.choice(words)
    return jsonify({'word': word, 'total_words': len(words)})


@app.route('/category_info', methods=['POST'])
def category_info():
    """Return just the total number of words for a category (no word revealed)."""
    category = request.json.get('category', '')
    words = load_words(category)
    return jsonify({'total_words': len(words)})


@app.route('/check_answer', methods=['POST'])
def check_answer():
    user_answer = request.json.get('answer', '').strip().lower()
    correct_word = request.json.get('correct_word', '').strip().lower()
    attempt = int(request.json.get('attempt', 1))
    max_attempts = 3  # configurable
    is_correct = user_answer == correct_word
    attempts_remaining = max_attempts - attempt

    response = {
        'is_correct': is_correct,
        'attempts_remaining': attempts_remaining,
        'max_attempts': max_attempts
    }

    # reveal correct word only when correct or no attempts left
    if is_correct or attempts_remaining <= 0:
        response['correct_word'] = correct_word

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
