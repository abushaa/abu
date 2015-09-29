import robot
r = robot.rmap()
r.lm('task6')
n=int(input())
m=int(input())
r.sleep = 0.02
def task():
    for i in range(0,  n):
        r.pt()
        r.rt(1)
    r.lt((n+1)//2)
    for k in range(0,  m):
        r.pt()
        r.dn(1)
r.start(task)

