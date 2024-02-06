#!/usr/bin/python3


frags = [
    """konserten""",
    """fritt inträde""",
    """någon""",
    """dum ursäkt""",
    """inte bara""",
    """ser bra ut""",
    """sportig""",
    """dö""",
    """nyfikenheten""",
    """kapplöpningen""",
    """bitit""",
    """allvarligt/dåligt""",
    """du behöver""",
    """än"""]#,
  #  """att se, ser""",
  #  """jag ser""",
  #  """du ser""",
  #  """han/hon/den/det ser""",
  #  """vi ser""",
  #  """ni ser""",
  #  """de/Ni ser"""]


answs = ["""das Konzert""", """Eintritt frei""", """jemand""", """faule Ausrede (ausreden : snacka sig ur saker)""", """nicht nur""", """sieht gut aus""",
         """sportlich""", """sterben""", """die Neugier""", """der Wettlauf""", """gebissen""", """schlimm""", """du brauchst""", """als""",
         """sehen""", """ich sehe""", """du siehst""", """er/sie/es sieht""", """wir sehen""", """ihr seht""", """sie/Sie sehen"""]




frags = ["""idrottsplatsen""", """innebandy""", """med er""",
         """vinner vi""",
         """säkert""", """hela""", """här:biljetter""", """följer ni med?/Kommer ni med?""",
         """tyvärr""", """på fredagarna""", """alltid""", """senare på kvällen""", """på besök""", """Jag följer gärna med!""", """mobiltelefonen""", """ringer""", """Har du tid idag?""", """pianolektion""", """jag behöver""", """ytterligare""", """medspelare""", """tror jag""", """ingen aning""", """senare""", """då""", """Hej så länge!""", """dum, kass""", """frustrerad""", """snett""", """tappar""", """punktering""", """idrottslektion""", """på ögat""", """Tina tänker""", """aldrig mer""", """bråkar Tina""", """fortfarande""", """sur""", """Andrea pratar inte alls med, Andrea säger inget ord med""", """köpcentrum""", """verkligen""", """tillbaka""", """drar täcket över huvudet""", """det överlever jag aldrig""", """efter en sådan vecka""", """har jag inte alls någon lust längre"""]

answs = ["""der Sportplatz""", """das Hallenhockey""", """mit euch""", """gewinnen wir""", """bestimmt""","""ganz""", """Karten""", """Kommt ihr mit?""", """leider""", """freitags""", """immer""", """später am Abend""", """zu Besuch""", """Ich gehe gerne mit!""", """das Handy""", """klingelt""", """Hast due heute Zeit?""", """der Klavierunterricht""","""ich brauche""","""noch""", """Mitspieler""", """glaube ich""", """Keine Ahnung""", """später""", """dann""", """Bis nachher!""", """doof""", """gefrustet""", """schief""", """verliert""", """der Platten""", """der Sportunterricht""", """aufs Auge""", """Tina denkt""", """nie mehr""", """streitet Tina""", """immer noch""", """sauer""", """Andrea redet kein Wort mit""", """das Einkaufszentrum""", """echt / wirklich""", """zurück""", """zieht die Decke über den Kopf""", """das überlebe ich nie""", """nach so einer Woche""", """habe ich gar keine Lust mehr"""]




import numpy as np
import subprocess as sp
import os

def cls():
    os.system('cls||clear')

L = len(frags)
cls()
print(f"Är du redo för {L} heta tyskafrågor?")
input()
cls()

x = np.random.permutation(L)
#print(x)
cls()

m = dict()

l = 0
wordz = np.random.permutation(L)
while l < L:
    x = wordz[l]
    print(f"{x} [{100*(1+l)/L:2.0f}%] --> {frags[x]}")
    dot = sp.Popen(['python3','dot.py']) # ,f'{x}'])
    a = input()
    dot.kill()
    with open('tick.txt','r') as fid:
        lines = fid.readlines()
        line = float(lines[0])
        m[x] = line
    print(f"--> {answs[x]}")
    print(f" Enter: Nästa, b: tillbaka, r: tag om. ")
    b = input()
    cls()
    if b == "b":
        l = l - 1
        if l < 0:
            l = 0
        continue
    if b == "r":
        pass
    else:
        l = l + 1
        
# ---

tot = 0
for x in range(L):
    print(f"{(1+x):2f} ---> {m[x]:2f}\n", end="")
    tot = tot + float(m[x])
print(f"Totalt antal sekunder: {tot}.")

import matplotlib.pyplot as plt
import numpy as np
mm = [m[key] for key in m]
plt.plot(list(range(L)), mm,'k--',linewidth=3)
plt.plot(list(range(L)), np.cumsum(mm),'b-',linewidth=4)
plt.text(L, 1+np.cumsum(mm)[-1],f'Tot: {tot}s', ha="right", fontsize=16)
plt.title('Vi har ett resultat!')
plt.xlabel('Fråga')
plt.ylabel('Tid')

for x in range(L):
    plt.text(x,np.cumsum(mm)[x],frags[x],va="top", fontsize=8, rotation=-70)

plt.ylim([-1, np.cumsum(mm)[-1]+1])
    


plt.show()

"""
Urlaub
meine Eltern
Freundin
Ich mache Urlaub
endlich
schlafen
das Wetter
auch nicht
den ganzen Tag
Luftmatratze
Loch
zusammen
echt eng
wir müssen ... reparieren
Tischtennis
mit ein paar netten Jungs
Sehen auch noch gut aus
Regen
bei
nach drei Stunden
wirklich
langweilig
einkaufen gehen
das ganze Zelt
nass
Schlafsack
zum Glück
scheint die Sonne
wieder
dann können wir ... alles trocknen
vielleicht
treffen wir
heiss
nach Stuttgart zurück morgen
beginnt die Schule wieder
auf jeden Fall
die Englischstunde
die grosse Pause
auf dem Schulhof
treffen sich
einige
Schüler
planen
Nachmittag
neue Fruende
Zwillinge
Parallelklasse
Was macht ihr?
nach der Schule
Schwimmbad
Warum nicht?
Heute ist ja eine Affenhitze
Wann treffen wir uns?
wie viele Stunden
noch
am Eingang
vor
warten
schon
denn
Entschuldigung
verspätet
schon okay
gehen wir hinein?
sofort
Regeln
Spieler
Mannschaft
Punkte
Los geht's
zuerst
aufwärmen
Ratet!
jede Mannschaft
gut geraten
dürfen
sogar
auf dem Feld
Wie lange dauert
viermal zwölf
Toll!
laufen
Jetzt
fangen wir an
ich habe ... vergessen
zu zweit
setz dich
neben
wir lösen
Aufgabe
Wer möchte an die Tafel
ich verstehe
Bei der Klammer
genau
"""
