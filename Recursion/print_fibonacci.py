# print fibonacci serise using recursion


def cal_fibo_series(a, b, n):
    if n == 0:
        return

    c = a + b
    print(c, end=" ")
    cal_fibo_series(b, c, n - 1)


a = 0
b = 1
print(a, b, end=" ")
n = 5
cal_fibo_series(a, b, n - 2)
