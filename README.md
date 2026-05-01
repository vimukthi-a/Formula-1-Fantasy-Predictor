# F1 Fantasy Predictor

An F1 race and fantasy prediction project using Python, FastF1, and machine learning.

## Goal
Predict race outcomes and provide F1 Fantasy-style driver picks based on historical and race-week data.

---

## 🧠 Methodology

### Data
- Historical race data collected using FastF1
- Seasons used:
  - **2023** → training
  - **2024** → testing (real-world simulation)

---

### Feature Engineering

Key features explored:

- **GridPosition** — starting position
- **RollingAvg3** — average finishing position over last 3 races
- **PrevPosition** — previous race result

---

### Advanced Features

To reduce over-reliance on a single feature, additional engineered features were created:

- **GridVsForm**  
  Compares a driver's recent form with their starting position

- **FormTrend**  
  Captures improvement or decline in recent performance

---

### Key Insight

Initial models showed that:

- `RollingAvg3` dominated predictions (**~0.78 feature importance**)

To address this:
- RollingAvg3 was used to derive more balanced features instead of being used directly

---

## 📊 Results

| Model Setup | MAE |
|------------|-----|
| With RollingAvg3 | **1.45** |
| Without RollingAvg3 | 1.74 |
| + GridVsForm | 1.61 |
| + FormTrend | **1.49** |

---

## 🔍 Learnings

- Feature dominance can negatively impact model balance
- Feature engineering is more effective than simply adding more features
- Proper evaluation (2023 → 2024 split) is critical to avoid data leakage
- Debugging and data pipeline correctness are essential for reliable results

---

## 🚀 Next Steps

- Improve feature set (driver consistency, track-specific performance)
- Build prediction function for race-week forecasting
- Develop a web dashboard for interactive predictions and F1 Fantasy picks

---

## ⚙️ Tech Stack

- Python
- FastF1
- Pandas / NumPy
- Scikit-learn

---

## 📌 Status

Active development — core prediction pipeline implemented, moving toward real-time prediction and deployment.