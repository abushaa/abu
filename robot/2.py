import robot
r = robot.rmap()
r.lm('task2')
r.sleep = 0.1
def task():
    def g():
        r.rt(1)
        r.pt()
        r.up(1)
        r.lt(1)
        r.pt()
        r.up(1)
        r.rt(1)
        r.pt()
        r.dn(1)
        r.rt(1)
        r.pt()
    def f():
        r.dn(1)
        r.rt(1)
    g()
    f()
    g()
    f()
    g()
    f()
    g()
    f()
    g()
    
r.start(task)

