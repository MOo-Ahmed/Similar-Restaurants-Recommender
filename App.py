import Engine
import time
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

start = time.time()

# loading the data into lists
dataset_filename = 'Datasets/restaurants.xls'
df = pd.read_excel(dataset_filename)
ids = df['id']
names = df['name']
ctg = df['categories']
longitudes = df['longitude']
latitudes = df['latitude']
combined = []
combined.append(ids)
combined.append(names)
combined.append(ctg)
combined.append(longitudes)
combined.append(latitudes)

#The user data
n = 10
prefs = ['thai', 'vegan']
location = [30.7607299030, 31.8952725481]
engine = Engine.RecommendationEngine(combined, prefs, location, n)
engine.run()

end = time.time()

# total time taken
print(f"Time =  {end - start} seconds")

