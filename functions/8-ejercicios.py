def es_palindromo(frase):
    no_spaces_frace = frase.replace(" ","").lower()
    
    if no_spaces_frace[::-1] == no_spaces_frace:
        print(f"`{frase}` es palindromo")
    else:
       print(f"{frase} no es palindromo") 

es_palindromo("Amo la paloma")
