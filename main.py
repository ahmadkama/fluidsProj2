import math

ts = [199, 214, 266, 288]
Ls = [0.2, 0.3, 0.4, 0.6]
Ls_tee = [0.2, 0.4]

sin_theta = 1/150
h1 = 0.1
h2 = 0.02

g = 9.81
d1 = 0.00794
# d3 = 0.00794
d3 = 0.01125
T = 0.32
W = 0.26
pi = 3.14
k1 = 0.5
k2 = 1

f = []
f_val = 0.0
for i in range(len(ts)):
    # k = (2/ts[i] * ((sin_theta + h1/Ls[i])**0.5 - (sin_theta+h2/Ls[i])**0.5))**2
    # f = pi**2 * g * d**5 / (8 * k * T**2 * W**2)
    #
    # print(f"K= {k} , f = {f}")

    f.append((2 * g * d1 / Ls[i]) * ((3.14 ** 2) * (d1 ** 4) * (ts[i] ** 2) / (64 * (T ** 2) * (W ** 2) * (((Ls[i] * sin_theta + h2) ** 0.5) - ((Ls[i] * sin_theta + h1) ** 0.5)) ** 2) - k1 / (2 * g)))

print("fs: ", f)
f_val = sum(f)/len(f)
print(f_val)

for i in range(len(ts)):
    time = -math.sqrt(f_val * Ls[i] / (2 * g * d1) + k1 / (2 * g)) * (8 * T * W) / (math.pi * d1 ** 2) * (math.sqrt(Ls[i] * sin_theta + h2) - math.sqrt(Ls[i] * sin_theta + h1))
    print("L:", Ls[i], "time: ", time, "model: ", ts[i])


# Tee Joint
A = (1-d1**2/(2*d3**2))**2
B = d1**4/(8*g*d3**4)

for L in Ls_tee:
    C = (f_val*L)/(2*g*d1) + k1/(2*g) + B*k2 - A/(2*g)
    D = math.sqrt(C)*4*T*W/(math.pi*d1**2)

    time = -2*D*(math.sqrt(L*sin_theta+h2) - math.sqrt(L*sin_theta+h1))
    print("L: ", L, "Time: ", time)
