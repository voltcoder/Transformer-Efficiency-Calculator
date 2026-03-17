# Transformer-Efficiency-Calculator
Python-based Transformer Efficiency Calculator that computes efficiency at different load conditions considering copper and iron losses.

---

# Transformer Efficiency Calculator

A Python-based project to calculate transformer efficiency under different load conditions.

This project considers:

* Copper Loss (Variable with load)
* Iron Loss (Constant)
* Load Percentage

It demonstrates practical transformer efficiency concepts used in power systems and electrical engineering.

---

## Formula Used

Efficiency (%) = Output Power / (Output Power + Copper Loss + Iron Loss) × 100

Where:

* Copper Loss ∝ (Load)²
* Iron Loss = Constant

---

## Maximum Efficiency Condition

A transformer achieves maximum efficiency when:

Copper Loss = Iron Loss

The program also checks and indicates when this condition is satisfied.

---

## Features

* Calculates efficiency at any load percentage
* Models copper loss using square-law relationship
* Considers constant iron loss
* Detects maximum efficiency condition
* Simple command-line interface (CLI) implementation

---

## How to Run

1. Install Python
2. Download the file `transformer_efficiency.py`
3. Run the script:

   ```bash
   python transformer_efficiency.py
   ```
4. Enter:

   * Rated Power
   * Load Percentage
   * Full Load Copper Loss
   * Iron Loss

---

## Sample Input

* Rated Power = 100 kW
* Load Percentage = 80%
* Full Load Copper Loss = 4 kW
* Iron Loss = 2 kW

---

## Sample Output

Efficiency at 80% load = 96.15%

---

## Note

All inputs should be provided in the same unit (kW recommended).

---

## Learning Outcome

This project helps in understanding:

* Transformer losses
* Efficiency calculation
* Effect of load variation
* Practical implementation using Python

---

## Future Improvements

* Plot efficiency vs load curve
* Add GUI interface
* MATLAB/Simulink integration
* Real-time transformer monitoring system

---

## Summary

This project calculates transformer efficiency using:

Efficiency = Output Power / (Output Power + Copper Loss + Iron Loss) × 100

### Inputs:

* Rated Power (kW)
* Load Percentage (%)
* Copper Loss (kW)
* Iron Loss (kW)

### Output:

* Transformer Efficiency (%)

---


Author: Swati Sharma(@voltcoder)
Electrical Engineering Graduate

