#!/bin/python
#http://www.pythonchallenge.com/pc/def/0.html


def exponent(base, power):
	answer=base
	for i in range(1, power):
		answer=answer*base
	if (power==0):
		answer=1
	return answer


url='http://www.pythonchallenge.com/pc/def/'+str(exponent(2,38))+'.html'
print url
