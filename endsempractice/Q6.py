base = int(input("Enter the base: "))
exp = int(input("Enter the exponent: "))
def power(base, exp):
    if exp == 0:
        return 1
    elif exp < 0:
        return 1/(base**(-exp))
    else:
        return base**exp
print(f"{base} raised to the power of {exp} is: {power(base, exp)}")