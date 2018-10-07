def descending(seq):
	if seq == []:
		return(True)
	for i in range(len(seq)-1):
		if seq[i] < seq[i+1]:
			return(False)
	else:
		return(True)

def valley(lst):
    flag = False
    for i in range(0, len(lst) - 1):
        if lst[i] == lst[i+1]:
            return False
        if not flag:
            if lst[i] > lst[i+1]:
                continue
            if lst[i] < lst[i+1]:
                flag = True
        else:
            if lst[i] > lst[i+1]:
                return False
            elif lst[i] < lst[i+1]:
                continue
    return flag
def transpose(lst):
    return [list(x) for x in zip(*lst)]
import ast

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "descending":
  arg = parse(farg)
  print(descending(arg))

if fname == "valley":
  arg = parse(farg)
  print(valley(arg))

if fname == "transpose":
  arg = parse(farg)
  print(transpose(arg))
  

