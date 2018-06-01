import sys

def rollAverage(dest):
  average = 0.0
  i = 0
  for i in range(dest):
    average = (average + sum(range(1,i+1))) / 2
  return average

if len(sys.argv) != 3:
  print('Usage: python main.py <start> <end>')
  exit(1)

start = int(sys.argv[1])
end = int(sys.argv[2])
for i in range(start,end+1):
  #print('rollAverage(' + str(start) + ') = ' + str(rollAverage(start)))
  start += 1
