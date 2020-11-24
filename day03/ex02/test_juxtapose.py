import numpy as np
from ScrapBooker import ScrapBooker

ma = [["A", "B", "C", "D", "E"],
      ["0", "B", "C", "D", "E"],
      ["1", "B", "C", "D", "E"],
      ["2", "B", "C", "D", "E"],
      ["3", "B", "C", "D", "E"],
      ["4", "B", "C", "D", "E"]]
na = np.asarray(ma)
nb = np.transpose(na)
#print(na)

print("------------------------------------------------------------")
print(ScrapBooker.juxtapose(na, 2, 1))
print("------------------------------------------------------------")
print("------------------------------------------------------------")
print(ScrapBooker.juxtapose(nb, 2, 0))
print("------------------------------------------------------------")