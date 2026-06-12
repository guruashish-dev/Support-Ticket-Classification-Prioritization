#!/usr/bin/env python
"""
Quick test to verify all dependencies are installed and working.
Run this before opening the notebook.
"""

import sys

def check_imports():
    deps = {
        'pandas': 'pandas',
        'numpy': 'numpy',
        'sklearn': 'scikit-learn',
        'matplotlib': 'matplotlib',
    }
    
    missing = []
    for module, package in deps.items():
        try:
            __import__(module)
            print(f"✓ {package}")
        except ImportError:
            print(f"✗ {package} (MISSING)")
            missing.append(package)
    
    if missing:
        print(f"\nInstall missing packages with:")
        print(f"  pip install {' '.join(missing)}")
        return False
    
    print("\n✓ All dependencies installed!")
    return True

if __name__ == '__main__':
    print(f"Python version: {sys.version}")
    print(f"Python executable: {sys.executable}\n")
    print("Checking dependencies...\n")
    
    if check_imports():
        print("\nYou're ready to run the notebook!")
        sys.exit(0)
    else:
        sys.exit(1)
