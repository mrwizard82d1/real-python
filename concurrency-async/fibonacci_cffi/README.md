Using the Python foreign function interface (FFI).

To run this code, one must take two steps:

1. Build the shared object file
   - `./build.sh`
2. Run the python script in a `uv` virtual environment
   - `uv run python fibonacci_ctypes.py`
3. Time the script (if desired)
   - `uv run /usr/bin/time python fibonacci_ctypes.py`
