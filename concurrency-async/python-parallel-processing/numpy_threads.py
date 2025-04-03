"""
Determine if `numpy` actually uses multiple threads for number crunching.

At the command line run, `/usr/bin/time python numpy_threads.py`
"""

import numpy as np


rng = np.random.default_rng(seed=42)
matrix = rng.random(size=(5000, 5000))
matrix @ matrix
