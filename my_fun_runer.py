import time

class Sheduler:
    def __init__(self):
        self.fun_list = {}

    def add_fun(self, fun, t_sleep):
        self.fun_list[fun] = t_sleep

    def run(self, *args):
        for f, t in self.fun_list.items():
            time.sleep(t)
            return f(*args)

def a_b(a, b):
    return a + b

M = Sheduler()
M.add_fun(a_b, 5)
print(M.run(2, 3))