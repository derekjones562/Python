

def make_2nd_degree_poly(k2, k1, k0):
    return lambda x: (str(k2)+"x^2 + " + str(k1) + "x + " + str(k0) + " at x = " +str(x) + " is " + str(k2*x*x + k1*x + k0))

def gen_2nd_deg_polys (coeffs):
    listOfPoly=[]
    for t in coeffs:
        listOfPoly.append(make_2nd_degree_poly(t[0],t[1],t[2]))
    return listOfPoly

def apply_2nd_deg_polys2(polys, numbers):
    app2nd =[]
    for n in numbers:
        for p in polys:
            app2nd.append(p(n))
    return app2nd

def poly_dance(coeffs, numbers):
    polys = gen_2nd_deg_polys(coeffs)
    poly_maps = apply_2nd_deg_polys2(polys, numbers)
    display_poly_maps(poly_maps)

def display_poly_maps(polys):
    for p in polys:
        print p

triplet0 = (1, 2, 3)
triplet1 = (4, 5, 6) 
#triplet2 = (7, 8, 9)
tripList = [triplet0, triplet1]#, triplet2]

#p1 = make_2nd_degree_poly(1, 2, 3)
#p2 = make_2nd_degree_poly(4, 5, 6)
#print p1(1)
#print p2(3)

numbers = range(1, 6)
poly_dance(tripList, numbers)
