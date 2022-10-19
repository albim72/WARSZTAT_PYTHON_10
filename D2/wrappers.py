import math
import time

def pomiarczasu(funkcja):

    def wrapper():
        starttime = time.perf_counter()
        funkcja()
        endtime = time.perf_counter()
        print(f'czas wykonania funkcji: {endtime-starttime} s')
    return wrapper


#opóźnienie wykonania kodu

def sleep(funkcja):
    def wrapper():
        time.sleep(8)
        return funkcja()
    return wrapper


@sleep
def startfunc():
    print("no to startujemy....każdy pomiar co 8 sekund")

startfunc()
@sleep
@pomiarczasu
def big_lista():
    sum([i**2 for i in range(1000000)])

big_lista()

lt = [i**2 for i in range(1000000)]
@sleep
@pomiarczasu
def big_lista_out():
    sum(lt)

big_lista_out()

@pomiarczasu
@sleep
def big_lista_d():
    sum([math.pow(((i+1)**5),3) for i in range(1000000)])

big_lista_d()



