import csv
from pathlib import Path

import moviepy.editor as mpe
from pydub import AudioSegment

BASE_PATH = Path('musemind_copycat/data/')
MIN_INTERVAL_SIZE = 500
FADING_TIME = 300


def main():
    dir_list = [d for d in BASE_PATH.iterdir() if d.is_dir()]

    for dir_path in dir_list:
        print(dir_path)
        # if 'club_med' not in dir_path.as_posix():
        #     continue
        shot_times = _read_shot_times_from_csv_and_convert_to_ms(dir_path)
        reduced_times = _reduce_adjacent_times(shot_times)
        filtered_times = _replace_too_small_intervals(reduced_times, MIN_INTERVAL_SIZE)
        _build_and_save_reduced_audio(dir_path, filtered_times)
        _merge_and_save_reduced_video_and_audio(dir_path)


def _read_shot_times_from_csv_and_convert_to_ms(dir_path):
    csv_path = [f for f in dir_path.iterdir() if f.suffix == '.csv'][0].as_posix()
    csv_file = csv.reader(open(csv_path, 'r'))
    next(csv_file)
    pydub_times = []
    for line in csv_file:
        if set(line[0]) == {';'}:
            continue
        stripped_times = line[0].split(';')
        cut_times = stripped_times[:2]
        start = int(cut_times[0].split(':')[-3]) * 60000 + \
                int(cut_times[0].split(':')[-2]) * 1000 + \
                int(cut_times[0].split(':')[-1]) * 10
        end = int(cut_times[1].split(':')[-3]) * 60000 + \
              int(cut_times[1].split(':')[-2]) * 1000 + \
              int(cut_times[1].split(':')[-1]) * 10
        pydub_times.append((start, end))
    return pydub_times


def _reduce_adjacent_times(pydub_times):
    i = 0
    filtered_times = []
    while i < len(pydub_times):
        start_index = i
        while i + 1 < len(pydub_times) and pydub_times[i + 1][0] - pydub_times[i][1] < 11:
            i += 1
        start, end = pydub_times[start_index][0], pydub_times[i][1]
        filtered_times.append((start, end))
        i += 1
    return filtered_times


def _replace_too_small_intervals(reduced_times, min_interval_size):
    filtered_times = []
    is_next_interval_small = False
    for start, end in reduced_times[::-1][:-1]:
        if is_next_interval_small:
            end += interval_size
        interval_size = end - start
        if interval_size < min_interval_size:
            is_next_interval_small = True
        else:
            filtered_times = [(start, end)] + filtered_times
            is_next_interval_small = False
    start, end = reduced_times[0]
    if end - start < min_interval_size:
        filtered_times[0] = filtered_times[0][0] - (end - start), filtered_times[0][1]
    return filtered_times


def _build_and_save_reduced_audio(dir_path, filtered_times):
    full_video_path = [f for f in dir_path.iterdir() if f.suffix == '.mp4' and 'result' not in f.as_posix()
                       and 'short' not in f.as_posix()][0].as_posix()
    audio = AudioSegment.from_file(full_video_path)
    reduced_audio = audio[filtered_times[0][0]:filtered_times[0][1]]
    for start, end in filtered_times[1:]:
        reduced_audio = reduced_audio.append(audio[start:end], crossfade=FADING_TIME)
    reduced_audio.export((dir_path / 'reduced_audio.mp3').as_posix(), format='mp3')


def _merge_and_save_reduced_video_and_audio(dir_path):
    video_path = (dir_path / 'short.mp4').as_posix()
    video = mpe.VideoFileClip(video_path)
    audio = mpe.AudioFileClip((dir_path / 'reduced_audio.mp3').as_posix())
    video_with_audio = video.set_audio(audio)
    video_with_audio.write_videofile((dir_path / 'result.mp4').as_posix(),
                                     codec='libx264',
                                     audio_codec='aac',
                                     temp_audiofile='temp-audio.m4a',
                                     remove_temp=True)
