# 🎓 Placement Prediction System

An AI-powered web application that predicts student placement outcomes based on academic performance (CGPA) and intelligence quotient (IQ) scores using machine learning.

## ✨ Features

- **Modern Glass-morphism UI** - Beautiful, responsive interface with animated gradients
- **Real-time Predictions** - Instant placement prediction using trained ML model
- **User-Friendly Input** - Intuitive form with input validation
- **Color-Coded Results** - Visual feedback with success/failure indicators
- **Mobile Responsive** - Optimized for desktop and mobile devices
- **Smooth Animations** - Enhanced UX with fade-in and slide-up effects

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3 (Glass-morphism Design)
- **ML Model**: Scikit-learn (Pre-trained)
- **Data Processing**: NumPy, Pandas
- **Deployment Ready**: Python 3.14+

## 📋 Requirements

- Python 3.8+
- Flask 3.1.3
- Scikit-learn 1.8.0
- NumPy 2.4.6
- Pandas 3.0.3
- Joblib 1.5.3

## 🚀 Installation

### 1. Clone or Download the Project
```bash
cd placement_prediction
```

### 2. Create Virtual Environment
```bash
python -m venv myenv
```

### 3. Activate Virtual Environment

**On Windows:**
```bash
myenv\Scripts\activate
```

**On macOS/Linux:**
```bash
source myenv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

## 📖 Usage

### Running the Application

1. Ensure your virtual environment is activated
2. Run the Flask app:
```bash
python app.py
```

3. Open your browser and navigate to:
```
http://localhost:5000
```

4. Enter your **CGPA** (0-4.0) and **IQ** score to get a prediction

### How It Works

The system uses a pre-trained machine learning model (`model.pkl`) that has been trained on historical placement data. It takes two inputs:

- **CGPA**: Cumulative Grade Point Average (0.0 - 4.0)
- **IQ**: Intelligence Quotient score (typically 0-200)

Based on these inputs, the model predicts whether a student will be placed (✅) or not placed (❌).

## 📁 Project Structure

```
placement_prediction/
├── app.py                 # Main Flask application
├── model.pkl             # Pre-trained ML model
├── requirements.txt      # Python dependencies
├── README.md             # This file
├── .gitignore            # Git ignore rules
├── myenv/                # Virtual environment
└── templates/
    └── index.html        # Web interface
```

## 🔧 Configuration

The application runs in debug mode by default. For production, modify `app.py`:

```python
if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)
```

## 🎨 UI Features

- **Animated Gradient Background** - Smooth color transitions
- **Glass Card Design** - Modern frosted glass effect
- **Responsive Forms** - Mobile-friendly input fields
- **Real-time Validation** - Input constraints (CGPA: 0-4, IQ: positive)
- **Instant Feedback** - Immediate prediction results with visual indicators

## 🐛 Troubleshooting

### Model File Not Found
Ensure `model.pkl` is in the project root directory.

### Port Already in Use
Change the port in `app.py`:
```python
app.run(debug=True, port=8000)
```

### Dependencies Installation Failed
Try upgrading pip:
```bash
pip install --upgrade pip
```

## 📝 Notes

- The ML model is pre-trained and not updated during runtime
- Input validation ensures CGPA is between 0 and 4
- All predictions are performed locally (no external API calls)

## 📄 License

This project is open source and available for educational purposes.

## 👨‍💻 Author

Created as an ML demonstration project.

---

**Enjoy predicting placements! 🎯**
