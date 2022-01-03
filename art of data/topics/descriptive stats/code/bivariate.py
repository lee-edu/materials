cookies = {
  'grade9': [49,29],
  'grade10': [50,20],
  'grade11': [46,36],
  'grade12': [48,32]
}

def calculate_conditional_proportions(table):
  ans = {}
  for col in table:
    total = sum(table[col])
    ans[col] = [x/total for x in table[col]]
  return ans

print(calculate_conditional_proportions(cookies))