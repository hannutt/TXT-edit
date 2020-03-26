from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.font import Font

def tallennaTxt(): #Luodaan funktio, jolla tallennetaan kirjoitettu teksti.
    
    file = filedialog.asksaveasfilename() #file-muuttujaan tallennetaan kenttään kirjoitettu
    # tiedostolle annettu tiedostonnimi.
    
    tiedosto = open(file,'a')#Avataan tiedosto, jonka nimi file-muuttujan syötetty tiedostonimi.
    teksti = tekstikentta.get('1.0','end-1c') #tallennetaan muuttujaan tekstikentän teksti ensimmäisestä kirjaimesta viimeiseen.
    tiedosto.write(teksti) #Kirjoiteaan teksti tiedostoon.
    
    messagebox.showinfo('Tallennus','Tiedosto on tallennettu!') #näytetään ilmoitus, kun tiedosto on tallennettu onnistuneesti.
    tiedosto.close

def avaaTxt(): #Luodaan funktio, jolla voidaan avata olemassaoleva tekstitiedosto.
    haettava = filedialog.askopenfilename(initialdir = 'C:\\',) #haettava muuttujaan tallennetaan avattavan tiedoston nimi,
    #initialdir komennolla asetetaan oletussijainniksi c-levy.
    
    tiedosto = open(haettava, encoding = 'utf-8')#avataan tiedosto ja käytetään siinä encoding komennolla utf-8 merkistökoodausta.
    tekstikentta.insert('1.0', tiedosto.read())#näytetään tiedoston teksti sisältö tekstikenttä komponentissa.
    #laatikkoon.
    tiedosto.close

def info():
    messagebox.showinfo('Info','(C) Hannu Tuomela\n' #toiminnot valikon info valinnan klikkaamisen jälkeen näytettävä teksti
                        'Give feedback: htuomela@gmail.com\n'
                        'Made with Python 3.8')
    
    

ikkuna = Tk()
ikkuna.geometry('250x250') #määritellään käyttöliittymäikkunan kooksi 250 * 250 pikseliä.
ikkuna.configure(background = 'slate gray') #määritellään ikkuna-komponentin taustaväri.
ikkuna.title('TXT-editor 1.0') #annetaan ikkunassa näkyvä otsikko.

tallenna = PhotoImage(file = 'NotepadSave.png') #tuodaan tallennusikoni ohjelmaan ja määritellään käytettävät pikselit.
tallennus = tallenna.subsample(4,4)

avaa = PhotoImage(file = 'NotepadOpen.png') #tuodaan tiedoston avausikoni ohjelmaan ja määritellään käytettävät pikselit.
avaatiedosto = avaa.subsample(4,4)

valikko = Menu(ikkuna) #luodaan alasvetovalikko

ikkuna.config(menu=valikko)
toiminnot = Menu(valikko)
valikko.add_cascade(label = 'Toiminnot', menu = toiminnot)

toiminnot.add_command(label = 'Tallenna', command = tallennaTxt, image = tallennus, compound = RIGHT) #Lisätään alasvetovalikkoon tallennustoiminto,
#command komennolla lisätään siihen tallennatxt funktion toiminnallisuuus. image komennolla tuodaan NotepadSave.png kuvatiedosto
#tekstin yhteyteen, joka asetetaan compound komennolla tekstin oikealle puolelle.

toiminnot.add_command(label = 'Avaa', command = avaaTxt, image = avaatiedosto, compound = RIGHT) #lisätään avaustoiminto valikkoon.

toiminnot.add_command(label = 'Info', command = info) #lisätään info-toiminto valikkoon.

otsikkofontti = Font(family = 'Georgia', size = 11) #tallenetaan muuttujaan georgia fontti koossa 11, jota käytetään ohjelman otsikossa.


rullauspalkki = Scrollbar(ikkuna) #luodaan rullauspalkki ohjelmaan.
rullauspalkki.pack(side = RIGHT, fill = Y) #asemoidaan rullauspalkki oikealle.
ohjnimi = Label(ikkuna, text = 'Txt-editor', background = 'white smoke', font = otsikkofontti, relief = 'solid')
#luodaan label-tekstikenttä, jossa lukee tekstieditori ja käytetään aiemmin määriteltyä otsikkofonttia.
#taustavärinä white smoke väriä ja relief komennolla ympyröidään kentän reunat mustalla viivalla.

tekstikentta = Text(ikkuna, width = 40, height = 8, borderwidth = 2, relief = 'sunken', yscrollcommand = rullauspalkki.set)
#luodaan tekstilaatikko, ja lisätään siihen aiemmin luotu rullasuspalkki.

alaosa = Label(ikkuna, background = 'slate gray')

rullauspalkki.config (command = tekstikentta.yview)



ohjnimi.pack()
tekstikentta.pack()
alaosa.pack()
mainloop()

    

