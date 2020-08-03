from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_file('data/NISSAN/accompaniment.wav')

beginning = sound[:5000]
end = sound[-15000:-10000]
play(beginning)
play(end)

with_style = beginning.append(end, crossfade=1500)
play(with_style)

awesome = with_style.fade_in(2000).fade_out(3000)
play(awesome)
