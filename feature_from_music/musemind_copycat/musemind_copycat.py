import csv
from pathlib import Path

import moviepy.editor as mpe
from pydub import AudioSegment

### init
FADING_TIME = 300
base_path = Path('musemind_copycat/data/')
dir_list = [d for d in base_path.iterdir() if d.is_dir()]

for dir_path in dir_list:
    print(dir_path)

    ### csv
    csv_path = [f for f in dir_path.iterdir() if f.suffix == '.csv'][0].as_posix()
    csv_file = open(csv_path, 'r')
    reader = csv.reader(csv_file)
    next(reader)
    pydub_times = []
    for line in reader:
        if set(line[0]) == {';'}:
            continue
        stripped_times = line[0].split(';')
        cut_times = stripped_times[:2]
        start = int(cut_times[0].split(':')[-2]) * 1000 + int(cut_times[0].split(':')[-1]) * 10
        end = int(cut_times[1].split(':')[-2]) * 1000 + int(cut_times[1].split(':')[-1]) * 10
        pydub_times.append((start, end))

    ### handle small and adjacent shots
    i = 0
    filtered_times = []
    while i < len(pydub_times):
        start_index = i
        while i + 1 < len(pydub_times) and pydub_times[i + 1][0] - pydub_times[i][1] < 11:
            i += 1
        start, end = pydub_times[start_index][0], pydub_times[i][1]
        filtered_times.append((start, end))
        i += 1

    ### song
    sound_path = [f for f in dir_path.iterdir() if f.suffix == '.mp4' and 'short' not in f.as_posix()][0].as_posix()
    sound = AudioSegment.from_file(sound_path)
    awesome = sound[filtered_times[0][0]:filtered_times[0][1]]
    for start, end in filtered_times[1:]:
        awesome.append(sound[start:end], crossfade=FADING_TIME)
    awesome.fade_out(FADING_TIME)
    # play(awesome)
    awesome.export((dir_path / 'awesome.mp3').as_posix(), format='mp3')

    ### video
    video_path = [f for f in dir_path.iterdir() if f.suffix == '.mp4' and 'short' in f.as_posix()][0].as_posix()
    video = mpe.VideoFileClip(video_path)
    # final_audio = mpe.CompositeAudioClip([video.audio, audio])  ### to add ambiance sound to original sound
    audio = mpe.AudioFileClip((dir_path / 'awesome.mp3').as_posix())
    video_with_audio = video.set_audio(audio)
    video_with_audio.write_videofile((dir_path / 'short_result.mp4').as_posix(),
                                     codec='libx264',
                                     audio_codec='aac',
                                     temp_audiofile='temp-audio.m4a',
                                     remove_temp=True)
