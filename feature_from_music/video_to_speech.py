from spleeter.audio.adapter import get_default_audio_adapter
from spleeter.separator import Separator

separator = Separator('spleeter:2stems')
audio_loader = get_default_audio_adapter()
separator.separate_to_file('data/NISSAN.mp4', 'data')
