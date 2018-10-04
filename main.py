from sympy import *

# definindo as 'variaveis'
t, y = symbols("t, y")


def main():
    expr = sympify(input('function: '))
    y0 = float(input('y0: '))
    t0 = float(input('t0: '))
    h = float(input('h: '))
    n = int(input('n: '))
    Euler(expr, y0, t0, h, n)

def Euler(expr, y0, t0, h, n):
    # initializing list
    axis_x = []
    axis_y = [y0]
    # defining tn
    for i in range(n+1):
        # inserting the current Tn in the axis list
        tn = t0 + i*h
        axis_x.append(tn)
        # calculating Yn+1 using Euler (Yn+1 = Yn + h*Fn)
        Yn1 = axis_y[i] + h*(# cotinue)


# Executa o main do programa
if __name__ == "__main__":
    main()
