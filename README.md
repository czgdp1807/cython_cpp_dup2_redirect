# 🔁 Redirect stdout using `_dup2` via C++ and expose via Cython

This version moves the redirection logic to C++ and uses Cython just to expose it to Python.

## 🛠 Build Instructions

### 1. Install Miniconda
👉 https://docs.conda.io/en/latest/miniconda.html

### 2. Create environment

```bash
conda create -n cy_cpp_dup_env python=3.10 cython pip setuptools
conda activate cy_cpp_dup_env
```

### 3. Build the Cython + C++ module

```bash
python setup.py build_ext --inplace
```

### 4. Run the script

```bash
python test_redirect.py
```

Check `output.txt` for redirected output.

## 📄 Files

- `redirect_cpp.h` — C++ implementation using `_dup2`
- `redirect.pyx` — Cython wrapper
- `setup.py` — Build script
- `test_redirect.py` — Python test
