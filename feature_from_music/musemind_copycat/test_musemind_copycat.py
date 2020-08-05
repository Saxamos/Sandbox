from feature_from_music.musemind_copycat.musemind_copycat import (BASE_PATH,
                                                                  _read_shot_times_from_csv_and_convert_to_ms,
                                                                  _reduce_adjacent_times, _replace_too_small_intervals)


def test_read_shot_times_from_csv_and_convert_to_ms():
    # When
    result = _read_shot_times_from_csv_and_convert_to_ms(BASE_PATH / 'club_med')

    # Then
    assert result == [(0, 1110), (6060, 7030), (7040, 7130), (7140, 8020), (8030, 9020), (9030, 10070), (18110, 18220),
                      (19120, 20120), (20130, 21010), (21020, 22070), (22080, 24050), (24060, 30000)]


def test_reduce_adjacent_times():
    # Given
    shot_times = [(0, 1110), (6060, 7030), (7040, 7130), (7140, 8020), (18110, 18220), (18230, 20120), (24060, 30000)]

    # When
    result = _reduce_adjacent_times(shot_times)

    # Then
    assert result == [(0, 1110), (6060, 8020), (18110, 20120), (24060, 30000)]


def test_replace_too_small_intervals():
    # Given
    reduced_times = [(0, 110), (130, 1130), (6060, 6460), (18110, 18220), (19120, 30000), (30200, 30250)]
    min_interval_size = 500

    # When
    result = _replace_too_small_intervals(reduced_times, min_interval_size)

    # Then
    assert result == [(20, 1130), (6060, 6570), (19120, 30050)]
