# 📊 Numerical Analysis & Advanced Programming Projects

This repository contains **three complete projects** from the Numerical Analysis and Advanced Programming course, covering interpolation, numerical integration, Excel data analysis, and professional documentation using **LaTeX** and **Word**.

---

## 📚 Project List

### 📁 Project 1: Lagrange & Cubic Spline Interpolation
**Objective:** Calculate and compare two interpolation methods on given data points.

- **Data Points:** (2,3), (3,5), (4,8), (5,5), (6,2)
- **Methods:**
  - Lagrange Interpolation (using `sympy`)
  - Natural Cubic Spline Interpolation (using `scipy.interpolate.CubicSpline`)
- **Outputs:**
  - Exact Lagrange polynomial (Decimal form)
  - Spline functions for each interval
  - Comparative visualization of both methods

**Files:** `project1_interpolation.py`

---

### 📁 Project 2: Excel Data Analysis & Statistical Charts
**Objective:** Automatically read Excel data and generate analytical visualizations.

- **Data:** Execution time of 3 algorithms for data sizes 100KB to 700KB
- **Charts:**
  - 📊 Bar Chart
  - 📈 Line Chart
  - 📦 Box Plot
- **Statistical Calculations:** Average execution time of Algorithm 2 for 100KB to 600KB data
- **Special Feature:** Charts update automatically when new data (700KB) is added without modifying the code

**Files:** `project2_excel_analysis.py`, `project2_data.xlsx`

---

### 📁 Project 3: Numerical Integration Methods
**Objective:** Numerically compute the integral of \( f(x) = e^{x^2} \) over [0, 1].

- **Methods:**
  - 📐 Simpson's Rule
  - 📐 Trapezoidal Rule
  - 📐 Gaussian Quadrature (using `quad`)
- **Output:** Accuracy comparison of three methods with estimated error

**Files:** `project3_numerical_integration.py`

---

## 🛠️ Prerequisites & Installation

Install the required libraries:

```bash
pip install numpy pandas matplotlib seaborn scipy sympy openpyxl
