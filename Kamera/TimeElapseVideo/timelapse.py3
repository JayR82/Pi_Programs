#!/usr/bin/python3

# Dieses Skript dient zur Erstellung von Zeitrafferaufnahmen mit dem Raspberry Pi.
# Das Skript speichert die Einzelbilder im Ordner des Skriptes und löscht vor dem aufnehmen neuer Bilder
# zunächst alle Bild Dateien mit gleichen Namen (Daran Denken !).
# Einstellschrauben sind die Variablen tl_name und die Einstellungen darunter.
# tl_name ist der Dateiname der Erzeugten Bilder, dort wird noch ein Zähler angehangen.
# Die Einstellung welche man benötigt testet man am besten vorher durch ausprobieren mit raspistill aus.

import os
import time
import subprocess
 
# Funktion zum löschen aller *.jpg Dateien die das Pattern enthalten.
def loeschen(path, pattern):
	for each in os.listdir(path):
		if (each.find(pattern) != -1 & each.find("jpg") != -1):
			name = os.path.join(path, each)
			try: 
				os.remove(name)
				print(name + " wurde gelöscht.")
			except:
				print("Löschen fehlgeschlagen")
				pass
	print("Alle Bilder erfolgreich gelöscht\n\n")
 
# Name für die Bilderreihe.
tl_name = 'Cobra11' 

# Kamera Einstellungen (siehe raspistill Manpage für genauere Infos).
photo_ex  = 'auto'
photo_awb = 'auto'
photo_effect = 'none'
#Exposure mode options :
#off,auto,night,nightpreview,backlight,spotlight,sports,snow,beach,verylong,fixedfps,antishake,fireworks
#AWB mode options :
#off,auto,sun,cloud,shade,tungsten,fluorescent,incandescent,flash,horizon
#Image Effect mode options :
#none,negative,solarise,sketch,denoise,emboss,oilpaint,hatch,gpen,pastel,watercolour,film,blur,saturation,colourswap,washedout,posterise,colourpoint,colourbalance,cartoon

# EV Level.
photo_ev = -5
 
# Auflösung und Qualität (max 2592 x 1944).
photo_width  = 2592
photo_height = 1944
photo_quality = 75

photo_sharpness = 50
photo_contrast = 10

# Intervall zwischen den Fotos (Sekunden).
# Tag in s    = 86400
# Stunde in s = 3600
# Minute in s = 60
# Beispiel: Intervall alle 3h 1x Bild => photo_interval = 3*3600
photo_interval = 20 # Sekunden

# Limitierung durch Anzahl der Bilder
total_photos =   0 # Anzahl Fotos Gesamt; 0 = Dauerlauf.



photo_counter  = 1    	# Foto Zähler.

# Alle eventuell vorhandenen gleichnamigen Bilder Löschen.
try:
  loeschen("./", tl_name)  
except OSError:
  print(OSError)
  pass
 
# Fotos machen!
try:
  print("Raspistill Einstellungen:")
  print("Dateinamen:" + tl_name)
  print("Exposure:" + photo_ex)
  print("AWB:" + photo_awb)
  print("Effekt:" + photo_effect)
  print("EV:" + str(photo_ev))
  print("Auflösung:" + str(photo_width) + "x" + str(photo_height))
  print("jpg Qualität:" + str(photo_quality))
  print("Zeitabstand Einzelbilder:" + str(photo_interval) + "s" + "(Auslösezeit der Kamera kommt dort noch hinzu. ca 250ms)")
  print("Anzahl Bilder:" + str(total_photos) + "\n\n")
  print("Fotoserie gestartet\n")
  
# Solange der Zähler noch nicht das Ende erreicht hat neue Fotos machen.
  while(photo_counter <= total_photos) or (total_photos == 0):      
      filename = (tl_name + "_%.4d.jpg"%photo_counter)
      cmd = ('raspistill -t 250 -w ' + str(photo_width) +
            ' -h ' + str(photo_height) +
            ' -q ' + str(photo_quality) +
            ' -sh ' + str(photo_sharpness) +
            ' -co ' + str(photo_contrast) +
            ' -awb ' + photo_awb +
            ' -ev ' + str(photo_ev) +
            ' -ex ' + photo_ex +
            ' -ifx ' + photo_effect +
            ' -o ' + filename)
      pid = subprocess.call(cmd, shell=True)
      
      # Berechnung der Verbleibenden Zeit.
#       rest_bilder = total_photos - photo_counter
#       rest_sekunden = rest_bilder * photo_interval
      
#      rest_zeit = rest_sekunden
#      einheit = " Sekunden"
#      if rest_sekunden > 86400:
#          rest_zeit = rest_sekunden/86400
#          einheit = " Tage"
#      elif rest_sekunden > 3600:
#          rest_zeit = rest_sekunden/3600
#          einheit = " Stunden"
#      elif rest_sekunden > 60:
#          rest_zeit = rest_sekunden/60
#          einheit = " Minuten"
#      # Statusmeldung ausgeben.
#      print(time.strftime("|--%d.%m.%Y - %H:%M:%S\n") + '|   [' +
#            str(photo_counter) + ' von ' +
#            str(total_photos) +
#            '] ' + filename + '   ' +
#            "%.2f"%rest_zeit + einheit + ' verbleibend\n|')
      time.sleep(photo_interval)
      photo_counter = photo_counter + 1
 
  print("Fotoserie beendet")
 
except KeyboardInterrupt:
  # Abbruch durch den Benutzer.
  print("\nAbgebrochen!")
