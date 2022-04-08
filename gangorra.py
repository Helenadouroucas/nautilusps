erro=30
kp = 3
ki = 1
kd =0.1
errop =0
sp = 0
for i in range(10):
    pid = kp*erro+kd*(erro-errop)+ki*(erro+sp)
    errop = erro
    sp+=erro
    print(pid)
print("após 10 loops o PID vale",pid)