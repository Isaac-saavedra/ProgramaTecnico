// Calcular el salario de un grupo de n trabajadores
// dada la cantidad de horas trabajadas y la tarifa 
// por hora para cada uno
Algoritmo sin_titulo
	Definir n, contador, salario, horas, tarifa, suma Como Entero;
	Escribir  "Ingrese cuantos trabajadores tiene: ";
	Leer n;
	contador <- 1;
	suma <- 0;
	Mientras contador <= n Hacer
		Escribir " [X] Ingrese horas: ";
		Leer horas;
		Escribir " [X] Ingrese tarifa: ";
		Leer tarifa;
		salario <- horas * tarifa;
		Escribir "   [X] Salario es: ", salario;
		suma <- suma + salario;
		contador <- contador + 1;
	FinMientras
	Escribir  "La suma de ", n, " trabajadores es: ", suma;
FinAlgoritmo
