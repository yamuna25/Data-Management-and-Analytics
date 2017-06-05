
 README File for WEKA & R

 What is it?
 -----------
 Weka is a collection of machine learning algorithms for data mining tasks. 
 The algorithms can either be applied directly to a dataset or called from your
 own Java code. Weka contains tools for data pre-processing, classification, 
 regression, clustering, association rules, and visualization. It is also 
 well-suited for developing new machine learning schemes.

 R is a language and environment for statistical computing and graphics.

 How to run ?
 ------------
 
 WEKA:

 Import the data set i.e CSV file provided with this package. If any pre-processing
 is required then it can be done there itself. Apply the filter called NumericToNominal
 to convert all the integral values to String. Weka by default does not accepts the 
 integral values. Once done then navigate to Associate tab and select the support count
 and confidence rate. Click on Start and there will be result generated.

 R:

 Install R binaries and RStudio IDE. Open RStudio IDE. Go to tools and select install packages option. Type the name of package to be installed and press install. Install “arules” and “arulesViz” packages.


 How We have handled Noise in Data ?
 ———————————————————————————————————————————-

 Only Target attribute is set as class attribute in WEKA Tool.
 No other pre-processing was required.


 what is project folder contains ?
 ———————————————————————————————

 1.All the data set
 2.README file
 3.R Script
 4.Report
 5.output.txt
 6.historical-senate-predictions.csv file
