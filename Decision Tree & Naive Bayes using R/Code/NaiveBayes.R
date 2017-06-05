
exti<-system.time({
  #opening output file to store results
  sink("NBoutput_R.txt", split=TRUE)
  #importing e1071 package
  library(e1071)
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
  #calling naivebayes classifier with train data
  nb_model <- naiveBayes(trainX,trainy)
  summary(nb_model)
  #predicting test data
  prediction<-predict(nb_model,testX) 
  print(nb_model)
  cat(sprintf("predicted:%s original: %s\n", prediction, testy))
  confusion_matrix<-table(pred=prediction,true=testy)
  print("Confusion Matrix:")
  print(confusion_matrix)
  accuracy<-mean(prediction==testy)
  print ("Accuracy: ")
  print(accuracy)
  sink()
  # Stop the clock
})
print(exti)