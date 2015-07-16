"""
Defines unit tests for icalc.
"""
import unittest
import icalc



class iCalcTestCase(unittest.TestCase):

    def test_plus_op_eval(self):
        # provides a single expressions using the addition ('+') operator in
        # the different forms it can be provided to icalc's eval_ method
        exprs = ['2+2', '2+ 2', '2 +2', '2 + 2', ' 2+ 2 ']
        for expr in exprs:
            result = icalc.eval_(expr)
            self.assertEqual(4, result, "4 expected for expression '%s'" % expr)
    
    def test_plus_op_more_values_eval(self):
        expr = '2+3+7+9+-4'
        result = icalc.eval_(expr)
        self.assertEqual(17, result, "17 expected for expression '%s'" % expr)
    
    
    def test_minus_op_eval(self):
        # provides a single expressions using the addition ('-') operator in
        # the different forms it can be provided to icalc's eval_ method
        exprs = ['5-3', '5- 3', '5 -3', '5 - 3', ' 5- 3 ']
        for expr in exprs:
            result = icalc.eval_(expr)
            self.assertEqual(2, result, "2 expected for expression '%s'" % expr)
            
    def test_cheval(self):
        #testing cheval variation one
        exprs=["99-76","-76+99","---76+99","-76-+-99","99+-76"]
        for expr in exprs:
            result= icalc.cheval(expr)
            self.assertEqual(23,result,"expected 23 as result for '%s'"%expr)

        

if __name__ == "__main__":
    unittest.main()
    