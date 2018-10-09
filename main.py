from sympy import *
import matplotlib.pyplot as plt

# definindo as 'variaveis'
t, y = symbols("t, y")

def main():
    # lendo os paramentros como string
    data = input()
    words = data.split()
    if words[0] == 'euler':
        Euler(float(words[1]), float(words[2]), float(words[3]), int(words[4]), sympify(words[5]))
    elif words[0] == 'euler_inverso':
        EulerInverso(float(words[1]), float(words[2]), float(words[3]), int(words[4]), sympify(words[5]))

def ShowGraphic(x, y, title):
    plt.title(title)
    plt.xlabel('t')
    plt.ylabel('y')
    plt.plot(x, y, 'go')
    plt.plot(x, y, 'k:', color='blue')
    plt.show()

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
            # check for backward euler option
            axis_y.append(Yn1)

    print(' x | y')
    for j in range(n+1):
        print(axis_x[j], axis_y[j])
    ShowGraphic(axis_x, axis_y, "Euler Simples")

def EulerInverso(y0, t0, h, n, expr):
    #initializing lists
    axis_x = []
    axis_y = [y0]
    for i in range(n+1):
        tn = t0 + i*h
        tn1 = tn + h
        axis_x.append(tn)
        if i != n:
            Yn1 = solve(axis_y[i]+h*(expr.subs(t, tn1)) - y, implicit=True)
            axis_y.append(Yn1[0])

    for j in range(n+1):
        print(axis_x[j], axis_y[j])
    ShowGraphic(axis_x, axis_y, "Euler Inverso")

# Executa o main do programa
if __name__ == "__main__":
    main()
