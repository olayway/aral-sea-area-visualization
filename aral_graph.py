import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/data/aral_area.csv')
df = df[['Year', 'Total']]
print(df)

plt.figure(figsize=(9, 16))
plt.plot(df['Year'], df['Total'], marker='o', linestyle='-', color='#E6825D')
plt.xlabel('Year')
plt.ylabel('Area in 1000 sq km')
plt.title('Does the Aral sea have a future?')
plt.show()
