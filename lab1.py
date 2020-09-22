import math
class OM1:
    def iter(self, n, x):
        if n < 100:
            print(n, "ітерація. x =", x, 'f(x) = %.15f'%(self.f(x)))
    def __init__(self,coef):
        self.coef = coef[::-1]
        self.b = 0
        self.h = 0
        self.newt = 0

    def f(self,x):
        y = 0
        for i in range(len(self.coef)):
            y += self.coef[i]*(x**i)
        return y

    def m_b(self,x0, x1, e):
        n = 1
        condition = True
        while condition:
            x2 = (x0 + x1) / 2
            self.iter(n, x2)
            if self.f(x0) * self.f(x2) < 0:
                x1 = x2
            else:
                x0 = x2
            print(f'[{x0}, {x1}]', end = " ")
            n += 1
            condition = abs(self.f(x2)) > e
        self.b = n
        return x2

    def m_h(self, x0, x1, e):
        x = lambda a, b: (a*self.f(b)-b*self.f(a)) / (self.f(b) - self.f(a))
        n = 0;
        if self.f(x0) * self.f(x(x0, x1)) <= 0:
            x1 = x(x0, x1)
        else:
            x0 = x(x0, x1)
        while (math.fabs(self.f(x(x0, x1))) > e):
            print(f'[{x0}, {x1}]', end = " ")
            if self.f(x0) * self.f(x(x0, x1)) <= 0:
                x1 = x(x0, x1)
                self.iter(n+1, x1)
                n += 1
        else:
            x0 = x(x0, x1)
        n += 1
        self.h = n
        return x0

    def Df(self,xn):
        y = 0
        for i in range(len(self.coef)):
            if i>0:
                y += i*self.coef[i] * (xn ** (i-1))
        return y

    def m_n(self,x0,e):
        xn = x0
        for n in range(0, 100):
            fxn = self.f(xn)
            self.iter(n+1, xn)
            if abs(fxn) < e:
                self.newt = n+1
                print("Знайдено корінь x =", xn, ', f(x) = %.15f'%(p.f(xn)), "\n")
                return xn
            Dfxn = self.Df(xn)
            if Dfxn == 0:
                print("Похідна дорівнює нулю, коренів нема.\n")
                return None
            xn = xn - fxn / Dfxn
        print("Після 100 кроків кореня не знайдено")
        return None
#
arr = [3,-2,-4,0,2,7]
left = -2
right = -1
eps = 0.00001
#
p = OM1(arr)
l = "Поліном: "
exp = len(arr) - 1
for n in range(exp+1):
    if exp-n == 0: 
        l += str(arr[n]) if arr[n] < 0 else "+" + str(arr[n]) + " = 0"
        break
    if arr[n] != 0:
        l += (str(arr[n]) if arr[n] < 0 else "+" + str(arr[n])) + "x" + (("^" + str(exp-n)) if exp-n > 1 else "")
print(l)
print('Метод бісекції:')
x = p.m_b(left, right, eps)
print("Знайдено корінь x =", x, ', f(x) = %.15f'%(p.f(x)), "\n")
print('Метод хорд:')
x = p.m_h(left, right, eps)
print("Знайдено корінь x =", x, ', f(x) = %.15f'%(p.f(x)), "\n")
print('Метод Ньютона:')
p.m_n(right, eps)
l = "Найбільш ефективним є метод "
if p.b <= p.h and p.b <= p.newt:
    l += "бісекції.\n"
elif p.h <= p.b and p.h <= p.newt:
    l += "хорд.\n"
elif p.newt <= p.b and p.newt <= p.h:
    l += "Ньютона.\n"
print(l)