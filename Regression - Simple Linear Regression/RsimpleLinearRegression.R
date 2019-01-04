#Simple Linear Regression

#Importing DataSet

dataset = read.csv('Salary_Data.csv')

library(caTools)
set.seed(123)

split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)


# Fitting Simple Linear Regression to the Training set
regressor = lm(formula = Salary ~ YearsExperience,
               data = training_set)


# Predicting the Test set results
y_pred = predict(regressor, newdata = test_set)

# Vistualising the Training set results
# install.packages('ggplot2')

library(ggplot2)
ggplot() +
  geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary),
             color = 'red') +
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)),
            color = 'blue') +
  ggtitle('Salary Vs Experience (TrainingSet)') + 
  xlab('Years of Experience') +
  ylab('Salary')


