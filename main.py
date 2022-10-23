from sys import stdin, stdout
from sympy import factorint, divisors

def main():
    print ("Calcolare i p-Sylows")
    print ("Inserisci l'ordine del gruppo")
    ord = int(input())

    #prime decomposition
    #without prememorized prime table

    #Returns a dictionary of the prime factors and multiplicities
    prime_dict = factorint(ord)
    #Iterating through the prime factors p. np is the amount of psylows
    for p in prime_dict:
        print('Calcolando', p, '-Sylows')
        m = int(ord/(p**prime_dict[p]))

        #compute possible values for np
        possible_np = []
        for q in divisors(m):
            if q % p == 1:
                possible_np.append(q)
        if possible_np == [1]:
            print('C`è un`unico', p, '-Sylow in un gruppo di ordine', ord)
            print('È un sottogrupo normale di ordine', p**prime_dict[p])
            print('Di conseguenza non esistono gruppi semplici di ordine', ord)
        else:
            print('I possibili numeri di', p, '-Sylows sono', possible_np)



     

if __name__ == "__main__":
    main()