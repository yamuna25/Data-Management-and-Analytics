
exti<-system.time({
  #opening output file to store results
  sink("output.txt", split=TRUE)
  #importing arules library for implementing apriori
  library(arules)
  #importing arulesViz library to create graphs
  library(arulesViz)
  #Reading the input dataset
  trans<-read.transactions("historical-senate-predictions.csv",format = "basket", sep=",", rm.duplicates=TRUE)
  #creating rules calling apriori funtion with parameters
  rules<-apriori(trans,parameter=list(minlen=2,supp=0.1,conf=0.2))
  #to view the summary of rules
  summary(rules)
  #to view all the rules created
  inspect(rules)
  #creating plot to view the rules
  jpeg('plot1.jpg')
  plot(rules)
  dev.off()
  jpeg('plot2.jpg')
  plot(rules, method="graph", control=list(type="items"))
  dev.off()
  #closing output file
  sink()
  # Stop the clock
})
print(exti)