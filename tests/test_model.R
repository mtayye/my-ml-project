library(testthat)
source("model.R")

test_that("Model accuracy is acceptable", {
  result <- train_model()
  expect_gt(result$accuracy, 0.8)
})
