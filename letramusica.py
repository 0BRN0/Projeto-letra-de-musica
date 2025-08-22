import sys
from rich import print
from time import sleep

def printLyrics():
    lines = [
        ("Je te laisserai des mots", 0.15), #velocidade por caractere
        ("En-dessous de ta porte", 0.09),
        ("En-dessous de les murs qui chantent", 0.14),
        
        ("", 0.5),  # linha em branco para pausar só
        
        ("Tout près de la place où tes pieds passent", 0.1),
        ("Cachés dans les trous de ton divan", 0.1),
        ("Et quand tu es seule pendant un instant", 0.1),
        
        ("", 0.09),
        
        ("Ramasse-moi", 0.2),
        ("Quand tu voudras", 0.18),
        ("Embrasse-moi", 0.1),
        ("Quand tu voudras", 0.15),
        ("Ramasse-moi", 0.1),
        ("Quand tu voudras", 0.2),
    ]








































    delays = [
        0.5, 3, 0, #tempo por linha
        0,
        0.9, 1.5, 1.5,
        0,
        1.8, 0, 0.9, 0, 1, 2
    ]

    for i, (line, char_delay) in enumerate(lines):
        color = "blue"
        for char in line:
            print(f"[bold][{color}]{char}[/{color}][/bold]", end='')
            sys.stdout.flush()
            sleep(char_delay)
        print()
        sleep(delays[i])

printLyrics()

print("\n[bold red]For you!! 😁🌹")