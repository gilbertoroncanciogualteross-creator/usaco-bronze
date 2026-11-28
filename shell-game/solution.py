# 1. How do I read this input?

# Almacenar en una variable el primer valor enviado por el usuario, que sera el numero de swaps.
# Este numero de swaps sera util para saber cuantas veces se deben hacer cambios entre las
# Parejas de conchas.
# Luego en una lista almacenar las siguentes lineas entregadas por el usuario, y nombrar a sus componentes
# como a, b y c respectivamente.

# 2. How do I represent where the ball is?

# Podriamos representar a la bola como una variable cuyo valor sea igual al valor de la posicion
# En la que se encuentra ahora mismo. (1, 2, 3)
 
# 3. When shells a and b swap, what happens to the ball?

# Existen 3 casos, el primer caso seria donde dicha concha en la que se encuentra ball se queda en
# La misma posicion, el segundo caso seria donde dicha concha en la que se encuentra ball es a y se intercambia
# con la posicion b y el tercer caso seria donde dicha concha en la que se encuentra ball es b y se  intermabia
# con a.

# 4. How do I count correct guesses, and how do I try all three starting positions?

# Para las adivinanzas correctas debemos contar cuantas veces la concha estuvo en la misma posicion
# y que poseia el valor de ball. Para probar todos los posibles valores de ball, asumiremos que su valor es primero,
# 1, despues que su valor sea 2 y despues que su valor sea tres. El resultado a imprimir sera la respuesta mas grande.

# 1. Read N

N = int(input())

# 2. Read the N lines into a list

swaps = []
for i in range(N):
    a, b, g = map(int, input().split())
    swaps.append((a, b, g))

results = []

# 3. For each starting position (1, 2, 3): replay all the swaps, counting correct guesses

for start in range (1, 4):
    ball = start
    count = 0

    for a, b, g in swaps:

        # First Case

        if ball == a:
            ball = b
        elif ball == b:
            ball = a

        if ball == g:
            count += 1

    results.append(count)

print(max(results))