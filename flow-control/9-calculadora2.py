n1 = int(input("ingresa un numero: "))

while n1 is not None:
    op = input("ingresa operación: ")
    n2 = int(input("ingresa otro numero: "))

    if op == "+":
        n1+=n2
        print(f"Resultado: {n1}")
    
    elif op == "-":
        n1-=n2
        print(f"Resultado: {n1}")
    
    elif op == "*":
        n1*=n2
        print(f"Resultado: {n1}")
    
    elif op == "/":
        n1/=n2
        print(f"Resultado: {n1}")

