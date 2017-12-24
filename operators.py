#############################################################################################
#############   ADDITION - SUBTRACTION - MULTIPLICATION - DIVISION - EXPONENTIATION  ########
#############################################################################################
fval1 = 1.556
fval2 = 2.667

print("Addition: ", fval1 + fval2)
print("Subtraction: ", '%.2f' % (fval1 - fval2))
print("Multiplication: ", '%.2f' % (fval1 * fval2))
print("Division: ", '%.2f' % (fval1 / fval2))
print("Exponentiation: ", '%.2f' % (fval1 ** 2))
print("Negation: ", -fval1)
print("Modulo division  5 % 2=", (5 % 2))
print("Floor division (integer division) 3 // 2=", (3 // 2))


####################################################
##################   LOGICAL OPERATORS  ########
#####################################################

lval1 = True
lval2 = False
print('Logical True and False:', lval1 and lval2)
print('Logical True or False:', lval1 or lval2)
print('Logical not True', not lval1)
print('Equality', (fval1 == fval2))
print('Inequality', (fval1 != fval2))
print('Magnitude Comparisons (<): ', (fval1 < fval2))
print('Magnitude Comparisons (<=): ', (fval1 <= fval2))
print('Magnitude Comparisons (>): ', (fval1 > fval2))
print('Magnitude Comparisons (>=): ', (fval1 >= fval2))

####################################################
##################  BITWISE OPERATORS  ########
#####################################################

print("bitwise or 2 | 1 =",(2 | 1))
print("bitwise and 2 & 1 =",(2 & 1))
print("bit shift left one bit 2 << 1 =",(2 << 1))
print("bit shift left three bits 2 << 3 =",(2 << 3))
print("bit shift right one bit 2 >> 1 =",(2 >> 1))