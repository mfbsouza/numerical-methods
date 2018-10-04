from sympy import *

# definindo as 'variaveis'
t, y = symbols("t, y")

def main():
    # lendo os paramentros como string
    data = input()
    words = data.split()
    if words[0] == 'euler':
        Euler(float(words[1]), float(words[2]), float(words[3]), int(words[4]), sympify(words[5]))

def Euler(y0, t0, h, n, expr):
    # initializing list
    axis_x = []
    axis_y = [y0]
    # defining tn
    for i in range(n+1):
        # inserting the current Tn in the axis list
        tn = t0 + i*h
        axis_x.append(tn)
        # calculating Yn+1 using Euler (Yn+1 = Yn + h*Fn)
        if i != n:
            Yn1 = axis_y[i] + h*(expr.subs([(y, axis_y[i]), (t, tn)]))
            axis_y.append(Yn1)
    print(' x | y')
    for j in range(n+1):
        print(axis_x[j], axis_y[j])

# Executa o main do programa
if __name__ == "__main__":
    main()
