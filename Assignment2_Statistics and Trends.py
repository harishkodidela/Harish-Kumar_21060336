import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#working with datasets
def handling_data(path):
    ''' generating two dataset with country and year as columns
    parameters: Path- location of the dataset.
    '''
    df = pd.read_csv(path)
    df=df.drop(columns=['Indicator Code','Country Code'])
    df1 = df.transpose()
    df1.columns = df1.iloc[0].values.tolist()
    df1=df1.iloc[1:]
    return df,df1

country,year=handling_data('Data World Bank_Climate change data.csv')
columns=year.iloc[0].unique()
countries=['India','Pakistan','China','Japan']
country_select=year[countries]

#working with bar graphs
def bar_graph(data_input,indicator):
    '''
    plotting the bar graphs for the given data and its indicators
    parameters: data_input- dataset, indicator- indicators to plot
    '''
    data_list=[]
    c=indicator
    for x in range(4):
        data_list.append(data_input.iloc[:,c])
        x=x+1
        c=c+76
    d= pd.DataFrame(data_list)
    d=d.iloc[:,1:]
    d=d.transpose()
    d.iloc[[30,40,50,58]].plot(kind='bar',figsize=(15,8),xlabel='Years',ylabel=columns[indicator],title=columns[indicator]+' from 1990 to 2018')
    plt.show()
bar_graph(country_select,0)
bar_graph(country_select,31)

#correlation of the data
country=year[['China']]
data_list=[]
indicators_index=[0,10,11,49,67,44]
for i in indicators_index:
    data_list.append(country.iloc[:,i])
d= pd.DataFrame(data_list)
d=d.transpose()
d.columns=d.iloc[0]
d=d[31:60]
d=d[1:]
d=d.fillna(d.median())
ax = sns.heatmap(d.corr(),cmap="BuPu", annot=True)
plt.title("China indicators correlation")
plt.show()

#correlation of the data
country=year[['Pakistan']]
temp=[]
indicators_index=[0,10,11,49,67,44]
for i in indicators_index:
    temp.append(country.iloc[:,i])
d= pd.DataFrame(temp)
d=d.transpose()
d.columns=d.iloc[0]
d=d[31:60]

d=d.fillna(d.median())
ax = sns.heatmap(d.corr(),cmap="YlGnBu", annot=True)
plt.title("Pakistan indicators correlation")
plt.show()

#working with line plots
def line_chart(data_input,indicator):
    '''
    plotting the line graphs for the given data and its indicators
    parameters: data_input- dataset, indicator- indicators to plot
    '''
    data_list=[]
    c= indicator
    for x in range(4):
        data_list.append(data_input.iloc[:,c])
        x=x+1
        c=c+76
    d= pd.DataFrame(data_list)
    d=d.iloc[:,1:]
    d=d.transpose()
    d.iloc[30:58].plot(kind='line',figsize=(15,8),xlabel='Years',ylabel=columns[indicator],title=columns[indicator]+' from 1990 to 2015')
    plt.show()

line_chart(country_select,59)
line_chart(country_select,42)







