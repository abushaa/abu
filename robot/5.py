import robot
r = robot.rmap()
r.lm('task5')
r.sleep = 0.02
def task():
    def f():
        while r.fr():
            r.pt()
            r.dn(1)
            r.rt(1)
            r.pt()
            r.up(1)
            r.rt(1)
            r.pt()
            r.rt(2)
    def g():
        while r.fl():
            r.lt()
        while r.fu():
            r.up()
    f()
    g()
    r.dn(3)
    f()
    g()
    r.dn(6)
    f()
r.start(task)

