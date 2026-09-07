#Import
import whisper
import subprocess
import sys



#Fonction pour convertir le temps
def convertTime(secBrut):
    h = int(secBrut / 3600)
    secBrut = secBrut % 3600

    m = int(secBrut / 60)
    secBrut = secBrut % 60

    s = int(secBrut)

    ms = int((secBrut - s)*1000)

    timecode = f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

    return timecode



#Petite vérification
if len(sys.argv) < 4:
    print("Erreur : Il manque des paramètres")
    print("Utilisation : python3 main.py 'vidéo_source' 'vidéo_sortie' 'modèle'")
    sys.exit()




#Les vidéos d'entrée et de sortie
source = sys.argv[1]
sortie = sys.argv[2]
model = sys.argv[3]


#Importation du modèle
model = whisper.load_model(model)
print("Le modèle est prêt")




#Transcription de l'audio en texte
out = model.transcribe(source)
if len(out["segments"]) == 0:
    print("Erreur : Aucune parole détectée dans la vidéo.")
    sys.exit()




#Fonction pour créer le fichier .srt
with open("subtitles.srt", "w", encoding="utf-8") as f:
    for segment in out["segments"]:
        id = segment["id"] + 1
        timeStart = convertTime(segment["start"])
        timeEnd = convertTime(segment["end"])

        text = f"{id}\n{timeStart} --> {timeEnd}\n{segment['text'].strip()}\n\n"
        f.write(text)





#Utilisation de FFmpeg
commande = ["ffmpeg", "-y", "-i", source, "-vf", "subtitles=subtitles.srt", sortie]
subprocess.run(commande)