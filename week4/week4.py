def orangecap(d):
	players = list(set([j for i in d.keys() for j in list(d[i].keys())]))
	total = []
	for i in players:
		total_score = 0
		for j in list(d.keys()):
			if i in d[j]:
				total_score += d[j][i]
		total.append((total_score,i))
	total.sort()
	return((total[-1][1],total[-1][0]))

  
def addpoly(p1,p2):
	poly = p1+p2
	exp = list(set([i[1] for i in poly]))
	exp.sort()
	exp.reverse()
	res = []
	for i in exp:
		total = 0
		for j in poly:
			if j[1] == i:
				total += j[0]
		res.append((total,i))
	for i in res:
		if i[0] == 0:
			res.remove(i)
	return res

def multpoly(p1,p2):
	poly = [[(i[0]*j[0],i[1]+j[1]) for j in p2] for i in p1]
	res = []
	for i in poly:
		res = addpoly(res,i)
	for i in res:
		if i[0] == 0:
			res.remove(i)

	return res
import ast

def todict(inp):
    inp = ast.literal_eval(inp)
    return (inp)

def topairoflists(inp):
    inp = "["+inp+"]"
    inp = ast.literal_eval(inp)
    return (inp[0],inp[1])

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "orangecap":
   arg = todict(farg)
   print(orangecap(arg))
elif fname == "addpoly":
   (arg1,arg2) = topairoflists(farg)
   print(addpoly(arg1,arg2))
elif fname == "multpoly":
   (arg1,arg2) = topairoflists(farg)
   print(multpoly(arg1,arg2))
else:
   print("Function", fname, "unknown")
  

