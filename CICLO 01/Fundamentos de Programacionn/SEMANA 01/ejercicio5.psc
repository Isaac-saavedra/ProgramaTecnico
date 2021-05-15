Algoritmo sin_titulo
	Definir operador Como Caracter;
	Definir  valor1, valor2, resultado Como Real;
	Escribir "Elegir una operación a realizar: ";
	Leer operador;
	Escribir  "Ingrese el primer valor";
	Leer valor1;
	Escribir  "Ingrese el segundo valor";
	Leer valor2;
	Si operador == "+" Entonces
		resultado <- valor1 + valor2;
	Fin Si
	Si operador == "-" Entonces
		Si valor1 > valor2 Entonces
			resultado <- valor1 - valor2;
		SiNo
			resultado <- valor2 - valor1;
		FinSi
	Fin Si
	Si operador == "*" Entonces
		resultado <- valor1 * valor2;
	Fin Si
	Si operador == "/" Entonces
		resultado <- valor1 / valor2;
	Fin Si
	Escribir  "El operador elegido es: ", operador;
	Escribir  "El resultado es: ", resultado;
FinAlgoritmo
