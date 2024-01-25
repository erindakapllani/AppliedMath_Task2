def derive(f, x, h=0.0001):
    """
    Calculate the derivative of the function f at the point x using numeric differentiation.
    """
    # Using the central difference formula for numerical derivative
    derivative = (f(x + h) - f(x - h)) / (2 * h)
    
    return derivative
