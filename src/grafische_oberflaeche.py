from tkinter import *
from tkinter import ttk


class Model:

    def __init__(self) -> None:
        self.on_update = None
        self.geschwindigkeit = None
        self.reaktionsweg = None
        self.bremsweg = None
        self.anhalteweg = None

    def update_geschwindigkeit(self, geschwindigkeit):
        self.geschwindigkeit = geschwindigkeit
        self.reaktionsweg = (geschwindigkeit/10)*3
        self.bremsweg = (geschwindigkeit/10) * (geschwindigkeit/10)
        self.anhalteweg = self.reaktionsweg + self.bremsweg
        if self.on_update:
            self.on_update(self)

class View:

    def __init__(self, model:Model) -> None:
        self.on_click = None
        self.tkFenster = None
        self.model = model
        self.model.on_update = self.on_model_udate
        self.entryGeschwindigkeit = None
        self.labelWertReaktionsweg = None
        self.labelWertBremsweg = None
        self.labelWertAnhalteweg = None
        self.createUI()

    def on_model_udate(self, model):
        anzeigeReaktionsweg = '{0:.2f}'. format(model.reaktionsweg)
        self.labelWertReaktionsweg.config(text=anzeigeReaktionsweg)
        anzeigeBremsweg = '{0:.2f}'. format(model.bremsweg)
        self.labelWertBremsweg.config(text=anzeigeBremsweg)
        anzeigeAnhalteweg = '{0:.2f}'. format(model.anhalteweg)
        self.labelWertAnhalteweg.config(text=anzeigeAnhalteweg)


    def delegate_on_click(self):
        if self.on_click:
            self.on_click()

    def createUI(self):
        # Erzeugung des Fensters
        self.tkFenster = Tk()
        self.tkFenster.title('Anhalteweg')
        self.tkFenster.geometry('300x287')
        # Rahmen für die Überschrift
        frameUeberschrift = Frame(master=self.tkFenster,
                                background='#889E9D')
        frameUeberschrift.place(x=5, y=5, width=290, height=45)
        # Rahmen für die Eingaben
        frameEingaben = Frame(master=self.tkFenster,
                            background='#D5E88F')
        frameEingaben.place(x=5, y=55, width=290, height=72)
        # Rahmen für die Verarbeitung
        frameVerarbeitung = Frame(master=self.tkFenster,
                                background='#FBD975')
        frameVerarbeitung.place(x=5, y=132, width=290, height=44)
        # Rahmen für die Ausgaben
        frameAusgaben = Frame(master=self.tkFenster,
                            background='#FFCFC9')
        frameAusgaben.place(x=5, y=181, width=290, height=101)
        # Label für die Überschrift
        labelUeberschrift = Label(master=frameUeberschrift,
                                background='white',
                                text='Anhalteweg eines Autos')
        labelUeberschrift.place(x=50, y=12, width=190, height=20)
        # Label mit Aufschrift Geschwindigkeit
        labelGeschwindigkeit = Label(master=frameEingaben,
                                    background='white',
                                    text='Geschwindigkeit [in km/h]')
        labelGeschwindigkeit.place(x=10, y=10, width=175, height=20)
        # Entry für die Geschwindigkeit
        self.entryGeschwindigkeit = Entry(master=frameEingaben)
        self.entryGeschwindigkeit.place(x=210, y=10, width=60, height=20)
        # Label mit Aufschrift geschätzter Anhalteweg
        labelGeschaetzterAnhalteweg = Label(master=frameEingaben,
                                            background='white',
                                            text='geschätzer Anhalteweg [in m]')
        labelGeschaetzterAnhalteweg.place(x=10, y=40, width=175, height=20)
        # Entry für den geschätzten Anhalteweg
        entryGeschaetzterAnhalteweg = Entry(master=frameEingaben)
        entryGeschaetzterAnhalteweg.place(x=210, y=40, width=60, height=20)
        # Button Berechnen
        buttonBerechnen = Button(master=frameVerarbeitung,
                                text='berechnen',
                                command=self.delegate_on_click)
        buttonBerechnen.place(x=95, y=12, width=100, height=20)
        # Label mit Aufschrift Reaktionsweg
        labelReaktionsweg = Label(master=frameAusgaben,
                                background='white',
                                text='Reaktionsweg [in m]')
        labelReaktionsweg.place(x=10, y=10, width=175, height=20)
        # Label für den Wert des Reaktionswegs
        self.labelWertReaktionsweg = Label(master=frameAusgaben,
                                    background='white',
                                    text='')
        self.labelWertReaktionsweg.place(x=210, y=10, width=60, height=20)
        # Label mit Aufschrift Bremsweg
        labelBremsweg = Label(master=frameAusgaben,
                            background='white',
                            text='Bremsweg [in m]')
        labelBremsweg.place(x=10, y=40, width=175, height=20)
        # Label für den Wert des Bremswegs
        self.labelWertBremsweg = Label(master=frameAusgaben,
                                background='white',
                                text='')
        self.labelWertBremsweg.place(x=210, y=40, width=60, height=20)
        # Label mit Aufschrift Anhalteweg
        labelAnhalteweg = Label(master=frameAusgaben,
                                background='white',
                                text='Anhalteweg [in m]')
        labelAnhalteweg.place(x=10, y=70, width=175, height=20)
        # Label für den Wert des Anhaltewegs
        self.labelWertAnhalteweg = Label(master=frameAusgaben,
                                    background='white',
                                    text='')
        self.labelWertAnhalteweg.place(x=210, y=70, width=60, height=20)

    def get_geschwindigkeit(self):
        return self.entryGeschwindigkeit.get()

    def show(self):
        # Aktivierung des Fensters
        self.tkFenster.mainloop()

    def set_on_click(self, delegate):
        self.on_click = delegate

class Controller:

    def __init__(self, model:Model, view:View) -> None:
        self.model = model
        self.view = view

    def berechnen(self):
        geschwindigkeit = self.view.get_geschwindigkeit()
        self.model.update_geschwindigkeit(geschwindigkeit)

class Application:

    def run(self):
        model = Model()
        view = View(model=model)
        controller = Controller(model=model, view=view)
        view.show()


# application = Application()
# application.run()

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()



