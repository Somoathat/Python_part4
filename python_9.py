# arb_mean — Accepts any number of integers and prints their average.
def arb_mean(*args):
  total = 0
  for a in args:
    total += a
  print(a/len(args))