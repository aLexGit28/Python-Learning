songs = ['Believer', 'Closer', 'Perfect', 'Shape of You', 'Thunder']

songs.sort()

print("Songs:", songs)

song = input("Enter song name: ")

low = 0
high = len(songs) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if songs[mid].lower() == song.lower():
        found = True
        break
    elif songs[mid].lower() < song.lower():
        low = mid + 1
    else:
        high = mid - 1

if found:
    print("'" + song + "' found!")
else:
    print("'" + song + "' not found!")