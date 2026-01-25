import pandas as pd
mydataset = {"cars": ["BMW", "Volvo", "Ford"],
              "passings": [3, 7, 2]
              }
abc = pd.DataFrame(mydataset)
print(abc)
print()
print(abc.loc[0])


