import functools

from pydub import AudioSegment
from pydub.playback import play


def strip_silence(sound, silence_threshold=-40.0, chunk_size=30):
    trim_list = [trim for trim in range(0, len(sound), chunk_size) if
                 sound[trim:trim + chunk_size].dBFS > silence_threshold]
    sound_list = [sound[trim_ms:trim_ms + chunk_size] for trim_ms in trim_list]
    stripped_sound = functools.reduce(lambda a, b: a + b, sound_list)
    return stripped_sound


sound = AudioSegment.from_wav('data/NISSAN/vocals.wav')

stripped_sound = strip_silence(sound)

play(stripped_sound)

stripped_sound.export('data/NISSAN/stripped_vocals.wav', format='wav')
