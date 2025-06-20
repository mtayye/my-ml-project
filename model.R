# library(caret)

# train_model <- function() {
#   data(iris)
#   trainIndex <- createDataPartition(iris$Species, p = .8, list = FALSE)
#   trainData <- iris[trainIndex,]
#   testData <- iris[-trainIndex,]
  
#   model <- train(Species ~ ., data = trainData, method = "glm")
#   predictions <- predict(model, testData)
#   accuracy <- sum(predictions == testData$Species) / nrow(testData)
  
#   return(list(model = model, accuracy = accuracy))
# }
