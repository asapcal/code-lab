import sys

# Leitura até o EOF
for line in sys.stdin:
    try:
        N = int(line.strip())  # Convertendo a entrada para inteiro
        if N == 0:
            print("vai ter copa!")
        else:
            print("vai ter duas!")
    except ValueError:
        break  # Encerra caso a entrada não seja válida
