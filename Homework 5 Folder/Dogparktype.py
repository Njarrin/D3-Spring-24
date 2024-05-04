import random
import pandas as pd

data = []
dates = pd.date_range(start='2023-04-24', periods=30)

for date in dates:
    data.append({
        'date': date.strftime('%Y-%m-%d'),
        'num_small_dogs': random.randint(10, 80),
        'num_medium_dogs': random.randint(10, 80),
        'num_large_dogs': random.randint(10, 80)
    })

df = pd.DataFrame(data)
df.to_csv('dog_counts.csv', index=False) 