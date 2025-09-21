# IELTS Dictation App

A web-based dictation practice tool built with Flask to help users, especially IELTS candidates, improve their spelling and listening skills. Users can select from multiple word categories, listen to words via speech synthesis, and practice spelling with instant feedback, hints, and scoring. Word categories are stored in simple `.txt` files for easy customization.

## Live Demo

Try the app now at [https://ielts-dictation-app.onrender.com/](https://ielts-dictation-app.onrender.com/)! No setup required—just open the link in a modern browser and start practicing.

## Features

- **Category Selection**: Choose from various word categories (e.g., "Academic," "Environment," "Technology") stored as `.txt` files.
- **Speech Synthesis**: Words are read aloud using the Web Speech API for realistic dictation practice.
- **Instant Feedback**: Get immediate results on whether your spelling is correct.
- **Hints**: Stuck? Request a hint to help with tricky words.
- **Scoring System**: Track your progress with a score for each session.
- **Customizable Word Lists**: Add or modify `.txt` files to create new categories or update existing ones.

## Prerequisites

- Python 3.8 or higher
- Flask (`pip install flask`)
- A modern web browser (for Web Speech API support)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/parsakhattat/IELTS-dictation-app.git
   cd IELTS-dictation-app
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Add word lists**:
   - Place `.txt` files containing words (one per line) in the `data/` folder.
   - Example: `data/academic.txt`, `data/environment.txt`.

5. **Run the application**:
   ```bash
   flask run
   ```
   - The app will be available at `http://localhost:5000`.

## Usage

1. Open the app in your browser (either locally or via the [live demo](https://ielts-dictation-app.onrender.com/)).
2. Select a word category from the dropdown menu.
3. Click "Start" to begin the dictation.
4. Listen to the word, type your answer, and submit to check if it's correct.
5. Use the "Hint" button if needed, and track your score as you go.
6. Switch categories or refresh to start a new session.

## Project Structure

```
IELTS-dictation-app/
├── app.py                 # Main Flask application
├── data/                  # Folder for .txt word lists
├── static/                # CSS, JavaScript, and other static files
├── templates/             # HTML templates for the frontend
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -m "Add your feature"`).
4. Push to your branch (`git push origin feature/your-feature`).
5. Open a pull request with a clear description of your changes.

Please ensure your code follows the project's coding style and includes relevant tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, reach out to [parsakhattat](https://github.com/parsakhattat) or open an issue on this repository.

---

Happy spelling, and good luck with your IELTS prep!