import math

def is_square_free(n):
    if n == 1  or n == -1:
        return True
    for d in range(2, int(math.ceil(math.sqrt(n))+1)):
        if n % (d*d) == 0:
            return False
    return True

def is_prime(n):
    d = 2
    while d != n:
        if((n % d)==0):
            return False

        d+=1
        if(d != n):
            if(d % 2 ==0):
                if(d != 2):
                    d+=1
    return True

def find_prime_divisors(n):

    prime_divisors =[]
    for d in range(2, n):
        if(n % d==0):
            if(is_prime(d)):
                prime_divisors.append(d)

    return prime_divisors;

def korselts(n, divisorList):
    flag = 0
    for d in range(0, len(divisorList)):
        flag=1
        p = divisorList[d]
        if(((n-1)%(p-1))!=0):
            return False
    if(flag==0):
        return False
    return True

def is_carmichael(n):
    if(is_square_free(n)):
        divisorList = find_prime_divisors(n)
        if(korselts(n ,divisorList)):
            return True
    else:
        return False

carmichael_list = []
num_found=0
i=0
while num_found!=5:
    if(is_carmichael(i)):
        carmichael_list.append(i)
        num_found+=1
    i+=1

for i in range(len(carmichael_list)):
    print carmichael_list[i], "\n";

#561,1105,1729,2465,2821,6601,8911,10585,15841,29341,41041 ,46657 ,52633 ,62745 ,63973 ,75361,101101 ,115921 ,126217 ,162401 ,172081 ,188461 ,252601 ,278545 ,294409,314821 ,334153 ,340561 ,399001 ,410041 ,449065 ,488881 ,512461 ,530881 ,552721 

