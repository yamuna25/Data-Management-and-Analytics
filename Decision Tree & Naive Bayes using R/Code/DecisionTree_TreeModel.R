exti<-system.time({
  #opening output file to store results
  sink("DToutput_R_TreeModel.txt", split=TRUE)
  library(C50)
  #opening dataset
  dataset <- "HR_comma_sep.csv"
  #reading dataset
  data <- read.table( file=dataset, header=TRUE, sep="," )
  #randomizing data
  data <- data[ sample( nrow( data ) ), ]
  #selecting the x and y columns and splitting train and test data
  X <- data[,1:9]
  y <- data[,10]
  trainX <- X[1:10500,]
  trainy <- y[1:10500]
  testX <- X[10501:14998,]
  testy <- y[10501:14998]
  trainy<-as.factor(trainy)
  str(trainy)
  #calling decisiontree classifier with train data
  dtclassifier <-C5.0( trainX, trainy )
  dtsummary<-summary( dtclassifier )
  print (dtsummary)
  print(dtclassifier)
  #predicting test data
  prediction <- predict( dtclassifier, testX, type="class" )
  accuracy <- sum( prediction == testy ) / length( prediction )
  confusion_matrix<-table(testy, Predicted=prediction)
  jpeg('decisiontree.jpg')
  plot(dtclassifier)
  dev.off()
  cat(sprintf("predicted:%s original: %s\n", prediction, testy))
  print("Confusion Matrix:")
  print(confusion_matrix)
  print ("Accuracy: ")
  print(accuracy)
  sink()
  # Stop the clock
})
print(exti)
