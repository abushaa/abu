import robot
r = robot.rmap()
r.lm('task4')
r.sleep = 0.02
def task():
    def g():
        while r.fu():
            r.up()
        while r.fr():
            r.rt()
    def f(i):
            i=0
            while i<5:
                r.dn(1)
                r.lt(1)
                r.pt()
                i+=1
    g()
    f(5)
    g()
    r.dn(2)
    f(5)
    g()
    r.dn(4)
    f(5)
r.start(task)

