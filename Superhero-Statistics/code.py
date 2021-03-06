# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#path of the data file- path
data=pd.read_csv(path)
#Code starts here 
data['Gender'].replace('-','Agender',inplace=True)
gender_count=data['Gender'].value_counts()
gender_count.plot(kind='bar')
plt.title('Genders Classification')
plt.show()





# --------------
#Code starts here
#Save the value counts of Alignment
alignment=data.Alignment.value_counts()
#Plot the pie chart of 'alignment'
plt.pie(alignment,labels=['good','bad','neutral'],startangle=90,colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue'],explode = (0.05,0.05,0.05))
#Label the plot as Character Alignment
plt.title('Character Alignment')
#Show pie
plt.show()


# --------------
sc_df = data[['Strength','Combat']]
sc_df.cov()
sc_covariance = sc_df.cov().iloc[0,1]
sc_combat = sc_df.Combat.std()
sc_strength = sc_df.Strength.std()
sc_pearson= sc_covariance/(sc_combat*sc_strength)
ic_df = data[['Intelligence','Combat']]
ic_covariance = ic_df.cov().iloc[0,1]
ic_combat = ic_df.Combat.std()
ic_intelligence = ic_df.Intelligence.std()
ic_pearson= ic_covariance/(ic_combat*ic_intelligence)
print(sc_pearson,ic_pearson)


# --------------
#Code starts here
#Calculate the value of quantile=0.99 for the column Total and store the value in the variable named total_high
total_high = data['Total'].quantile(q = 0.99)

super_best=data[data['Total']>total_high]

super_best_names=list(super_best['Name'])

print(super_best_names)


# --------------
#Code starts here
fig,(ax_1,ax_2,ax_3)=plt.subplots(nrows = 1 , ncols = 3, figsize=(20,10))
ax_1.boxplot(data['Intelligence'], meanline = True, showmeans = True)
ax_1.set_title('Intelligence')
ax_2.boxplot(data['Speed'], meanline = True, showmeans = True)
ax_2.set_title('Speed')
ax_3.boxplot(data['Power'], meanline = True, showmeans = True)
ax_3.set_title('Power')
plt.show()


