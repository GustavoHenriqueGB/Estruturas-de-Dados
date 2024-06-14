def fibonacci(n, numerosUsados):
	if n == 0:
		numerosUsados[0] += 1
		return 0;
	elif n == 1:
		numerosUsados[1] += 1
		return 1;
	else: 
		numerosUsados[n] += 1
		return fibonacci(n - 1, numerosUsados) + fibonacci(n - 2, numerosUsados)

n = int(input())
numerosUsados = [0] * (n + 1)

valorFibonacci = fibonacci(n, numerosUsados)

print(f"fibonacci({n}) = {valorFibonacci}.")

for i in range(n + 1):
	print(f"{numerosUsados[i]} chamada(s) a fibonacci({i}).")