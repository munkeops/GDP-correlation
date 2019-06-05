import pandas as pd
import matplotlib.pylab as plt
url1 = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(PPP)_per_capita"
url2 = "https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"
pop_list=pd.read_html(url2)
pop_df=pop_list[1]
pop_df = pop_df.rename(columns = {"Country or area": "Country"}) 

#print(pop_df)
gdp_list = pd.read_html(url1)
gdp_df=gdp_list[2]
gdp_df = gdp_df.rename(columns = {"Country/Territory": "Country"}) 
#print (gdp_df)
gdp_df['Country'] = gdp_df['Country'].str.replace(r'\[.*?\]','')

final_merged =pd.merge(gdp_df, pop_df, on='Country')
final_df=final_merged[['Country','Int$','Population(1 July 2017)[3]']]
#print(final.columns)
final_df = final_df.rename(columns = {"Int$": "GDP","Population(1 July 2017)[3]":"Population"})
final_df = final_df[final_df.Country != "India"]
#final_df = final_df[final_df.Country != "China"]
final_df = final_df[final_df.Population <700000000]
final_df = final_df[final_df.Country != "United States"]


print(final_df)
print(final_df['GDP'].corr(final_df['Population']))

plt.scatter(final_df.GDP, final_df.Population)



