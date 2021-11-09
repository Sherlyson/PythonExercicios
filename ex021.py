from pydub import AudioSegment
from pydub.playback import play
musica = 'ex021.mp3'
musica = AudioSegment.from_mp3(musica)
play(musica)
