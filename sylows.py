from sys import stdin, stdout
from sympy import factorint, divisors

class Sylow:   

    #Class constructor
    def __init__(self, ord):
        self.ord = ord
        #Returns a dictionary of the prime factors and multiplicities
        self.primedict = factorint(ord)
        #Dictionary of prime factors and (list of possible) order of the p-sylows
        self.psylows = factorint(ord)
        #Dictionary of prime factors and quantity of the p-sylows
        self.amount = factorint(ord)
        #Dictionary of normal psylows (order - boolean)
        self.isnormal = dict()
        self.simple = False #True here means "There could exist a simple group of order ord"

    def get_prime(self):
        return self.primedict

    def get_sylows(self):
        return self.psylows
    
    def get_amount(self):
        return self.amount

    def get_normal(self):
        return self.isnormal

    def get_simple(self):
        return self.simple

    def computation(self):
        #Iterating through the prime factors p. np is the amount of psylows
        for p in self.primedict:
            m = int(self.ord/(p**self.primedict[p]))
            self.isnormal[p] = False
            #compute possible values for np
            possible_np = []
            for q in divisors(m):
                if q % p == 1:
                    possible_np.append(q)
            self.psylows[p] = p**self.primedict[p]
            if possible_np == [1]:
                self.amount[p] = 1
                self.isnormal[p] = True

                #resulttext += """C`è un`unico {}-Sylow in un gruppo di ordine {}""".format(p,ord)
                #resulttext += """È un sottogrupo normale di ordine {}""".format(p**self.primedict[p])
                #resulttext += """Di conseguenza non esistono gruppi semplici di ordine {}""".format(ord)
                #print('C`è un`unico', p, '-Sylow in un gruppo di ordine', ord)
                #print('È un sottogrupo normale di ordine', p**self.dict[p])
                #print('Di conseguenza non esistono gruppi semplici di ordine', ord)
            else:
                self.amount[p] = possible_np
                self.isnormal[p] = False #meaning we don't know yet

                #resulttext += """I possibili numeri di {}-Sylows sono {}""".format(p,possible_np)
                #print('I possibili numeri di', p, '-Sylows sono', possible_np)

def parser(ord):
    s = Sylow(ord)
    s.computation()
    resulttext = []
    for p in s.get_sylows():
        if s.get_normal()[p]:
            resulttext.append("""C`è un`unico {}-Sylow in un gruppo di ordine {}""".format(p,ord))
            resulttext.append("""È un sottogrupo normale di ordine {}""".format(s.get_sylows()[p]))
            resulttext.append("""Di conseguenza non esistono gruppi semplici di ordine {}""".format(ord))
        else:
            resulttext.append("""I possibili numeri di {}-Sylows sono {}""".format(p,s.get_amount()[p]))
            resulttext.append("""Sono tutti coniugati di ordine {}""".format(s.get_sylows()[p]))
    return resulttext
