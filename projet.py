import matplotlib.pyplot as plt
import numpy as np

# Data
Re = [0.001,0.010,0.1,1,2,5,10,20,50,100,150,200,400]
mu = 0.2
rho = 1 
g = 9.81
L = 2

Vitesse_1 = Re
Vitesse_2 = [2*Re[i] for i in range(len(Re))]
Vitesse_3 = Vitesse_2   

Perte_1 = [0.59506,5.9507,59.514,596.16,1195.9,3035.2,6315.7,14002,47421,136180,261960,424720,1471200]
Perte_2 = [0.6219,6.213,62.141,623.71,1256.7,3246,6931.7,15670,51677,142290,268350,429050,1420400]
Perte_3 = [0.91721,9.1722,91.73,919.22,1847.4,4744.4,10095,22757,75731,212890,407690,660270,2271800]

# Plot global
fig = plt.figure(1)
ax = fig.add_subplot(111)
ax.plot(Re,Perte_1,'r-',label='Perte 1')
ax.plot(Re,Perte_2,'b-',label='Perte 2')
ax.plot(Re,Perte_3,'g-',label='Perte 3')
ax.set_xlabel('Re')
ax.set_ylabel('Perte de charge')
ax.legend()

# Plot pour Re<10
fig = plt.figure(2)
ax = fig.add_subplot(111)
ax.plot(Re[:6],Perte_1[:6],'r-',label='Perte 1')
ax.plot(Re[:6],Perte_2[:6],'b-',label='Perte 2')
ax.plot(Re[:6],Perte_3[:6],'g-',label='Perte 3')
ax.set_xlabel('Re')
ax.set_ylabel('Perte de charge')
ax.legend()

# Corrélation pour Re > 5

# Perte 1
coef1 = np.polyfit((Vitesse_1[5:]),(Perte_1[5:]),2)
print(coef1)

k_1_hr = mu/coef1[1]
print('Perméabilité du milieu 1 k_1 = ',k_1_hr)

# idem bas reynolds
coef1 = np.polyfit((Vitesse_1[:6]),(Perte_1[:6]),2)
print(coef1)

k_1_br = mu/coef1[1]
print('Perméabilité du milieu 1 br k_1 = ',k_1_br)

beta1 = [(Perte_1[i]/L-mu*Vitesse_1[i]/k_1_hr)*1/(rho*Vitesse_1[i]**2) for i in range(5,len(Vitesse_1))]
conduc_1 =k_1_br*rho*g/mu
print('Conductivité du milieu 1 K1 = ',conduc_1)

# Perte 2
coef2 = np.polyfit((Vitesse_2[5:]),(Perte_2[5:]),2)

k_2_hr = mu/coef2[1]
print('Perméabilité du milieu 2 k_2 = ',k_2_hr)

# idem bas reynolds

coef2 = np.polyfit((Vitesse_2[:6]),(Perte_2[:6]),2)

k_2_br = mu/coef2[1]
print('Perméabilité du milieu 2 br k_2 = ',k_2_br)

beta2 = [(Perte_2[i]/L-mu*Vitesse_2[i]/k_2_hr)*1/(rho*Vitesse_2[i]**2) for i in range(5,len(Vitesse_2))]

conduc_2 = k_2_br*rho*g/mu
print('Conductivité du milieu 2 K2 = ',conduc_2)

# Perte 3
coef3 = np.polyfit((Vitesse_3[5:]),(Perte_3[5:]),2)

k_3_hr = mu/coef3[1]
print('Perméabilité du milieu 3 k_3 = ',k_3_hr)

# idem bas reynolds

coef3 = np.polyfit((Vitesse_3[:6]),(Perte_3[:6]),2)

k_3_br = mu/coef3[1]
print('Perméabilité du milieu 3 br k_3 = ',k_3_br)

beta3 = [(Perte_3[i]/L-mu*Vitesse_3[i]/k_3_hr)*1/(rho*Vitesse_3[i]**2) for i in range(5,len(Vitesse_3))]

conduc_3 = k_3_br*rho*g/mu
print('Conductivité du milieu 3 K3 = ',conduc_3)

# Plot
plt.figure(3)
plt.plot(Re[5:],beta1,'r-',label='beta 1')
plt.plot(Re[5:],beta2,'b-',label='beta 2')
plt.plot(Re[5:],beta3,'g-',label='beta 3')
plt.xlabel('Re')
plt.ylabel('beta')
plt.legend()

k_1 = np.mean([k_1_hr,k_1_br])
k_2 = np.mean([k_2_hr,k_2_br])
k_3 = np.mean([k_3_hr,k_3_br])

# Conductivité et perméabilité équivalente

#parallèle
k_para = (k_1 + k_2 + k_3)/3
print('Perméabilité parallele = ',k_para)
K_para = k_para*rho*g/mu
print('Conductivité parallele = ',K_para)

#orthogonal
k_ortho = 3/(((1/k_1)+(1/k_2)+(1/k_3)))
print('Perméabilité orthogonal = ',k_ortho)
K_ortho = k_ortho*rho*g/mu
print("Conductivité orthogonal = ",K_ortho)


#plt.show()



u_3 = 0.00444117
u_1 = 0.0011750

