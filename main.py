import math

ts = [199, 214, 266, 288]
Ls = [0.2, 0.3, 0.4, 0.6]

sin_theta = 1/150
h1 = 0.1
h2 = 0.02

g = 9.81
d = 0.00794
T = 0.32
W = 0.26
pi = 3.14
k = 0.5

f = 0
for i in range(len(ts)):
    # k = (2/ts[i] * ((sin_theta + h1/Ls[i])**0.5 - (sin_theta+h2/Ls[i])**0.5))**2
    # f = pi**2 * g * d**5 / (8 * k * T**2 * W**2)
    #
    # print(f"K= {k} , f = {f}")

    f += (2*g*d/Ls[i])*((3.14**2)*(d**4)*(ts[i]**2)/(64*(T**2)*(W**2) * (((Ls[i]*sin_theta+h2)**0.5) - ((Ls[i]*sin_theta+h1)**0.5))**2) - k/(2*g))

    print("f: ", f)

f /= len(ts)
for i in range(len(ts)):
    time = -math.sqrt(f*Ls[i]/(2*g*d) + k/(2*g)) * (8*T*W)/(math.pi*d**2)*(math.sqrt(Ls[i]*sin_theta+h2) - math.sqrt(Ls[i]*sin_theta+h1))
    print("time: ", time)