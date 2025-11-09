if __name__ == "__main__":
    def get_the_largest(numbers,n):
        numbers.sort()
        return numbers[:]

    n=[5,6,3,2,9,8,6,1,4]
    print(get_the_largest(n,2))


    def complicated_fun(a,b,c=True,d=False):
        print(a,b,c,d)
    complicated_fun(*[1,3],**{"c":"siva","d":"kafa"})
    """ note: in dict using *args for parameter => value split by keys ,
    ** => values splited"""


def add(a,b):
    return a+b
if __name__ == "__main__":
    print("run")
""" GIL - global interpreter lock

one thread can execute at a bytecode time
resone , that is using on GIL sare the same GIL and take turns running
  in case use multi process

  from multiprocessing import Process

  it's runs truly in parallel because each process has own python interpreter and memory
  



""""
