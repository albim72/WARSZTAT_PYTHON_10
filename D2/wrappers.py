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


#dekorator z funkcją magiczną __name__

def debug(funkcja):
    def wrapper(*args,**kwargs):
        print(f'wołana funkcja to: {funkcja.__name__}')
        funkcja(*args)
    return wrapper

@debug
def info(i):
    print(f"informacja: {i}")

info("nr 4566")


#repeater

def repeater(n):
    def wrapper(funkcja):
        def inner(*args):
            for i in range(n):
                funkcja(*args)
        return inner
    return wrapper


@repeater(n=5)
def komunikat(k,n):
    print(f'ważny komunikat: {k}, numer: {n}')

komunikat("T5456464",3)


@repeater(n=7)
def hx(n):
    print((n-1)**7)

hx(9)
