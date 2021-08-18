#*******************************************************************************
#* INTERFACE GRAFICA DE ADQUISICION DE DATOS
#* DESARROLLADOR: Necrovalle
#* VERSION: 0.1alpha
#* REPOSITORIO:
#* <URL de gitHub>
#*******************************************************************************

#*********************************************************************** MODULOS
from tkinter import *		# Widgets estandar
from tkinter import ttk		# Widgets nuevos del 8.5+
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#************************************************************ VARIABLES GLOBALES
x = [1,2,3]
y = [2,4,1]


#************************************************************** SCRIPT PRINCIPAL
window = Tk()
matplotlib.use("TkAgg")

#window.geometry('800x600')
window.resizable(False, False)
window.title('Data logger Arduino')

#Seccion de coneccion serial
grpCOMM = LabelFrame(window, text='Coneccion: ')
grpCOMM.grid(row=0, column=0, padx=5, pady=5,sticky='NS')
lbl1 = Label(grpCOMM, text='Puerto:')
lbl1.grid(row=0, column=0)
cmbCOMM = ttk.Combobox(grpCOMM, text='Seleccione el puerto')
cmbCOMM.grid(row = 0, column = 1, padx = (0, 5), pady = 5)
btnConect = Button(grpCOMM, text='conectar')
btnConect.grid(row=1, column=1, padx =(0, 5), pady=(0, 5), sticky = 'E')

#Seccion de archivo de salida
grpFile = LabelFrame(window, text='Guardar en: ')
grpFile.grid(row=1, column=0, padx=5, pady=5, sticky='NS')
lbl2 = Label(grpFile, text='Nombre: ')
lbl2.grid(row=0, column=0, sticky='E')
entNameF = Entry(grpFile)
entNameF.grid(row=0, column=1, padx=(0, 5), pady=5)
lbl3 = Label(grpFile, text='Ruta: ')
lbl3.grid(row=1, column=0, sticky='E')
entRutaF = Entry(grpFile)
entRutaF.grid(row=1, column=1, padx=(0,5), pady=(0,5))

#Seccion de Configuracion de adquisicion de datos
grpConf = LabelFrame(window, text='Configuracion: ')
grpConf.grid(row=0, column=1, padx=0, pady=5, sticky='NS')
lbl4 = Label(grpConf, text='Canales:')
lbl4.grid(row=0, column=0, sticky='E')
chkCH1 = Checkbutton(grpConf, text='Canal 1')
chkCH1.grid(row=1, column=0)
chkCH2 = Checkbutton(grpConf, text='Canal 2')
chkCH2.grid(row=2, column=0)
chkCH3 = Checkbutton(grpConf, text='Canal 3')
chkCH3.grid(row=3, column=0)
chkCH4 = Checkbutton(grpConf, text='Canal 4')
chkCH4.grid(row=4, column=0)
lbl5 = Label(grpConf, text='Nombres:')
lbl5.grid(row=0, column=1)
entCHN1 = Entry(grpConf)
entCHN1.grid(row=1, column=1, padx=(0,5))
entCHN2 = Entry(grpConf)
entCHN2.grid(row=2, column=1, padx=(0,5))
entCHN3 = Entry(grpConf)
entCHN3.grid(row=3, column=1, padx=(0,5))
entCHN4 = Entry(grpConf)
entCHN4.grid(row=4, column=1, padx=(0,5), pady=(0,5))

#Seccion de control de flujo de datos
grpCTRL = LabelFrame(window, text='Controles: ')
grpCTRL.grid(row=1, column=1, padx=0, pady=5, sticky='NS')
btnUPF = Button(grpCTRL, text='Subir')
btnUPF.grid(row=0, column=1)
lbl6 = Label(grpCTRL, text='Samples/S')
lbl6.grid(row=1, column=1)
btnDNF = Button(grpCTRL, text='Bajar')
btnDNF.grid(row=2, column=1)
btnACN = Button(grpCTRL, text='Iniciar')
btnACN.grid(row=3, column=0, padx=5, pady=5)
btnPAUS = Button(grpCTRL, text='Pausa')
btnPAUS.grid(row=3, column=2,padx=5, pady=5)

#Seccion de grafica de datos
grpPlot = LabelFrame(window, text='Grafica: ')
grpPlot.grid(row=0, column=2, padx=5, pady=5, rowspan=2, columnspan=2, sticky='wens')
figure = Figure(figsize=(5, 4), dpi=100)
plt = figure.add_subplot(1, 1, 1)
#plt = figure.add_splot()  esta mal
plt.plot(x, y)
#plt.xlabel('x - axis')
#plt.ylabel('y - axis')
#plt.title('My first graph!')
canvas = FigureCanvasTkAgg(figure, grpPlot)
canvas.get_tk_widget().grid(row=0, column=0, padx=5, pady=5)



window.mainloop()

#****************************************************************** FIN DE SCRIPT

