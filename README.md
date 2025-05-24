# Thermodynamics Modeling Lab

This repository documents my learning journey and experimental modeling in thermodynamics using Python.

## Overview
This repo includes toy models built while exploring thermodynamic systems from first principles, inspired by the MIT OCW Thermodynamics and Kinetics course (5.60). These are not polished simulations but stepping stones in understanding core concepts through code.

## Included Models

### `gasmixer.py`
- **Purpose:** A toy model for mixing two gases in a container.
- **Concepts:** Ideal gas law, energy conservation, pressure-volume dynamics.
- **Tools Used:** Python, matplotlib for visualizing mixing trajectory.
- **Learning Goal:** Understand equilibrium conditions and apply energy balance.

### `engine.py`
- **Purpose:** Simulate a toy reversible engine cycle with volume ramp.
- **Concepts:** Volume change dynamics from pressure and temperature gradients.
- **Status:** Ongoing—this is more of a sketch to test differential volume computation logic.
- **Learning Goal:** Build intuition for dynamic systems in thermodynamics.

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
