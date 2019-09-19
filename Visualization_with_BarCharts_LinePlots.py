### Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
print('Libraries are imported!!!')


### Scrape The Average Medals of Olympics Summer Games from Wikipedia
tot_medals=[]
tot_country=[]
tot_means=[]
years=np.arange(1896,2020,4)
years=list(years)
years = [e for e in years if e not in {1916,1940,1944}]
for i,year in enumerate(years):
    url='https://en.wikipedia.org/wiki/{}_Summer_Olympics_medal_table'.format(year)
    request = requests.get(url)
    soup = BeautifulSoup(request.content,'lxml')
    try:
        tot_medal= soup.find_all('td',{'style':"font-weight:bold"})[3].text.strip()
        tot_medal=int(tot_medal)
        tot_medals.append(tot_medal)
    except:
        tot_medal= soup.find_all('tr',{'class':"sortbottom"})[0].text.strip()
        tot_medal=tot_medal.split()
        tot_medal=tot_medal[6]
        tot_medal=int(tot_medal)
        tot_medals.append(tot_medal)

    country = soup.find('th',{'colspan':"2"}).text.strip()
    country = ''.join(x for x in country if x.isdigit())
    country=int(country)
    tot_country.append(country)
    
    if country!=0:
        mean=round(tot_medal/country)
        tot_means.append(mean)
    else:
        tot_means.append(0)
print('Totally {} URLs scraped!!!'.format(len(years)))
df_medals = pd.DataFrame({'Years':years,'TotalCountry':tot_country, 'TotalMedals':tot_medals,'AverageMedals':tot_means})
df_medals.head()

### Loading Data
df_tr=pd.read_csv('Turkey_MedalsbySummerGames.csv')
df_nl=pd.read_csv('Netherlands_MedalsbySummerGames.csv')
df_medals

### Plotting
fig=plt.figure(figsize=(22, 8))
xvals = np.arange(df_tr.shape[0])
bars=plt.bar(xvals-0.2, df_tr['Bronze'], color = 'darkblue', label='Bronze Medals of Turkey', width = 0.4)
bars=plt.bar(xvals-0.2, df_tr['Silver'], color = 'blue', bottom=df_tr['Bronze'], label='Silver Medals of Turkey', width = 0.4)
bars=plt.bar(xvals-0.2, df_tr['Gold'], color = 'mediumpurple', bottom=df_tr['Bronze']+df_tr['Silver'], label='Gold Medals of Turkey', width = 0.4)


bars2=plt.bar(xvals+0.2, df_nl['Bronze'], color = 'orange', width = 0.4, label='Bronze Medals of Netherlands')
bars2=plt.bar(xvals+0.2, df_nl['Silver'], color = 'goldenrod', bottom=df_nl['Bronze'], label='Silver Medals of Netherlands', width = 0.4)
bars2=plt.bar(xvals+0.2, df_nl['Gold'], color = 'gold', bottom=df_nl['Bronze']+df_nl['Silver'], label='Gold Medals of Netherlands', width = 0.4)

plt.plot(df_medals['AverageMedals'], '--r', linewidth=4, label='Average Medals')

# direct label each bar with Y axis values
for i, bar in enumerate(bars):
    plt.gca().text(bar.get_x() + bar.get_width()/2, bar.get_y()+bar.get_height()+0.6, df_tr['Total'][i] , 
                 ha='center', va='top', color='black', fontsize=11)
    
for i, bar in enumerate(bars2):
    plt.gca().text(bar.get_x() + bar.get_width()/2, bar.get_y()+bar.get_height()+0.6, df_nl['Total'][i] , 
                 ha='center', va='top', color='black', fontsize=11)

### Dejunkifying Plot
[plt.gca().spines[loc].set_visible(False) for loc in ['top', 'left','right']] #Remove top, left and right frame
plt.yticks([]) #disable ythicks

#Adding Title-Label-Legend
plt.title('Wined Medals of Olympics Summer Games\nBetween 1896-2016', size=20)
plt.legend(loc=2, frameon=True, title='Legend')
plt.xticks(xvals, df_nl['Year'],rotation=45, ha='center')


plt.show()