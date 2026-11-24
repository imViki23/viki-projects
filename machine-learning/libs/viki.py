USE_GPU = True

if USE_GPU:
    try:
        import cupy as xp
        print("CuPy activated")
    except ImportError:
        import numpy as xp
        print("Problem with CuPy, switched to Numpy")
else:
    import numpy as xp
    print("Numpy activated")

def asarray(data):
    return xp.asarray(data)

def mean(data):
    return xp.mean(data)