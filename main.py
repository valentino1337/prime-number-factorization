import os.path

def lang():
    lang = input('Which language do you want to use?/Aký jazyk použiť? (EN/SK): ').lower()
    with open('lang.txt', 'w') as file:
        file.write(lang)

def isprime():
    print(nolist)
    with open('primenumbers.txt', 'w'):
        pass
    howmany = int(input(howmanyq))
    for num in range(howmany):
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                break
        else:
            if num <= 1:
                pass
            else:
                with open('primenumbers.txt', 'a') as file:
                    file.write(str(num) + '\n')
    else:
        pass

if os.path.isfile('lang.txt') == False:
    lang()
else: pass

with open('lang.txt', 'r') as langconfig:
    language = langconfig.readline()

    if language == 'en':
        nolist = 'You do not have a list of prime numbers yet. This will create one for you.'
        howmanyq = 'Check primes up to what number?: '
        primefactorq = 'What number do you want to prime factor?: '
        outofrange = 'You either entered a prime number or the number is too great and the list is too short'
        resultis = 'Prime factors of number '
        resultis0 = ' are '

    else:
        if language == 'sk':
            nolist = 'Nenájdený súbor s prvočíslami, vytváram.'
            howmanyq = 'Po aké číslo chceš nájsť prvočísla?: '
            primefactorq = 'Aké číslo chceš rozložiť?: '
            outofrange = 'Buď si zadal prvočíslo alebo je číslo príliš veľké a zoznam príliš krátky'
            resultis = 'Prvočíselný rozklad čísla '
            resultis0 = ' je '
        else: print('wrong language config')

if os.path.isfile('primenumbers.txt') == False:
    isprime()
else: pass

def dasadelit(rozklad,ktorymrozlozit):
    if int(rozklad) %int(ktorymrozlozit) != 0:
        return True# has decimals
    else:
        return False# doesnt have decimals

def rozkladat(rozklad):
    with open('primenumbers.txt', 'r') as file:
        content = file.readlines()
    
    founddivisible = False
    ktoryriadok = 0

    while founddivisible == False:
        try:
            ktorymrozlozit = content[ktoryriadok]
        except IndexError:
            print(outofrange)
            return
        if dasadelit(rozklad, ktorymrozlozit) == False:
            druhydelitel = int(int(rozklad)/int(ktorymrozlozit))
            ktorymrozlozit = int(ktorymrozlozit)
            founddivisible = True
            return [ktorymrozlozit, druhydelitel]# prve je prvocislo cim sa deli, druhe je vysledok delenia a to co treba delit znova
        else:
            ktoryriadok = ktoryriadok + 1

rozklad = int(input(primefactorq))# original number

numbers = [rozklad, rozkladat(rozklad)[1]]# 1-orig, 2-second number, 3-next number
primes = [rozkladat(rozklad)[0]]

ktorearray = 1
done = False

while done == False:
    rozlprime = int(rozkladat(numbers[ktorearray])[0])
    rozl1 = int(rozkladat(numbers[ktorearray])[1])
    if rozl1 == 1: done = True
    else: pass
    primes.append(rozlprime)
    numbers.append(rozl1)
    ktorearray = ktorearray + 1

print(resultis + str(rozklad) + resultis0 + '*'.join(map(str, primes)))
