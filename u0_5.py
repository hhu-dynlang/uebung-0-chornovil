import math

def solve_equasion(a, b, c):
    return [(-b+math.sqrt(b*b-4*a*c))/(2*a), (-b-math.sqrt(b*b-4*a*c))/(2*a)]

print(solve_equasion(3, -15, 18))
