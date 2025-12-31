#
# import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame

#
# mydataset = {
#   'cars': ["BMW", "TOYTA", "Ford"],
#   'passings': [2, 7, 5]
# }
#
# myvar = pd.DataFrame(mydataset)
#
# print(myvar)
#
# # Pandas Series
# a = [1,2,3,4,5]
# myvar1 = pd.Series(a)
# print(myvar1)
#
# b = [6,7,8,9,10]
# c = [11,12,1,14,15]
#
# myvar2 = pd.Series(b)
#
# print(myvar2[0])



## Create Labels

# import pandas as pd
#
# a = [3,4,5]
#
# mybar = pd.Series(a,index=["x","y","z"])
# print(mybar)
# print(mybar)


# a = [1, 7, 2]
#
# myvar = pd.Series(a, index = ["x", "y", "z"])
#
# print(myvar["z"])
#
# Colorieas = { "day1":380,"day2": 420,"day3":650}
# myvar = pd.Series(Colorieas)
# print(myvar)

# DataFrames

# Data = {"Name":["Sayem","Rakib","Sifat"],"Age":[23,23,25]}
# df = pd.DataFrame(Data)
# print(df)

# Data = {
#     "Colories" : [320,230,409],
#     "Duration": [2,3,4]
# }
# myvar = pd.DataFrame(Data)
# print(myvar)


# Data = {
#     "Colories": [230,333,334,676],
#     "Duration": [5,6,7,9]
#
# }
# df = pd.DataFrame(Data)
#
#
# print(df.loc[[0,1]])
# print(df.loc[2])

# import pandas as pd
#
# Data ={
#     "Colories": [340,330,440],
#     "Duration": [3,4,5]
# }
# df = pd.DataFrame(Data)
# print(df)


# Max Rows Statement
# import pandas as pd
#
# print(pd.options.display.max_rows)

# import  pandas as pd
# pd.options.display.max_rows = 10000
# df = pd.read_csv('Data.csv')
# print(df)
# import pandas as pd
#
# json =[
#     {"Name": "Sayem","Age": 23,"City":"Dhaka"},
#     {"Name": "Hamja","Age": 24,"City":"Dhaka"},
#     {"Name": "Bipul","Age": 22,"City":"Nohakhali"}
# ]
# df = pd.read_json("Data.json")
# print(df)

# import pandas as pd
#
# data = {
#   "Duration":{
#     "0":60,
#     "1":60,
#     "2":60,
#     "3":45,
#     "4":45,
#     "5":60
#   },
#   "Pulse":{
#     "0":110,
#     "1":117,
#     "2":103,
#     "3":109,
#     "4":117,
#     "5":102
#   },
#   "Maxpulse":{
#     "0":130,
#     "1":145,
#     "2":135,
#     "3":175,
#     "4":148,
#     "5":127
#   },
#   "Calories":{
#     "0":409.1,
#     "1":479.0,
#     "2":340.0,
#     "3":282.4,
#     "4":406.0,
#     "5":300.5
#   }
# }
#
# df = pd.DataFrame(data)
#
# print(df)




##Pandas - Analyzing DataFrames
#
# import pandas as pd
#
# df = pd.read_csv("Data.csv")
# print(df.head(10))
#
# print(df.tail())
# print(df.info())

