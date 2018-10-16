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
    elif words[0] == 'euler_aprimorado':
        EulerAprimorado(float(words[1]), float(words[2]), float(words[3]), int(words[4]), sympify(words[5]))
    elif words[0] == 'runge_kutta':
        rungekutta(float(words[1]), float(words[2]), float(words[3]), int(words[4]), sympify(words[5]))

def ShowGraphic(x, y, title):
    plt.title(title)
    plt.xlabel('t')
    plt.ylabel('y')
    plt.plot(x, y, 'go')
    plt.plot(x, y, 'k:', color='blue')
    plt.show()

def fn(expr, yn, tn):
    return expr.subs( [ (t, tn), (y, yn) ] )

def Euler(y0, t0, h, n, expr):
    # initializing list
    axis_x = []
    axis_y = [y0]
    # defining tn
    for i in range(n+1):
        # inserting the current Tn in the axis list
        tn = t0 + i*h
        axis_x.append(round(tn , 3))
        # calculating Yn+1 using Euler (Yn+1 = Yn + h*Fn)
        if i != n:
            Yn1 = axis_y[i] + h*(expr.subs([(y, axis_y[i]), (t, tn)]))
            # check for backward euler option
            axis_y.append(round(Yn1, 7))

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
        axis_x.append(round(tn, 3))
        if i != n:
            #Yn+1 = Yn + h*Fn+1
            Yn1 = solve(axis_y[i]+h*(expr.subs(t, tn1)) - y, implicit=True)
            axis_y.append(round(Yn1[0], 7))

    for j in range(n+1):
        print(axis_x[j], axis_y[j])
    ShowGraphic(axis_x, axis_y, "Euler Inverso")

def EulerAprimorado(y0, t0, h, n, expr):
    #initializing lists
    axis_x = []
    axis_y = [y0]
    for i in range(n+1):
        tn = t0 + i*h
        tn1 = tn + h
        axis_x.append(round(tn, 3))
        if i != n:
            #Yn+1 = Yn + (Fn + Fn+1)*h/2
            Yn1 = solve(axis_y[i] + (h/2)*(expr.subs(t, tn1) + expr.subs([(y, axis_y[i]), (t, tn)])) - y, implicit=True)
            axis_y.append(round(Yn1[0], 7))

    for j in range(n+1):
        print(axis_x[j], axis_y[j])
    ShowGraphic(axis_x, axis_y, "Euler Aprimorado")

def rungekutta(y0, t0, h, n, expr):
    #initializing lists
    axis_x = []
    axis_y = [y0]
    for i in range(n+1):
        tn = t0 + i*h
        if i != n:
            yn = axis_y[i]
            # defining K's
            k1 = expr.subs( [ (t, tn),     (y, yn)             ] )
            k2 = expr.subs( [ (t, tn+h/2), (y, yn + (h/2)*k1)  ] )
            k3 = expr.subs( [ (t, tn+h/2), (y, yn + (h/2)*k2)  ] )
            k4 = expr.subs( [ (t, tn+h),   (y, yn + h*k3)      ] )
            # finding Yn+1 by runge-kutta: Yn1 = Yn + (h/6)*(k1 + 2k2 + 2k3 + k4)
            Yn1 = yn + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
            # Saving values into the arrays
            axis_y.append(round(Yn1, 7))
        axis_x.append(round(tn, 3))
    
    # printing the values
    for j in range(n+1):
        print(axis_x[j], axis_y[j])
    ShowGraphic(axis_x, axis_y, "Runge-Kutta Grau 4")

def AdamBashforth(input_y, t0, h, n, expr, order):
    # initializing lists
    axis_x = []
    axis_y = [input_y[-1]]
    if order == 2:
        for i in range(n+1):
            tn = t0 + i*h
            if != n:
                tn_1 = tn - h
                yn = axis_y[i]
                yn_1 = input_y[0]
                # Defining Fn's
                Fn_1 = (1/2)*expr.subs( [ (t, tn_1), (y, yn_1) ] )
                Fn   = (3/2)*expr.subs( [ (t, tn),   (y, yn)   ] )
                # Finding Yn+1 by Adam-Bashforth: Yn+1 = h*(Fn - Fn_1)
                Yn1 = h*(Fn - Fn_1)
                # Saving values into the arrays
                axis_y.append(round(Yn1, 7))
            axis_x.append(round(tn, 3))
    elif order == 3:
        for i in range(n+1):
            tn = t0 + i*h
            if != n:
                tn_1 = tn - h
                tn_2 = tn_1-h
                yn = axis_y[i]
                yn_1 = input_y[0]
                # Defining Fn's
                Fn_1 = (1/2)*expr.subs( [ (t, tn_1), (y, yn_1) ] )
                Fn   = (3/2)*expr.subs( [ (t, tn),   (y, yn)   ] )
                # Finding Yn+1 by Adam-Bashforth: Yn+1 = h*(Fn - Fn_1)
                Yn1 = h*(Fn - Fn_1)
                # Saving values into the arrays
                axis_y.append(round(Yn1, 7))
            axis_x.append(round(tn, 3))
            

# Executa o main do programa
if __name__ == "__main__":
    main()
