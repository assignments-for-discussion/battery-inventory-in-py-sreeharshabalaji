
def count_batteries_by_usage(cycles):
  s = 0
  r = 0
  f = 0
  for i in range(len(cycles)):
    if cycles[i]<400:
    	s = s+1
    elif(cycles[i]>=920):
     	f = f+1
    else:  
     	r = r+1
      
  return {
    "lowCount": s,
    "mediumCount": r,
    "highCount": f
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
