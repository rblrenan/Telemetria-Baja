"""
  BAJA UFSCar - 2021
  Eletrônica - Renan - André - Jack - Paloma

  Telemetria - Data Visualisation

  Descrição: Visualização de dados fornecidos pela Serial da placas Arduino envolvidos no projeto.

  Em curso: fornecimento de gráficos dos dados dos sensores do carro.

  Próxima etapa: Realizar simulações com os sensores e através da comunicação LORAWAN.

"""
import serial as sr
import matplotlib.pyplot as plt
import time

leitura = []
eixo_x = 120
#  eixo_x0 = -30
fig, ax = plt.subplots()


def set_graficos():
    #  Gráfico 1: Temperatura do CVT
    #  plt.subplot(311)
    plt.style.use('fivethirtyeight')
    plt.title('Temperatura do CVT', fontsize=18, loc='left', fontweight='black')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Temperatura(ºC)')
    plt.axis([-30, eixo_x, -5, 80])
    plt.grid(True)


'''def axis(eixo_x0=eixo_x01, eixo_x=eixo_x1):
    while True:
        time.sleep(1)
        eixo_x0 += 1
        eixo_x += 1
        plt.axis([eixo_x0, eixo_x, -5, 80])'''


def telemetria(p_serial):  # Função de leitura de dados da serial
    i = 0
    arduino = sr.Serial(p_serial, 115200)
    while True:
        while arduino.inWaiting() == 0:
            ax.clear()
            ax.set_xlim(0, eixo_x)
            ax.set_ylim(0, 1023)
            y = str(arduino.readline())
            y = int(y[2:-5])
            leitura.append(y)
            set_graficos()
            ax.plot(leitura, label='Temperatura (ºC)', color='reddark')
            plt.legend()
            plt.pause(.00000001)
            i += 1
            if i > eixo_x:
                #  dados_antigos.append(leitura[0])
                leitura.pop(0)
        arduino.close()


telemetria('COM4')
