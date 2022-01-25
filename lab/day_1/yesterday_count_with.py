lyrics_text = ''
with open('yesterday.txt', 'r') as file:
    lyrics_text = file.read()
    # while 1:
    #     text = file.readline()
    #     if not text:
    #         break
    #     lyrics_text += text

lyrics_text = ''
with open('yesterday.txt') as f:
    for txt in f:
        lyrics_text += txt

print(len(lyrics_text))
n_of_YESTERDAY = lyrics_text.upper().count('YESTERDAY')
print(f'Number of a word YESTERDAY {n_of_YESTERDAY}')