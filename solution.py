def jumpingOnClouds(c):
  steps = 0
  current = 0
  stop = len(c) - 1
  while current != stop:
    try:
      if c[current + 2] == 0:
        current += 2
        steps += 1
      elif c[current + 1] == 0:
        current += 1
        steps += 1
    except IndexError:
      if current != stop:
        current += 1
        steps += 1
      break
  return steps 
