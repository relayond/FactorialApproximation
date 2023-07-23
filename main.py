from numpy import linalg, array, unique


def factorial(n):
    if n == 0:
        return 1
    result = n
    for i in range(1,n):
        result *= i
    return result

def createMatrix(acc):
    m = []
    a = []
    augment = []
    for i in range(1, acc+1):
        for j in range(1, acc+1):
            a.append(i**j) 
        m.append(a)
        a = []
        augment.append(factorial(i))
    return array(m), array(augment)

running = True
while running:
    try:
        accuracy = int(input("Enter how many terms you would like: "))
    except TypeError:
        print("Enter a number.\n")
        continue
    matrix, augment = createMatrix(accuracy)
    rref = linalg.solve(matrix, augment)
    equation = ""
    i = 1
    for coef in rref:
        equation += f"{coef}*(x^{i})+"
        i += 1
    print(equation)