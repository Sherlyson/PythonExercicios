from time import sleep
from pydub import  AudioSegment
from pydub.playback import play
for c in range(10, -1, -1):
    print(c)
    sleep(1)
musica = 'ex046.mp3'
musica = AudioSegment.from_mp3(musica)
play(musica)