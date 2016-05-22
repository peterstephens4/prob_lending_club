#  Peter Stephens
# 5/21/2016
#  Comparison of the "Amount.Requested" column with the "Amount.Funded.By.Investors"
#  column using Lending Club loan data.

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import subprocess

#  Clean the directory of old png files
p = subprocess.Popen("rm -rf *.png",  shell=True)

#  Read in Lending Club Data form git hub repository
loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

#  Clean Data:  Remove null value rows
loansData.dropna(inplace=True)

#   Generate plots for Amount.Requested
# Box Plot
plt.figure()
box_plot = loansData.boxplot(column='Amount.Requested', return_type='axes', vert=False)
plt.savefig("Box_Plot_Amount.Requested.png")
# Histogram
plt.figure()
hit_plot = loansData.hist(column='Amount.Requested')
plt.savefig("Histogram_Plot_Amount.Requested.png")
# QQ-plot of the normal distribution
plt.figure()  
qq_plot = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.savefig("QQ_Plot_Amount.Requested.png") 


#   Generate plots for Amount.Funded.By.Investors
# Box Plot
plt.figure()
box_plot = loansData.boxplot(column='Amount.Funded.By.Investors', return_type='axes', vert=False)
plt.savefig("Box_Plot_Amount_Funded_By_Investors.png")
# Histogram
plt.figure()
hit_plot = loansData.hist(column='Amount.Funded.By.Investors')
plt.savefig("Histogram_Plot_Amount_Funded_By_Investors.png")
# QQ-plot of the normal distribution
plt.figure()  
qq_plot = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.savefig("QQ_Plot_Amount_Funded_By_Investors.png")


