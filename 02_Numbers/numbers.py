# Numbers :: int, float, complex

x,y,z = 10, 10.5, 10j
print(z, type(z))

#Int ::  Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
x,y,z = 1023444, -1345354, 1
print(x,y,z)


# Float :: Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
x,y,z = 1043.4, -10.59, 1.0
print(x,y,z)

## Float can also be scientific numbers with an "e" to indicate the power of 10.
x,y,z = 32e5, 34E2, -33.1e43
print(x,y,z)


# Complex :: Complex numbers are written with a "j" as the imaginary part:
x,y,z = 3j, 3+5J, -5j
print(x,y,z)


# Type Conversion :: we can convert from one type to another with the int(), float(), and complex() methods:
print(float(12), int(34.5), complex(2))