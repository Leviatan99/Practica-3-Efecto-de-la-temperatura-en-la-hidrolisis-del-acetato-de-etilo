import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
# Funciones necesarias

def alineal(x,y):
  n =  len(x)
  x2 = x**2
  y2 = y**2
  xy = x*y
  sx = sum(x)
  sy = sum(y)
  sxy = sum(xy)
  sx2 = sum(x2)
  sy2 = sum(y2)
  r = ( n*sxy - ( sx*sy ))/ math.sqrt((n*(sx2)-sx**(2))*(n*(sy2)-sy**(2)))
  regresion = np.polyfit(x,y,1)
  m = regresion[0]
  b = regresion[1]
  r2 = r**2
  salida = [m,b,r2]
  return salida

def k(c):
    kelvin = c + 273
    return kelvin


#Importar datos de excel

data_frame = 'Practica_3.xlsx'
data1 = pd.read_excel(data_frame)
data_frame2 = 'calibracion.xlsx'
calibracion_data  = pd.read_excel(data_frame2)
#print(head(data1)
# Calculos de calibracion

regresion_calibracion30 = alineal(calibracion_data.CA030,calibracion_data.S030)
mc30 = regresion_calibracion30[0]
bc30 = regresion_calibracion30[1]
rc30 = regresion_calibracion30[2]
vector_calibracion30 = (calibracion_data.CA030*mc30) + bc30

regresion_calibracion35 = alineal(calibracion_data.CA035,calibracion_data.S035)
mc35 = regresion_calibracion35[0]
bc35 = regresion_calibracion35[1]
rc35 = regresion_calibracion35[2]
vector_calibracion35 = (calibracion_data.CA035*mc35) + bc35

regresion_calibracion40 = alineal(calibracion_data.CA040,calibracion_data.S040)
mc40 = regresion_calibracion40[0]
bc40 = regresion_calibracion40[1]
rc40 = regresion_calibracion40[2]
vector_calibracion40 = (calibracion_data.CA040*mc40) + bc40

regresion_calibracion45 = alineal(calibracion_data.CA045,calibracion_data.S045)
mc45 = regresion_calibracion45[0]
bc45 = regresion_calibracion45[1]
rc45 = regresion_calibracion45[2]
vector_calibracion45 = (calibracion_data.CA045*mc45) + bc45

#Para los calculos de la concentracion
concentracion30 = (data1.S30 - bc30 )/(mc30)
concentracion35 = (data1.S35 - bc35 )/(mc35)
concentracion40 = (data1.S40 - bc40 )/(mc40)
concentracion45 = (data1.S45 - bc45 )/(mc45)

# Para la  inversa de la concentracion
inversa_concentracion30 = 1 /concentracion30
inversa_concentracion35 = 1 /concentracion35
inversa_concentracion40 = 1 /concentracion40
inversa_concentracion45 = 1 /concentracion45

#Para la regresion de la concentracion
regresion_concentracion30 = alineal(data1.t30,inversa_concentracion30)
mC_30 = regresion_concentracion30[0]
bC_30 = regresion_concentracion30[1]
rC_30 = regresion_concentracion30[2]
vector_concentracion30 = (data1.t30*mC_30) + bC_30


regresion_concentracion35 = alineal(data1.t35,inversa_concentracion35)
mC_35 = regresion_concentracion35[0]
bC_35 = regresion_concentracion35[1]
rC_35 = regresion_concentracion35[2]
vector_concentracion35 = (data1.t35*mC_35) + bC_35


regresion_concentracion40 = alineal(data1.t40,inversa_concentracion40)
mC_40 = regresion_concentracion40[0]
bC_40 = regresion_concentracion40[1]
rC_40 = regresion_concentracion40[2]
vector_concentracion40 = (data1.t40*mC_40) + bC_40


regresion_concentracion45 = alineal(data1.t45,inversa_concentracion45)
mC_45 = regresion_concentracion45[0]
bC_45 = regresion_concentracion45[1]
rC_45 = regresion_concentracion45[2]
vector_concentracion45 = (data1.t45*mC_45) + bC_45

temperaturas = np.array([k(30),k(35),k(40),k(45)])
inversa_temperaturas = 1/temperaturas
constantes_k = np.array([mC_30,mC_35,mC_40,mC_45])
ln_constantes_k =  np.log(constantes_k)

regresion_k = alineal(inversa_temperaturas,ln_constantes_k)
mc_k = regresion_k[0]
bc_k = regresion_k[1]
rc_k = regresion_k[2]
vector_k = (inversa_temperaturas*mc_k) + bc_k


#Graficos Concentracion ---------------------------------------------------------
plt.figure('Ctodos')
plt.figure('Ctodos').set_size_inches(11, 10)
plt.subplot(2,2,1)
#plt.figure('C30')
plt.plot(data1.t30,inversa_concentracion30,'ob',label = 'Datos experimentales')
plt.plot(data1.t30,vector_concentracion30,':k',label = 'Ajuste Lineal')
#plt.axis([0,0.210,0,450])
plt.title('Concentración $ 30  C^{o}$ ')
plt.xlabel('Tiempo (min)')
plt.ylabel('1/Concentración ($M^{-1}$)')
ccord30 =  str("{0:.4f}".format(mC_30)) +'x + '+ str("{0:.4f}".format(bC_30)+'\n $r^{2} = $' + str("{0:.4f}".format(rC_30)))
plt.text(15,35,ccord30)
plt.legend()
plt.grid(True)
plt.savefig('C_30.pdf')

plt.subplot(2,2,2)
#plt.figure('C35')
plt.plot(data1.t35,inversa_concentracion35,'og',label = 'Datos experimentales')
plt.plot(data1.t35,vector_concentracion35,':k',label = 'Ajuste Lineal')
#plt.axis([0,0.210,0,450])
plt.title('Concentración $ 35  C^{o}$ ')
plt.xlabel('Tiempo (min)')
plt.ylabel('1/Concentración ($M^{-1}$)')
ccord35 =  str("{0:.4f}".format(mC_35)) +'x + '+ str("{0:.4f}".format(bC_35) +'\n $r^{2} = $' + str("{0:.4f}".format(rC_35)))
plt.text(15,40,ccord35)
plt.legend()
plt.grid(True)
plt.savefig('C_35.pdf')

plt.subplot(2,2,3)
#plt.figure('C40')
plt.plot(data1.t40,inversa_concentracion40,'or',label = 'Datos experimentales')
plt.plot(data1.t40,vector_concentracion40,':k',label = 'Ajuste Lineal')
#plt.axis([0,0.210,0,450])
plt.title('Concentración $ 40  C^{o}$ ')
plt.xlabel('Tiempo (min)')
plt.ylabel('1/Concentración ($M^{-1}$)')
ccord40 =  str("{0:.4f}".format(mC_40)) +'x '+ str("{0:.4f}".format(bC_40)+'\n $r^{2} = $' + str("{0:.4f}".format(rC_40)))
plt.text(15,40,ccord40)
plt.legend()
plt.grid(True)
plt.savefig('C_40.pdf')

plt.subplot(2,2,4)
#plt.figure('C45')
plt.plot(data1.t45,inversa_concentracion45,'oy',label = 'Datos experimentales')
plt.plot(data1.t45,vector_concentracion45,':k',label = 'Ajuste Lineal')
#plt.axis([0,0.210,0,450])
plt.title('Concentración $ 45  C^{o}$ ')
plt.xlabel('Tiempo (min)')
plt.ylabel('1/Concentración ($M^{-1}$)')
ccord45 =  str("{0:.4f}".format(mC_45)) +'x '+ str("{0:.4f}".format(bC_45)+'\n $r^{2} = $' + str("{0:.4f}".format(rC_45)))
plt.text(15,40,ccord45)
plt.legend()
plt.grid(True)
plt.savefig('C_45.pdf')
plt.savefig('Ctodos.pdf')




plt.figure('FiguraTodos')
plt.figure('FiguraTodos').set_size_inches(11, 10)
plt.subplot(2,2,1)
#Graficos
#plt.figure('calibracion_30')
plt.plot(calibracion_data.CA030,calibracion_data.S030,'ob',label = 'Datos experimentales')
plt.plot(calibracion_data.CA030,vector_calibracion30,':k',label = 'Ajuste Lineal')
plt.axis([0,0.210,0,450])
plt.title('Calibración $ 30  C^{o}$ ')
plt.xlabel('Concentración (M)')
plt.ylabel('Conductividad (mS)')
cord30 =  str("{0:.4f}".format(mc30)) +'x '+ str("{0:.4f}".format(bc30)+'\n $r^{2} = $' + str("{0:.4f}".format(rc30)))
plt.text(0.125,200,cord30)
plt.legend()
plt.grid(True)
#plt.savefig('calibracion_30.pdf')

plt.subplot(2,2,2)
#plt.figure('calibracion_35')
plt.plot(calibracion_data.CA035,calibracion_data.S035,'og',label = 'Datos experimentales')
plt.plot(calibracion_data.CA035,vector_calibracion35,':k',label = 'Ajuste Lineal')
#plt.axis([0,0.210,0,450])
plt.title('Calibración $ 35  C^{o}$ ')
plt.xlabel('Concentración (M)')
plt.ylabel('Conductividad (mS)')
cord35 =  str("{0:.4f}".format(mc35)) +'x + '+ str("{0:.4f}".format(bc35) +'\n $r^{2} = $' + str("{0:.4f}".format(rc35)))
plt.text(0.125,100,cord35)
plt.legend()
plt.grid(True)
#plt.savefig('calibracion_35.pdf')

plt.subplot(2,2,3)
#plt.figure('calibracion_40')
plt.plot(calibracion_data.CA040,calibracion_data.S040,'or',label = 'Datos experimentales')
plt.plot(calibracion_data.CA040,vector_calibracion40,':k',label = 'Ajuste Lineal')
#plt.axis([0,0.210,0,250])
plt.title('Calibración $ 40^{o} C$ ')
plt.xlabel('Concentración (M)')
plt.ylabel('Conductividad (mS)')
cord40 =  str("{0:.4f}".format(mc40)) +'x '+ str("{0:.4f}".format(bc40)+'\n $r^{2} = $' + str("{0:.4f}".format(rc40)))
plt.text(0.125,150,cord40)
plt.legend()
plt.grid(True)
#plt.savefig('calibracion_40.pdf')

plt.subplot(2,2,4)
#plt.figure('calibracion_45')
plt.plot(calibracion_data.CA045,calibracion_data.S045,'oy',label = 'Datos experimentales')
plt.plot(calibracion_data.CA045,vector_calibracion45,':k',label = 'Ajuste Lineal')
#plt.axis([0,0.210,0,250])
plt.title('Calibración $ 45^{o} C$ ')
plt.xlabel('Concentración (M)')
plt.ylabel('Conductividad (mS)')
cord45 =  str("{0:.4f}".format(mc45)) +'x + '+ str("{0:.4f}".format(bc45)+'\n $R^{2} = $' + str("{0:.4f}".format(rc45)))
plt.text(0.125,150,cord45)
plt.legend()
plt.grid(True)
#plt.savefig('calibracion_45.pdf')
#plt.suptitle("Curvas de calibración")
plt.savefig('FiguraTodos.pdf')
#Graficos extras





plt.figure('calibracion_todos')
plt.plot(calibracion_data.CA030,calibracion_data.S030,'-b',label = '$ 30^{o} C$')
plt.plot(calibracion_data.CA035,calibracion_data.S035,'-g',label = '$ 35^{o} C$')
plt.plot(calibracion_data.CA040,calibracion_data.S040,'-r',label = '$ 40^{o} C$')
plt.plot(calibracion_data.CA045,calibracion_data.S045,'-y',label = '$ 45^{o} C$')
#plt.axis([0,0.210,0,250])
plt.title('Calibración  de $ (30-45)^{o} C$ ')
plt.xlabel('Concentración (M)')
plt.ylabel('Conductividad (mS)')
plt.grid(True)
plt.legend()
plt.savefig('calibracion_todos.pdf')

plt.figure('concentracion_todos')
plt.plot(data1.t30,inversa_concentracion30,'-b',label = '$ 30^{o} C$')
plt.plot(data1.t35,inversa_concentracion35,'-g',label = '$ 35^{o} C$')
plt.plot(data1.t40,inversa_concentracion40,'-r',label = '$ 40^{o} C$')
plt.plot(data1.t45,inversa_concentracion45,'-y',label = '$ 45^{o} C$')
plt.title('Método integral orden $II$   ')
plt.xlabel('Tiempo (min)')
plt.ylabel('1/Concentración ($M^{-1}$)')
plt.grid(True)
plt.legend()
plt.savefig('concentracion_todos.pdf')

plt.figure('Conductividad_vs_Tiempo')
plt.plot(data1.t30,data1.S30,'-b',label = '$ 30^{o} C$')
plt.plot(data1.t35,data1.S35,'-g',label = '$ 35^{o} C$')
plt.plot(data1.t40,data1.S40,'-r',label = '$ 40^{o} C$')
plt.plot(data1.t45,data1.S45,'-y',label = '$ 45^{o} C$')
plt.title('Conductividad vs Tiempo, a diversas temperaturas')
plt.xlabel('Tiempo (min)')
plt.ylabel('Conductividad (mS)')
plt.grid(True)
plt.legend()
plt.savefig('Conductividad_vs_Tiempo.pdf')


#plt.figure(figsize=(6, 4.5))
plt.figure('ln_k_t')
plt.plot(inversa_temperaturas,ln_constantes_k,'om',label='Datos ')
plt.plot(inversa_temperaturas,vector_k,':k',label = 'Ajuste Lineal')
plt.title('Determinación de $A $ y $ E_a$')
plt.xlabel('Temperatura $^{-1}$ (K $^{-1}$ )')
plt.ylabel('$Ln(K)$')
plt.xticks(rotation=8)
cordk =  str("{0:.4f}".format(mc_k)) +'x + '+ str("{0:.4f}".format(bc_k)+'\n $r^{2} = $' + str("{0:.4f}".format(rc_k)))
plt.text(0.00322,1.05,cordk)
plt.grid(True)
plt.legend()
plt.savefig('ln_k_t.pdf')
