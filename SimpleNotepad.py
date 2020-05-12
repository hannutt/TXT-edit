from tkinter import *
from tkinter import filedialog #tuodaan tiedostodialogi toiminnallisuus
from tkinter import messagebox #tuodaan messagebox-toiminnallisuus
from tkinter.font import Font #tuodaan fonttikirjasto

def tallennaTxt(): #Luodaan funktio, jolla tallennetaan kirjoitettu teksti.
    
    file = filedialog.asksaveasfilename() #file-muuttujaan tallennetaan tiedostolle annettava nimi. avaus ja tallentaminen
                                         #tapahtuu windows-käyttöjärjestelmän vakio-dialogeissa, joka on toteutettu
                                         #filedialog kirjastolla.
    
    
    tiedosto = open(file,'w')#Avataan tiedosto, jonka nimi on file-muuttujan syötetty tiedostonimi. w-kirjaimella
                             #kerrotaan, että tallennus tehdään tekstimuodossa ja korvataan mahdollinen vanha sisältö.   
    teksti = tekstikentta.get('1.0','end-1c') #tallennetaan muuttujaan tekstikentän teksti ensimmäisestä kirjaimesta viimeiseen.
    tiedosto.write(teksti)                    #Kirjoitetaan teksti tiedostoon.
    
    messagebox.showinfo('Tallennus','Tiedosto on tallennettu!') #näytetään ilmoitus erillisessä ikkunassa
    #kun tiedosto on tallennettu onnistuneesti.
    tiedosto.close #suljetaan tiedosto.

def avaaTxt(): #Luodaan funktio, jolla voidaan avata olemassaoleva tekstitiedosto.
    haettava = filedialog.askopenfilename(initialdir = 'C:\\',) #haettava muuttujaan tallennetaan avattavan tiedoston nimi,
    #initialdir komennolla asetetaan oletussijainniksi c-levy.
    
    tiedosto = open(haettava, encoding = 'utf-8')#avataan tiedosto ja käytetään siinä encoding komennolla utf-8 merkistökoodausta.
    tekstikentta.insert('1.0', tiedosto.read())#näytetään tiedoston teksti sisältö tekstikenttä laatikossa.
    tiedosto.close

    
    

ikkuna = Tk()
ikkuna.geometry('250x250') #määritellään käyttöliittymäikkunan kooksi 250 * 250 pikseliä.
ikkuna.configure(background = 'slate gray') #määritellään ikkuna-komponentin taustaväri.
ikkuna.title('TXT-editor 1.0') #annetaan ikkunassa näkyvä otsikko.

tallenna = PhotoImage(file = 'NotepadSave.png') #tuodaan png-kuvat ohjelmaan, joita käytetään kuvakkeina ohjelman pudotus
#valikossa.
tallennus = tallenna.subsample(4,4)

avaa = PhotoImage(file = 'NotepadOpen.png') 
avaatiedosto = avaa.subsample(4,4)

#luodaan alasvetovalikko
valikko = Menu(ikkuna) 
ikkuna.config(menu=valikko)
toiminnot = Menu(valikko)

#annetaan alasvetovalikon otsikkoteksti eli functions
valikko.add_cascade(label = 'Functions', menu = toiminnot)

#Lisätään alasvetovalikkoon toimintoja. command komennolla lisätään funktiot, jotka suoritetaan jos toiminto valitaan.
#image komennolla tuodaan kuvatiedosto tekstin yhteyteen, joka asetetaan compound komennolla tekstin oikealle puolelle.
toiminnot.add_command(label = 'Save', command = tallennaTxt, image = tallennus, compound = RIGHT)

toiminnot.add_command(label = 'Load', command = avaaTxt, image = avaatiedosto, compound = RIGHT) 


#tallenetaan muuttujaan georgia fontti koossa 11, jota käytetään ohjelman otsikossa.
otsikkofontti = Font(family = 'Georgia', size = 11) 


rullauspalkki = Scrollbar(ikkuna) #luodaan rullauspalkki ohjelmaan.
rullauspalkki.pack(side = RIGHT, fill = Y) #asemoidaan rullauspalkki oikealle, fill komennolla kerrotaan rullaussuunta.


#luodaan label-komennolla tekstikomponentti. text-komennolla annetaan komponentissa näkyvä teksti, background
#komennolla komponentin taustaväri ja font komennolla käytettävä fontti.
ohjnimi = Label(ikkuna, text = 'Txt-editor', background = 'white smoke', font = otsikkofontti, relief = 'solid')


#luodaan tekstikentta niminen tekstilaatiko, width ja height komennoilla määritellään sen koko.
tekstikentta = Text(ikkuna, width = 40, height = 10, borderwidth = 2, relief = 'sunken', yscrollcommand = rullauspalkki.set)
rullauspalkki.config (command = tekstikentta.yview)

alaosa = Label(ikkuna, background = 'slate gray')





ohjnimi.pack(pady=2) #pakataan luodut komponentit, jolloin ne näkyvät ohjelmassa.
tekstikentta.pack()
alaosa.pack()
mainloop()

    

