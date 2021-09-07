import serial
import time
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

def procurarletra(linha,letra): #search letter in line and return a value after the word or -1 if dont find the letter
        cond1=0
        cond2=0
        cond3=0
        for l in linha:
                if l=="'":
                        cond3=1
                if cond1 == 1 and (l == ' ' or l == '\n' or l == '\r' or l=="\\") and cond3==1:
                        cond2 = 1
                if cond1 == 1 and cond2 == 0 and cond3==1:
                        try:
                                num = num + l
                        except UnboundLocalError:
                                num = l
                if l == letra and cond3==1:
                        cond1 = 1
                        
        if cond1 == 1:
                return float(num)
        if cond1 == 0:
                return -1000


def procurarletra2(linha,letra): 
        cond1=0
        cond2=0
        for l in linha:
                if cond1 == 1 and ( l == '\n' or l == '\r' or l=="\\"):
                        cond2 = 1
                if cond1 == 1 and cond2 == 0:
                        try:
                                num = num + l
                        except UnboundLocalError:
                                num = l
                if l == letra:
                        cond1 = 1
        if cond1 == 1:
                return str(num)
        if cond1 == 0:
                return -1




def gravar(arquivo,diretorio): 
        file = open (diretorio, 'a+')
        file.write(arquivo+'\n')
        file.close()

        
now = datetime.now()
dt_string = now.strftime("%d-%m-%Y_%H-%M-%S.dat")


s = serial.Serial('COM10',115200)
time.sleep(10)


i=0
y1=[]
y2=[]
y3=[]
y4=[]
y5=[]
x=[]

plt.ion()
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, gridspec_kw={'left': 0.05,'bottom': 0.07,'right': 0.98,'top': 0.96,'wspace': 0.15,'hspace': 0.30})
ax1.set_title('Rotação')
ax1.set_xlabel('Tempo [s]')
ax1.set_ylabel('Rotação [rpm]')

ax2.set_title('Velocidade')
ax2.set_xlabel('Tempo [s]')
ax2.set_ylabel('Velocidade [km/h]')

ax3.set_title('Temperatura da CVT')
ax3.set_xlabel('Tempo [s]')
ax3.set_ylabel(r'Temperatura [$^{o}$C]')

ax4.set_title('Pressão nas vias')
ax4.set_xlabel('Tempo [s]')
ax4.set_ylabel('Pressão [MPa]')


f = open(dt_string,'w+')
f.close()
while True:
        cond=1;
        s.flushInput()
        out = str(s.readline())
        try:
                outprint=procurarletra2(out,"'")
        except:
                cond=0
        
        try:
                out1 = procurarletra(out,'r')
        except:
                cond=0
        
        
        try:
                out2 = procurarletra(out,'v')
        except:
                cond=0
        

        try:
                out3 = procurarletra(out,'t')
        except:
                cond=0
        

        try:
                out4 = procurarletra(out,'p')
        except:
                cond=0
        

        try:
                out5 = procurarletra(out,'m')
        except:
                cond=0

        if cond==1 and out1>-1000 and out2>-1000 and out3>-1000 and out4>-1000 and out5>-1000:
                print(outprint)
                gravar(outprint,dt_string)
                y1.append(int(out1))
                y2.append(int(out2))
                y3.append(int(out3))
                y4.append(int(out4))
                y5.append(int(out5))
                x.append(i)
                ax1.plot(x,y1,'b')
                ax2.plot(x,y2,'b')
                ax3.plot(x,y3,'b')
                ax4.plot(x,y4,'b')
                ax4.hold
                ax4.plot(x,y5,'r')
                ax4.legend(['Dianteira','Traseira'],loc=2)
                if i>=10:
                        ax1.set_xlim(i-60,i)
                        ax2.set_xlim(i-60,i)
                        ax3.set_xlim(i-60,i)
                        ax4.set_xlim(i-60,i)
                i=i+1
                plt.show()
                plt.pause(0.0001)
        









