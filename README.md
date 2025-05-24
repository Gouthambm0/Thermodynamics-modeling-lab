# Thermodynamic Simulation: Ideal Gas Mixer

### 🎯 The Goal
My transition from medicine to technology is driven by a need to understand complex systems from first principles. I built this model to move beyond static textbook equations and develop an intuitive, hands-on understanding of thermodynamics. My primary aim was to visualize how core properties like entropy and internal energy behave dynamically as the parameters of an ideal gas mixture change.

### 📜 Project Description
This repository contains `gasmixer.py`, a Python script that models a system of two ideal gases separated by a partition. The model allows for user-defined initial conditions (volume, pressure, temperature) for each gas and then simulates the final, equilibrium state of the system after the partition is removed. It is specifically designed to clarify the behavior of partial derivatives for entropy and energy.


### `engine.py`
- **Purpose:** Simulate a toy reversible engine cycle with volume ramp.
- **Concepts:** Volume change dynamics from pressure and temperature gradients.
- **Status:** Ongoing—this is more of a sketch to test differential volume computation logic.
- **Learning Goal:** Build intuition for dynamic systems in thermodynamics.

### 💡 Key Concepts Solidified
* **The Second Law of Thermodynamics:** Gaining a tangible feel for how entropy changes in an irreversible process by observing the system's evolution.
* **Partial Derivatives in Physics:** Clearly visualizing how changing one system variable (like volume) affects the overall energy and entropy.
* **Scientific Modeling in Python:** Translating a physical system and its governing laws (the Ideal Gas Law) into a functional, predictive computational model.
* **Object-Oriented Thinking:** Structuring the code to represent distinct physical components and their interactions.

## Why This Exists
This is part of a broader systems-thinking effort—building intuition by modeling reality. Instead of just memorizing equations, this repo is about translating thermodynamic principles into working Python code.

## How to Run
These are single-file scripts. Clone and run with Python 3.x:
```bash
python gasmixer.py
python engine.py
```

## Future Additions
- Model Carnot cycle.
- Add logging for entropy and energy flow.
- Create visual demos with interactive sliders (via Streamlit or similar).

---

If you have feedback, or if you're building physical models too, feel free to fork or reach out. This is part of a longer journey into understanding complex systems by modeling their simplest forms.
