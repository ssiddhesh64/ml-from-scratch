# Machine Learning From Scratch (ml-from-scratch)

A structured, clean, and educational Python package implementing fundamental machine learning algorithms, mathematical optimizations, statistics, and neural network components from scratch using only standard libraries and basic numpy vectorization.

This repository is designed with clean software engineering principles, modular organization, and testing best practices, serving as a robust reference for learning the mechanics behind popular ML algorithms.

---

## 📂 Repository Structure

The project is organized into self-contained packages covering the entire ML pipeline:

```text
ml-from-scratch/
├── linear_algebra/          # Vectors, matrices, norms, and similarity measures
├── statistics/              # Central tendency, dispersion, and relationships
├── optimization/            # Numerical optimization algorithms (e.g., gradient descent)
├── machine_learning/        # Standard supervised and unsupervised ML models
├── neural_networks/         # Basic deep learning components and backpropagation
└── tests/                   # Test suite matching package structure for verification
```

### Module Breakdown

- **`linear_algebra/`**
  - `dot_product.py`: Custom dot product calculation.
  - `norms.py`: L1, L2, and other vector/matrix norms.
  - `cosine_similarity.py`: Angular similarity metric.
  - `matrix_multiplication.py`: Classical and optimized matrix multiplication algorithms.
- **`statistics/`**
  - `mean.py`: Arithmetic, geometric, and harmonic means.
  - `variance.py`: Sample and population variance.
  - `covariance.py`: Correlation and covariance metrics.
- **`optimization/`**
  - `gradient_descent.py`: Batch, stochastic, and mini-batch gradient descent optimizer stubs.
- **`machine_learning/`**
  - `linear_regression.py`: Ordinary Least Squares linear regression.
  - `logistic_regression.py`: Classification using sigmoid activation and log-loss.
  - `knn.py`: K-Nearest Neighbors classifier and regressor.
  - `kmeans.py`: K-Means clustering algorithm.
- **`neural_networks/`**
  - `perceptron.py`: The single-layer binary classifier.
  - `dense_layer.py`: Fully connected layer representation (weights, biases, forward pass).
  - `backpropagation.py`: Chain rule derivatives and error backpropagation logic.

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.8+
- [uv](https://github.com/astral-sh/uv) (recommended) or `pip`

### 2. Installation & Setup
Clone the repository and set up a virtual environment:

```bash
# Clone the repository
git clone https://github.com/yourusername/ml-from-scratch.git
cd ml-from-scratch

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

### 3. Running Tests
Verify your implementations using `pytest`:

```bash
pytest
```

---

## 🛠 Future Additions & Roadmap
This repository is designed to be highly extensible. Future extensions plan to cover:
- [ ] Support for regularization (Lasso/Ridge) in regression.
- [ ] Tree-based algorithms (Decision Trees, Random Forests).
- [ ] Advanced Optimizers (Adam, RMSProp).
- [ ] Convolutional Neural Networks (CNNs) components from scratch.

---

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
