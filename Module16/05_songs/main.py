violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]


def time_of_song(name, songs):
    for song in songs:
        for name_song in song:
            if name_song == name:
                return song[1]


count_song = int(input("Сколько песен выбрать? "))
result_time = 0

for song in range(1, count_song + 1):
    print("Название", song, "-й песни:", end=" ")
    name = input()
    result_time += time_of_song(name, violator_songs)

print("Общее время звучания песен:", round(result_time, 2))

# зачтено
