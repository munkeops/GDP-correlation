import pandas as pd
import matplotlib.pylab as plt
url1 = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(PPP)_per_capita"
url2 ="https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_area,_population_and_population_density"
pop_list=pd.read_html(url2)
pop_df=pop_list[1]


pop_df = pop_df.rename(columns = {"Country (or dependent territory)": "Country",}) 
pop_df = pop_df[["Country","Density(pop./km2)"]]

gdp_list = pd.read_html(url1)
gdp_df=gdp_list[2]
gdp_df = gdp_df.rename(columns = {"Country/Territory": "Country"}) 

final_merged =pd.merge(gdp_df, pop_df, on='Country')
final_df = final_merged.rename(columns = {"Int$": "GDP","Density(pop./km2)":"PopDens"}) 
final_df.PopDens = list(map(int, final_df.PopDens))
print(final_df)
#print()
print(final_df['GDP'].corr(final_df['PopDens']))

plt.scatter(final_df.GDP, final_df.PopDens)


