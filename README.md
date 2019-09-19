# Visualization with BarCharts LinePlots

This is study is prepared for the Assignmen-4 of the "Applied Plotting, Charting & Data Representation in Python Course" by University of Michigan. In the study, we try to find an answer to the question of "__How are the numbers of wins medals from Summer Olympics changed over the years in terms of Turkey and Netherlands?__". To reach the answer, 2 datasets are needed. Which are;
- The Netherlands wins medals for every year.
- Turkey wins medals for every year.

We know that Wikipedia is one of the rich and common open source so it is not difficult to reach and get the information which we need. The data of the [Netherlands Records](https://en.wikipedia.org/wiki/Netherlands_at_the_Olympics#Medals_by_Summer_Games) and [Turkey Records](https://en.wikipedia.org/wiki/Turkey_at_the_Olympics#Medals_by_Summer_Games) were saved as a CSV file and used in the study. While looking at the data it is understood that the Summer Olympics Games continue since 1896 every 4 years period, except in 1916,1940,1944.

While visualizing the data, "bar chart" charting method was selecting. Also for showing all 3 medals (bronze, silver and gold) in one bar, "stacked bar chart" method was used. And close colors were selected for these 3 types of medals for every 2 countries. On the other hand, for simplies of the chart, 2 different (contrast) colors were selected for 2 countries. And finally, the total medals numbers were added to chart and the information of y-label and y-ticks were disabled.

Lastly, for making an evaluation about the medals numbers, the yearly average medals numbers were added the chart as a line. Because of the participant numbers (countries) are changing nearly every Olympics year, the average medals numbers are also changing every year. So, a new dataset was created from 28 different Wikipedia URLs by scraping. And calculating the average number for every Olympics year and adding the chart.

As a result;
- Except 2 Olympics years, Netherlands won more medals than Turkey.
- Except for 1 Olympics year, Turkey couldn't win more medals than the overall average.
- More than half of the Olympics years, Netherlands also couldn't win more medals than the overall average.
- After 1980 both Netherland and Turkey are wining medals properly. Also, the Netherlands is winning medals above the overall average.
