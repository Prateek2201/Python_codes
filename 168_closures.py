# function returning function called-- closure or first class function
def to_pow(x):
    def calc_pow(n):
        return n**x
    return calc_pow

cube= to_pow(3)
print(cube(2))

sq= to_pow(2)
print(sq(4))
