import robot
r = robot.rmap()
r.lm('task3')
r.sleep = 0.02
def task():
    while r.fr():
        r.rt(1)
        r.rt(1)
        r.dn(1)
        r.up(1)
r.start(task)

