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

#############################################################################################
##################   LOGICAL OPERATORS  ########
#############################################################################################

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