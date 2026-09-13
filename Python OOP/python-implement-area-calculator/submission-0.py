import math

class AreaCalc:
    def calculate(self, length, width=None):
        if width is None:
            ans = math.pi * (length)**2
            ans = round(ans, 2)
            return ans
        else:
            new = length * width
            return new

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
