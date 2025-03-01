"""altura = float(input("ingrese su altura en m . cm:"))
reaccion = altura / 100 
print(f"Su impulso nervioso de los pies a la cabeza seria de: {reaccion} m/s")
"""


largo_inicial = float(input("Ingrese el largo actual del cabello en cm: "))
largo_objetivo = float(input("Ingrese el largo al que se cortará el cabello en cm: "))

promedio_crecimiento = 2  

tiempo_meses = (largo_objetivo - largo_inicial) / promedio_crecimiento

print(f"El estudiante deberá cortarse el cabello en aproximadamente {tiempo_meses:.1f} mes(es).")
