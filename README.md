# Recycling Meltspinning Materials Calculator

A Python-based GUI tool for calculating material balances in **recycling meltspinning processes**.  
This calculator helps engineers to calculate the combination of oil, polymers, flakes, chips, masterbatch, waste, and the bunker mass during meltspinning with recycling inputs for recycled fibers plants.
This tool mostly help plant engineers to calculate material percentage for ERP systems based on each 100 kg product for input materials.

---

## ✨ Features
- **Interactive GUI** built with `tkinter`
- **Entry + Result columns** for each material:
  - Oil, PSU, SPC, SKPC, Flake, Chips, Master batch, Waste, Bunker mass with respective units
- **Master batch mode toggle**:
  - Radio buttons for **kg** or **%**
- **Flake mix strategy**:
  - Two flake rows:
    - Flake 1 (always active)
    - Flake 2 (enabled when “Mix” checkbox is selected)
  - Mix percentage (1–99%) splits flake distribution into two parts
- **Calculate & Reset buttons** for quick recalculation

---

## 🧮 Calculation Logic
- Oil percent = fixed input
- Other percents = `component * (100 + waste) / bunker`
- Chips vs Flake:
  - If total < 300 → Chips calculated, Flake is remainder, the fiber is flake based
  - If total ≥ 300 → Flake calculated, Chips is remainder, the fiber is polyester chips based
- Flake mix logic:

```python
  if mix_var == 1 and 1 <= mix_val <= 99:
      flake_percent1 = flake_percent * mix_val / 100
      flake_percent2 = flake_percent * (100 - mix_val) / 100
  else:
      flake_percent1 = flake_percent
      flake_percent2 = 0
```

---

# 🚀 Installation
Clone the repository and run the script:

```bash
git clone https://github.com/Javanmardi/RecycleMeltspinningMaterialsCalculator.git
cd RecycleMeltspinningMaterialsCalculator
python RMCalculator.py
```

---

# Requirements:
- Python 3.8+ (Anaconda preferred)
- Standard library (tkinter, webbrowser)

---

# 📖 Usage
1. Enter values for each material in the left column.
2. Select kg or % for Master batch.
3. Optionally enable Mix for Flake and enter a percentage.
4. Click Calculate to compute percentages.
5. Click Reset to clear all fields.

---

# 📜 License
This project is licensed under the MIT License.
See the LICENSE file for details.

---

# 👤 Author
Created by Behrouz Javanmardi

📧 behrouz@javanmardi.org

🔗 [GitHub Repository](https://github.com/Javanmardi/RecycleMeltspinningMaterialsCalculator)

---

# 🛠️ Future Improvements
- Add status bar for calculation feedback
- Export results to CSV/Excel
- Add error handling for invalid inputs
- Extend to other polymer recycling scenarios
