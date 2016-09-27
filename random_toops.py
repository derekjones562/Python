from random import randint

def random_4_toop (a, b):
    a = abs(a)
    b = abs(b)
    toop=[]
    for i in range(0,4):
        if (randint(0,1)):
            toop.append(randint(a, b))
        else:
            toop.append(randint(a, b)-100)
    ## return an array reference
    return toop

	
def gen_random_4_toops(a,b,n):
    toops=[]
    for i in range(0, n):
        toops.append(random_4_toop(a,b))
    return toops ## return an array reference

def sort_random_4_toops_by_sum(listoftoops):
    sorted_toops=[]
    for toop in listoftoops:
        if not sorted_toops:
            sorted_toops.append(toop)
        else:
            mysum = sum(toop)
            numofsorted_toops = len(sorted_toops);
            for i in range(0, numofsorted_toops):
                sum2 = sum(sorted_toops[i])
                if(mysum > sum2):
                    sorted_toops.insert(i, toop)
                    break
                if(i+1==numofsorted_toops):
                    sorted_toops.append(toop)
                    break
    return sorted_toops

def filter_random_4_toops_by_sum(toops, thresh):
    filtered_toops=[]
    for t2 in toops:
        if(sum(t2) > thresh):
            filtered_toops.append(t2)
    return filtered_toops

def test_step_1():
    toop1 = random_4_toop(1, 100)
    toop2 = random_4_toop(1, 100)
    toop3 = random_4_toop(1, 100)
    print 'toop1 = ' + str(toop1)
    print 'toop2 = ' + str(toop2)
    print 'toop3 = ' + str(toop3)
def test_step_2():
    toops = gen_random_4_toops(1, 100, 5)
    for n, toop in zip(xrange(1, 6), toops):
        print 'toop ' + str(n) + ": " + str(toop)
def test_step_3():
    toops = gen_random_4_toops(1, 100, 5)
    print "---- random 4-toops:"
    for n, toop in zip(xrange(1, 6), toops):
        print 'toop ' + str(n) + ": " + str(toop) +\
        'sum = ' + str(sum(toop))
    print "\n---- random 4-toops sorted by sum:"
    sorted_toops = sort_random_4_toops_by_sum(toops)
    for n, toop in zip(xrange(1, 6), sorted_toops):
        print 'toop ' + str(n) + ": " + str(toop) +\
        'sum = ' + str(sum(toop))
def test_step_4():
    toops = gen_random_4_toops(1, 100, 5)
    print "---- random 4-toops:"
    for n, toop in zip(xrange(1, 6), toops):
        print 'toop ' + str(n) + ": " + str(toop) +\
        'sum = ' + str(sum(toop))
    thresh = 0
    print "\n---- random 4-toops filtered by sum above", thresh, ":"
    filtered_toops = filter_random_4_toops_by_sum(toops, thresh)
    for n, toop in zip(xrange(1, 6), filtered_toops):
        print 'toop ' + str(n) + ": " + str(toop) +\
        '; sum = ' + str(sum(toop))


#test_step_1()
#test_step_2()
#test_step_3()
test_step_4()
