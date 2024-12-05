import math

def eh_racional(a, b, c):
    discriminante = b**2 - 4*a*c

    # Check for non-numeric discriminant
    if not isinstance(discriminante, (int, float)):
        raise ValueError("Input invalido: Coeficientes devem ser numeros")

    # Handle negative discriminant (irrational roots)
    if discriminante < 0:
        return "Ops, discriminate negativo"

    raiz_discriminante = math.sqrt(discriminante)
    return raiz_discriminante.is_integer()

# Get input coefficients (ensure they are numbers)
try:
    a, b, c = map(float, input().split())
except ValueError:
    print("Invalid input: Please enter numbers separated by spaces.")
    exit()

# Call the function and print the result
result = eh_racional(a, b, c)
if isinstance(result, bool):  # Check if result is a boolean (rational)
    if result:
        print("Y")  # Rational roots
    else:
        print("N")  # Irrational roots
else:
    print(result)  # Print "Ops, discriminate negativo" if negative discriminant