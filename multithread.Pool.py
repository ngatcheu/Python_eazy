#Nouvelle classe python pour le multithreading: ThreadPoolExecutor
#https://docs.python.org/fr/3.10/library/concurrent.futures.html?highlight=threadpoolexecutor#concurrent.futures.ThreadPoolExecutor

from concurrent.futures import ThreadPoolExecutor

values = [3,4,5,6,7,8]

def cube(x):
    print(f'Cube of {x}:{x*x*x}')

if __name__ == '__main__':

    result = []
    #Definir le nombre de worker 
    with ThreadPoolExecutor(max_workers=6) as exe:
        exe.submit(cube,2)

        #Maps the method 'cube' with the list of values.
        result = exe.map(cube,values)


    for r in result:
            print(r)
