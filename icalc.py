# -*- coding: utf-8 -*-
"""
icalc is a command-line based interactive calculator which mimics how the Python 
interactive interpreter evaluates mathematical expressions.
"""


# note: naming the method below 'eval' will hide the python's built-in method
# which goes by the same name.
def eval_(expr):
    """Evaluates the expression passed in via 'expr'."""
    # tests expr for None and splits it into parts using '+' if it isn't
    expr_parts = expr and expr.split('+')
    
    if len(expr_parts) < 2:
        raise ValueError('Invalid expression provided: %s' % expr)
    
    # converts operands to integers
    figures = [int(x) for x in expr_parts]
    return sum(figures)


