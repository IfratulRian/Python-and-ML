import numpy as np

letter = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
          [['J','K','L'],['M','N','O'],['P','Q','R']],
          [['S','T','U'],['V','W','X'],['Y','Z',' ']]])
she = letter[2,0,0] + letter[0,2,1] + letter[0,0,0] + letter[1,2,2] + letter[0,0,0]
me = letter[1,2,2] + letter[0,2,2] + letter[0,0,0] + letter[1,1,1]
print(she, letter[2,2,2], me)
