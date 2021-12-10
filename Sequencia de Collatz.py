


def collatz(number):
    try:
        
        number = int(number)
        verifica_par = number % 2 == 0
        verifica_impar = number % 2 == 1

        #print('Verifica Par é igual ->' + str(verifica_par))
        #print('Verifica Impar é igual ->' + str(verifica_impar))
    
        if verifica_par:
            return number // 2
        elif verifica_impar:    
            return 3 * number + 1
        
    except ValueError:
        print('Um numero inteiro tem que ser digitado')
       

def seq_collatz(number):
    while True:
        resultado = collatz(number)
        number = resultado
        print(resultado)
        if resultado == 1:
            break
            

    
########################################################


    '''
    def collatz(number):
        if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1
    '''
