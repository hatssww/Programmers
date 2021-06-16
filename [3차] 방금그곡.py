def change(melody):
    if 'A#' in melody: melody = melody.replace('A#', 'a')
    if 'C#' in melody: melody = melody.replace('C#', 'c')
    if 'D#' in melody: melody = melody.replace('D#', 'd')
    if 'F#' in melody: melody = melody.replace('F#', 'f')
    if 'G#' in melody: melody = melody.replace('G#', 'g')
    return melody


def solution(m, musicinfos):
    m = change(m)
    ans = ('(None)', None)
    for info in musicinfos:
        start, end, title, melody = info.split(',')
        start_h, start_m, end_h, end_m = map(int, start.split(':') + end.split(':'))
        time = 60 * (end_h - start_h) + (end_m - start_m)
        melody = change(melody)
        melody_played = (melody * time)[:time]
        if m in melody_played:
            if ans[1] == None or time > ans[1]:
                ans = (title, time)

    return ans[0]


print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))