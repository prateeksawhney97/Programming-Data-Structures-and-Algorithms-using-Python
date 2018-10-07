def readinput():
  n = int(input())     # Length
  for j in range(n):   
    nextnum = int(input())  # Read each value
    insequence.append(nextnum)
    best.append(0)     # Initialize best[k] for each position
  return

def solve():
  for j in range(len(insequence)):
    # Collect best[k] for values to left of j that divide insequence[j]
    prev = [ best[k] for k in range(j) if insequence[j]%insequence[k] == 0 ]
    if prev:
       best[j] = 1 + max(prev)
    else:
       best[j] = 1

insequence = []
best = []
readinput()
solve()
print(max(best))
