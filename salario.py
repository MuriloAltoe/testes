valh = int(input("Quanto vc ganha por Hora? "))
valm = int(input("Quantas horas vc trablha no mes? "))

bruto = (valh * valm)

valir = bruto-((bruto/100)*11)
valinss = bruto-((bruto/100)*8)
valsin = bruto-((bruto/100)*5)
liquido = bruto-((bruto/100)*24)

print("O salario bruto e " + str (bruto))
print("O salario - IR e " + str(valir)) 
print("O salario - INSS e " + str(valinss))
print("O salario - Sindicato e " + str(valsin))
print("O salario liquido e " + str(liquido))