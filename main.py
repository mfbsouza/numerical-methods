from sympy import *
import matplotlib.pyplot as plt

# definindo as 'variaveis'
t, y = symbols("t, y")

def main():
    # lendo os paramentros como string
    data = input()
    words = data.split()
    if words[0] == 'euler':
        Euler(float(words[1]), float(words[2]), float(words[3]), int(words[4]), sympify(words[5]), 1)
    elif words[0] == 'euler_inverso':
        EulerInverso(float(words[1]), float(words[2]), float(words[3]), int(words[4]), sympify(words[5]),1)
    elif words[0] == 'euler_aprimorado':
        EulerAprimorado(float(words[1]), float(words[2]), float(words[3]), int(words[4]), sympify(words[5]),1)
    elif words[0] == 'runge_kutta':
        rungekutta(float(words[1]), float(words[2]), float(words[3]), int(words[4]), sympify(words[5]),1)
    elif words[0] == 'adam_bashforth':
        order = int(words[-1])
        ys = []
        for i in range(1, order+1):
            ys.append(float(words[i]))
        AdamBashforth(ys, float(words[order+1]), float(words[order+2]), int(words[order+3]), sympify(words[order+4]), order)
    elif words[0] == 'adam_bashforth_by_euler':
        order = int(words[-1])
        t0 = float(words[2]) + float(words[3])*(order-1)
        list_y = Euler(float(words[1]), float(words[2]), float(words[3]), (order-1), sympify(words[5]), 0)
        AdamBashforth(list_y, t0, float(words[3]), int(words[4]), sympify(words[5]), order)
    elif words[0] == 'adam_bashforth_by_euler_inverso':
        order = int(words[-1])
        t0 = float(words[2]) + float(words[3])*(order-1)
        list_y = EulerInverso(float(words[1]), float(words[2]), float(words[3]), (order-1), sympify(words[5]), 0)
        AdamBashforth(list_y, t0, float(words[3]), int(words[4]), sympify(words[5]), order)
    elif words[0] == 'adam_bashforth_by_euler_aprimorado':
        order = int(words[-1])
        t0 = float(words[2]) + float(words[3])*(order-1)
        list_y = EulerAprimorado(float(words[1]), float(words[2]), float(words[3]), (order-1), sympify(words[5]), 0)
        AdamBashforth(list_y, t0, float(words[3]), int(words[4]), sympify(words[5]), order)
    elif words[0] == 'adam_bashforth_by_runge_kutta':
        order = int(words[-1])
        t0 = float(words[2]) + float(words[3])*(order-1)
        list_y = rungekutta(float(words[1]), float(words[2]), float(words[3]), (order-1), sympify(words[5]), 0)
        AdamBashforth(list_y, t0, float(words[3]), int(words[4]), sympify(words[5]), order)
    elif words[0] == 'adam_moulton':
        order = int(words[-1])
        ys = []
        for i in range(1, order):
            ys.append(float(words[i]))
        AdamMoulton(ys, float(words[order]), float(words[order+1]), int(words[order+2]), sympify(words[order+3]), order)
    elif words[0] == 'adam_moulton_by_euler':
        order = int(words[-1])
        t0 = float(words[2]) + float(words[3])*(order - 2)
        list_y = Euler(float(words[1]), float(words[2]), float(words[3]), (order - 2), sympify(words[5]), 0)
        AdamMoulton(list_y, t0, float(words[3]), int(words[4]), sympify(words[5]), order)

def ShowGraphic(x, y, title):
    plt.title(title)
    plt.xlabel('t')
    plt.ylabel('y')
    plt.plot(x, y, 'go')
    plt.plot(x, y, 'k:', color='blue')
    plt.show()

def Euler(y0, t0, h, n, expr, show):
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

    if show == 1:
        print(' x | y')
        for j in range(n+1):
            print(axis_x[j], axis_y[j])
        ShowGraphic(axis_x, axis_y, "Euler Simples")
    elif show == 0:
        return axis_y

def EulerInverso(y0, t0, h, n, expr, show):
    #initializing lists
    axis_x = []
    axis_y = [y0]
    for i in range(n+1):
        tn = t0 + i*h
        tn1 = tn + h
        axis_x.append(tn)
        if i != n:
            #Yn+1 = Yn + h*Fn+1
            Yn1 = solve(axis_y[i]+h*(expr.subs(t, tn1)) - y, implicit=True)
            axis_y.append(Yn1[0])
    if show == 1:
        for j in range(n+1):
            print(axis_x[j], axis_y[j])
        ShowGraphic(axis_x, axis_y, "Euler Inverso")
    elif show == 0:
        return axis_y

def EulerAprimorado(y0, t0, h, n, expr, show):
    #initializing lists
    axis_x = []
    axis_y = [y0]
    for i in range(n+1):
        tn = t0 + i*h
        tn1 = tn + h
        axis_x.append(tn)
        if i != n:
            #Yn+1 = Yn + (Fn + Fn+1)*h/2
            Yn1 = solve(axis_y[i] + (h/2)*(expr.subs(t, tn1) + expr.subs([(y, axis_y[i]), (t, tn)])) - y, implicit=True)
            axis_y.append(Yn1[0])
    if show == 1:
        for j in range(n+1):
            print(axis_x[j], axis_y[j])
        ShowGraphic(axis_x, axis_y, "Euler Aprimorado")
    elif show == 0:
        return axis_y

def rungekutta(y0, t0, h, n, expr, show):
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
            axis_y.append(Yn1)
        axis_x.append(tn)

    if show == 1:
        # printing the values
        for j in range(n+1):
            print(axis_x[j], axis_y[j])
        ShowGraphic(axis_x, axis_y, "Runge-Kutta Grau 4")
    elif show == 0:
        return axis_y

def AdamBashforth(input_y, t0, h, n, expr, order):
    # initializing lists
    axis_x = []
    axis_y = []
    # Storing the first values
    aux = order - 1
    for item in input_y:
        axis_y.append(item)
        t_aux = t0 - h*aux
        axis_x.append(t_aux)
        aux = aux - 1

    # Calculating Yn+1
    if order == 2:
        for i in range(1, n):
            tn = axis_x[i]
            tn_1 = axis_x[i-1]
            yn = axis_y[i]
            yn_1 = axis_y[i-1]
            # Defining Fn's
            Fn_1 = (1/2)*expr.subs( [ (t, tn_1), (y, yn_1) ] )
            Fn   = (3/2)*expr.subs( [ (t, tn),   (y, yn)   ] )
            # Finding Yn+1 by Adam-Bashforth: Yn+1 = Yn + h*(Fn - Fn_1)
            Yn1 = yn + h*(Fn - Fn_1)
            # Saving values into the arrays
            axis_y.append(Yn1)
            axis_x.append((tn+h))
    elif order == 3:
        for i in range(2, n):
            tn = axis_x[i]
            tn_1 = axis_x[i-1]
            tn_2 = axis_x[i-2]
            yn = axis_y[i]
            yn_1 = axis_y[i-1]
            yn_2 = axis_y[i-2]
            # Defining Fn's
            Fn_2 = (5/12) * expr.subs( [ (t, tn_2), (y, yn_2) ] )
            Fn_1 = (4/3)  * expr.subs( [ (t, tn_1), (y, yn_1) ] )
            Fn   = (23/12)* expr.subs( [ (t, tn),   (y, yn)   ] )
            # Finding Yn+1 by Adam-Bashforth:
            Yn1 = yn + h*(Fn - Fn_1 + Fn_2)
            # Saving values into the arrays
            axis_y.append(Yn1)
            axis_x.append((tn+h))
    elif order == 4:
        for i in range(3, n):
            tn = axis_x[i]
            tn_1 = axis_x[i-1]
            tn_2 = axis_x[i-2]
            tn_3 = axis_x[i-3]
            yn = axis_y[i]
            yn_1 = axis_y[i-1]
            yn_2 = axis_y[i-2]
            yn_3 = axis_y[i-3]
            # Defining Fn's
            Fn_3 = (3/8)   * expr.subs( [ (t, tn_3), (y, yn_3) ] )
            Fn_2 = (37/24) * expr.subs( [ (t, tn_2), (y, yn_2) ] )
            Fn_1 = (59/24) * expr.subs( [ (t, tn_1), (y, yn_1) ] )
            Fn   = (55/24) * expr.subs( [ (t, tn),   (y, yn)   ] )
            # Finding Yn+1 by Adam-Bashforth:
            Yn1 = yn + h*(Fn - Fn_1 + Fn_2 - Fn_3)
            # Saving values into the arrays
            axis_y.append(Yn1)
            axis_x.append((tn+h))
    elif order == 5:
        for i in range(4, n):
            tn = axis_x[i]
            tn_1 = axis_x[i-1]
            tn_2 = axis_x[i-2]
            tn_3 = axis_x[i-3]
            tn_4 = axis_x[i-4]
            yn = axis_y[i]
            yn_1 = axis_y[i-1]
            yn_2 = axis_y[i-2]
            yn_3 = axis_y[i-3]
            yn_4 = axis_y[i-4]
            # Defining Fn's
            Fn_4 = (251/720)  * expr.subs( [ (t, tn_4), (y, yn_4) ] )
            Fn_3 = (637/360)  * expr.subs( [ (t, tn_3), (y, yn_3) ] )
            Fn_2 = (109/30)   * expr.subs( [ (t, tn_2), (y, yn_2) ] )
            Fn_1 = (1387/360) * expr.subs( [ (t, tn_1), (y, yn_1) ] )
            Fn   = (1901/720) * expr.subs( [ (t, tn),   (y, yn)   ] )
            # Finding Yn+1 by Adam-Bashforth:
            Yn1 = yn + h*(Fn - Fn_1 + Fn_2 - Fn_3 + Fn_4)
            # Saving values into the arrays
            axis_y.append(Yn1)
            axis_x.append((tn+h))
    elif order == 6:
        for i in range(5, n):
            tn = axis_x[i]
            tn_1 = axis_x[i-1]
            tn_2 = axis_x[i-2]
            tn_3 = axis_x[i-3]
            tn_4 = axis_x[i-4]
            tn_5 = axis_x[i-5]
            yn = axis_y[i]
            yn_1 = axis_y[i-1]
            yn_2 = axis_y[i-2]
            yn_3 = axis_y[i-3]
            yn_4 = axis_y[i-4]
            yn_5 = axis_y[i-5]
            # Defining Fn's
            Fn_5 = (95/288)    * expr.subs( [ (t, tn_5), (y, yn_5) ] )
            Fn_4 = (959/480)   * expr.subs( [ (t, tn_4), (y, yn_4) ] )
            Fn_3 = (3649/720)  * expr.subs( [ (t, tn_3), (y, yn_3) ] )
            Fn_2 = (4991/720)  * expr.subs( [ (t, tn_2), (y, yn_2) ] )
            Fn_1 = (2641/480)  * expr.subs( [ (t, tn_1), (y, yn_1) ] )
            Fn   = (4277/1440) * expr.subs( [ (t, tn),   (y, yn)   ] )
            # Finding Yn+1 by Adam-Bashforth:
            Yn1 = yn + h*(Fn - Fn_1 + Fn_2 - Fn_3 + Fn_4 - Fn_5)
            # Saving values into the arrays
            axis_y.append(Yn1)
            axis_x.append((tn+h))
    elif order == 7:
        for i in range(6, n):
            tn = axis_x[i]
            tn_1 = axis_x[i-1]
            tn_2 = axis_x[i-2]
            tn_3 = axis_x[i-3]
            tn_4 = axis_x[i-4]
            tn_5 = axis_x[i-5]
            tn_6 = axis_x[i-6]
            yn = axis_y[i]
            yn_1 = axis_y[i-1]
            yn_2 = axis_y[i-2]
            yn_3 = axis_y[i-3]
            yn_4 = axis_y[i-4]
            yn_5 = axis_y[i-5]
            yn_6 = axis_y[i-6]
            # Defining Fn's
            Fn_6 = (19087/60480)  * expr.subs( [ (t, tn_6), (y, yn_6) ] )
            Fn_5 = (5603/2520)    * expr.subs( [ (t, tn_5), (y, yn_5) ] )
            Fn_4 = (135713/20160) * expr.subs( [ (t, tn_4), (y, yn_4) ] )
            Fn_3 = (10754/945)    * expr.subs( [ (t, tn_3), (y, yn_3) ] )
            Fn_2 = (235183/20160) * expr.subs( [ (t, tn_2), (y, yn_2) ] )
            Fn_1 = (18637/2520)   * expr.subs( [ (t, tn_1), (y, yn_1) ] )
            Fn   = (198721/60480) * expr.subs( [ (t, tn),   (y, yn)   ] )
            # Finding Yn+1 by Adam-Bashforth:
            Yn1 = yn + h*(Fn - Fn_1 + Fn_2 - Fn_3 + Fn_4 - Fn_5 + Fn_6)
            # Saving values into the arrays
            axis_y.append(Yn1)
            axis_x.append((tn+h))
    elif order == 8:
        for i in range(7, n):
            tn = axis_x[i]
            tn_1 = axis_x[i-1]
            tn_2 = axis_x[i-2]
            tn_3 = axis_x[i-3]
            tn_4 = axis_x[i-4]
            tn_5 = axis_x[i-5]
            tn_6 = axis_x[i-6]
            tn_7 = axis_x[i-7]
            yn = axis_y[i]
            yn_1 = axis_y[i-1]
            yn_2 = axis_y[i-2]
            yn_3 = axis_y[i-3]
            yn_4 = axis_y[i-4]
            yn_5 = axis_y[i-5]
            yn_6 = axis_y[i-6]
            yn_7 = axis_y[i-7]
            # Defining Fn's
            Fn_7 = (5257/17280)     * expr.subs( [ (t, tn_7), (y, yn_7) ] )
            Fn_6 = (32863/13440)    * expr.subs( [ (t, tn_6), (y, yn_6) ] )
            Fn_5 = (115747/13440)   * expr.subs( [ (t, tn_5), (y, yn_5) ] )
            Fn_4 = (2102243/120960) * expr.subs( [ (t, tn_4), (y, yn_4) ] )
            Fn_3 = (296053/13440)   * expr.subs( [ (t, tn_3), (y, yn_3) ] )
            Fn_2 = (242653/13440)   * expr.subs( [ (t, tn_2), (y, yn_2) ] )
            Fn_1 = (1152169/120960) * expr.subs( [ (t, tn_1), (y, yn_1) ] )
            Fn   = (16083/4480)     * expr.subs( [ (t, tn),   (y, yn)   ] )
            # Finding Yn+1 by Adam-Bashforth:
            Yn1 = yn + h*(Fn - Fn_1 + Fn_2 - Fn_3 + Fn_4 - Fn_5 + Fn_6 - Fn_7)
            # Saving values into the arrays
            axis_y.append(Yn1)
            axis_x.append((tn+h))

    # Priting values
    for j in range(n+1):
        print(axis_x[j], axis_y[j])
    ShowGraphic(axis_x, axis_y, "Adam-Bashforth de ordem: " + str(order))

def AdamMoulton(input_y, t0, h, n, expr, order):
    # initializing lists
    axis_x = []
    axis_y = []
    # Storing the first values
    aux = order - 2
    for item in input_y:
        axis_y.append(item)
        t_aux = t0 - h*aux
        axis_x.append(t_aux)
        aux = aux - 1

    # Caculating Yn+1
    if order == 2:
        for i in range(n):
            tn = axis_x[i]
            tn1 = tn + h
            yn = axis_y[i]
            # Defining Fn's
            Fn   = (1/2) * expr.subs( [ (t, tn),   (y, yn)   ] )
            Fn1  = (1/2) * expr.subs(t, tn1)
            # Finding Yn+1 by AdamMoulton: Yn+1 = Yn + h*(Fn+1 + Fn)
            Yn1 = solve(yn + h*(Fn1 + Fn) - y, Implicit=True)
            # Saving values into the arrays
            axis_y.append(Yn1[0])
            axis_x.append(tn1)
    elif order == 3:
        for i in range(1, n):
            tn = axis_x[i]
            tn1 = tn + h
            tn_1 = axis_x[i-1]
            yn = axis_y[i]
            yn_1 = axis_y[i-1]
            # Defining Fn's
            Fn_1 = (1/12) * expr.subs( [ (t, tn_1), (y, yn_1) ] )
            Fn   = (2/3)  * expr.subs( [ (t, tn),   (y, yn)   ] )
            Fn1  = (5/12) * expr.subs(t, tn1)
            # Finding Yn+1 by AdamMoulton: Yn+1 = Yn + h*(Fn+1 + Fn - Fn-1)
            Yn1 = solve(yn + h*(Fn1 + Fn - Fn_1) - y, Implicit=True)
            # Saving values into the arrays
            axis_y.append(Yn1[0])
            axis_x.append(tn1)
    elif order == 4:
        for i in range(2, n):
            tn = axis_x[i]
            tn1 = tn + h
            tn_1 = axis_x[i-1]
            tn_2 = axis_x[i-2]
            yn = axis_y[i]
            yn_1 = axis_y[i-1]
            yn_2 = axis_y[i-2]
            # Defining Fn's
            Fn_2 = (1/24)  * expr.subs( [ (t, tn_2), (y, yn_2) ] )
            Fn_1 = (5/24)  * expr.subs( [ (t, tn_1), (y, yn_1) ] )
            Fn   = (19/24) * expr.subs( [ (t, tn),   (y, yn)   ] )
            Fn1  = (3/8)   * expr.subs(t, tn1)
            # Finding Yn+1 by AdamMoulton: Yn+1 = Yn + h*(Fn+1 + Fn - Fn-1)
            Yn1 = solve(yn + h*(Fn1 + Fn - Fn_1 + Fn_2) - y, Implicit=True)
            # Saving values into the arrays
            axis_y.append(Yn1[0])
            axis_x.append(tn1)
    elif order == 5:
        for i in range(3, n):
            tn = axis_x[i]
            tn1 = tn + h
            tn_1 = axis_x[i-1]
            tn_2 = axis_x[i-2]
            tn_3 = axis_x[i-3]
            yn = axis_y[i]
            yn_1 = axis_y[i-1]
            yn_2 = axis_y[i-2]
            yn_3 = axis_y[i-3]
            # Defining Fn's
            Fn_3 = (19/720)  * expr.subs( [ (t, tn_3), (y, yn_3) ] )
            Fn_2 = (53/360)  * expr.subs( [ (t, tn_2), (y, yn_2) ] )
            Fn_1 = (11/30)   * expr.subs( [ (t, tn_1), (y, yn_1) ] )
            Fn   = (323/360) * expr.subs( [ (t, tn),   (y, yn)   ] )
            Fn1  = (251/720) * expr.subs(t, tn1)
            # Finding Yn+1 by AdamMoulton:
            Yn1 = solve(yn + h*(Fn1 + Fn - Fn_1 + Fn_2 - Fn_3) - y, Implicit=True)
            # Saving values into the arrays
            axis_y.append(Yn1[0])
            axis_x.append(tn1)
    elif order == 6:
        for i in range(4, n):
            tn = axis_x[i]
            tn1 = tn + h
            tn_1 = axis_x[i-1]
            tn_2 = axis_x[i-2]
            tn_3 = axis_x[i-3]
            tn_4 = axis_x[i-4]
            yn = axis_y[i]
            yn_1 = axis_y[i-1]
            yn_2 = axis_y[i-2]
            yn_3 = axis_y[i-3]
            yn_4 = axis_y[i-4]
            # Defining Fn's
            Fn_4 = (3/160)     * expr.subs( [ (t, tn_4), (y, yn_4) ] )
            Fn_3 = (173/1440)  * expr.subs( [ (t, tn_3), (y, yn_3) ] )
            Fn_2 = (241/720)   * expr.subs( [ (t, tn_2), (y, yn_2) ] )
            Fn_1 = (133/240)   * expr.subs( [ (t, tn_1), (y, yn_1) ] )
            Fn   = (1427/1440) * expr.subs( [ (t, tn),   (y, yn)   ] )
            Fn1  = (95/288)    * expr.subs(t, tn1)
            # Finding Yn+1 by AdamMoulton:
            Yn1 = solve(yn + h*(Fn1 + Fn - Fn_1 + Fn_2 - Fn_3 + Fn_4) - y, Implicit=True)
            # Saving values into the arrays
            axis_y.append(Yn1[0])
            axis_x.append(tn1)
    elif order == 7:
        for i in range(5, n):
            tn = axis_x[i]
            tn1 = tn + h
            tn_1 = axis_x[i-1]
            tn_2 = axis_x[i-2]
            tn_3 = axis_x[i-3]
            tn_4 = axis_x[i-4]
            tn_5 = axis_x[i-5]
            yn = axis_y[i]
            yn_1 = axis_y[i-1]
            yn_2 = axis_y[i-2]
            yn_3 = axis_y[i-3]
            yn_4 = axis_y[i-4]
            yn_5 = axis_y[i-5]
            # Defining Fn's
            Fn_5 = (863/60480)   * expr.subs( [ (t, tn_5), (y, yn_5) ] )
            Fn_4 = (263/2520)    * expr.subs( [ (t, tn_4), (y, yn_4) ] )
            Fn_3 = (6737/20160)  * expr.subs( [ (t, tn_3), (y, yn_3) ] )
            Fn_2 = (586/945)     * expr.subs( [ (t, tn_2), (y, yn_2) ] )
            Fn_1 = (15487/20160) * expr.subs( [ (t, tn_1), (y, yn_1) ] )
            Fn   = (2713/2520)   * expr.subs( [ (t, tn),   (y, yn)   ] )
            Fn1  = (19087/60480) * expr.subs(t, tn1)
            # Finding Yn+1 by AdamMoulton:
            Yn1 = solve(yn + h*(Fn1 + Fn - Fn_1 + Fn_2 - Fn_3 + Fn_4 - Fn_5) - y, Implicit=True)
            # Saving values into the arrays
            axis_y.append(Yn1[0])
            axis_x.append(tn1)
    elif order == 8:
        for i in range(6, n):
            tn = axis_x[i]
            tn1 = tn + h
            tn_1 = axis_x[i-1]
            tn_2 = axis_x[i-2]
            tn_3 = axis_x[i-3]
            tn_4 = axis_x[i-4]
            tn_5 = axis_x[i-5]
            tn_6 = axis_x[i-6]
            yn = axis_y[i]
            yn_1 = axis_y[i-1]
            yn_2 = axis_y[i-2]
            yn_3 = axis_y[i-3]
            yn_4 = axis_y[i-4]
            yn_5 = axis_y[i-5]
            yn_6 = axis_y[i-6]
            # Defining Fn's
            Fn_6 = (275/24192)     * expr.subs( [ (t, tn_6), (y, yn_6) ] )
            Fn_5 = (11351/120960)  * expr.subs( [ (t, tn_5), (y, yn_5) ] )
            Fn_4 = (1537/4480)     * expr.subs( [ (t, tn_4), (y, yn_4) ] )
            Fn_3 = (88547/120960)  * expr.subs( [ (t, tn_3), (y, yn_3) ] )
            Fn_2 = (123133/120960) * expr.subs( [ (t, tn_2), (y, yn_2) ] )
            Fn_1 = (4511/4480)     * expr.subs( [ (t, tn_1), (y, yn_1) ] )
            Fn   = (139849/120960) * expr.subs( [ (t, tn),   (y, yn)   ] )
            Fn1  = (5257/17280)    * expr.subs(t, tn1)
            # Finding Yn+1 by AdamMoulton:
            Yn1 = solve(yn + h*(Fn1 + Fn - Fn_1 + Fn_2 - Fn_3 + Fn_4 - Fn_5 + Fn_6) - y, Implicit=True)
            # Saving values into the arrays
            axis_y.append(Yn1[0])
            axis_x.append(tn1)

    # Printing values
    for j in range(n+1):
        print(axis_x[j], axis_y[j])
    ShowGraphic(axis_x, axis_y, "Adam-Bashforth de ordem: " + str(order))

# Executa o main do programa
if __name__ == "__main__":
    main()
