import os
import sys

def writable_path(*paths):
    if getattr(sys, "frozen", False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.abspath(".")
    
    full_path = os.path.join(base_path, *paths)

    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    return full_path