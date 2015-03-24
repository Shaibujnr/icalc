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
    
    # now lets evaluate the parts in expr_parts in order to account for the '-'
    # operator if any exists
    expr_results = []
    for expr in expr_parts:
        more_parts = [x for x in expr.split('-') if x != '']
        if len(more_parts) < 2:
            expr_results.append(int(expr))
        else:
            parts = [int(x) for x in more_parts]
            result = parts[0]
            for part in parts[1:]:
                result -= part
            expr_results.append(result)
            
    if len(expr_results) < 2 and type(expr_results[0]) == str:
        raise ValueError('Invalid expression provided: %s' % expr)
    
    # sum up all values in expr_results
    return sum(expr_results)
        
        
        
        
def eval2(expr):
    ''''evaluates expressions containing only division and multiplication'''
    
    
    expr_parts= expr and expr.split('*')
    
    expr_results=[]
    
    for expr in expr_parts:
    #further splitting the '/' expressions
        
        more_parts= [x for x in expr.split('/') if x !='']
        if len(more_parts)==1:
        # to ensure that,the expression is valid(no characters)
            try: 
                int(expr)
                expr_results.append(int(expr))
            except:
                raise ValueError('Invalid expression provided: %s' % expr)
        else:
            try:
                parts=[int(x) for x in more_parts]
                parts[0]= str(str(parts[0])+'.0')
                results= float(parts[0])
                    
                for part in parts[1:]:
                    results /= part
                expr_results.append(results)
            except:
                raise ValueError('Invalid expression provided: %s' % expr)
            
            
        x= expr_results[0]
        for i in expr_results[1:]:
            x*=i
        
    
    if len(expr_results)<2 and type(expr_results[0])==str:
        raise ValueError('Invalid expression provided:%s' %expr)
        
    
    return x


    