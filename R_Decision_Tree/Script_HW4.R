library(dplyr) 

A <- c(1, 3, 2, 1, 3, 2, 75, 1, 3, 2, 2, 1, 2, 3, 2, 1)
View (A)

# 1.	Create a histogram of the data distribution. 
# You may create it by hand or any software.  Can you see the outliers visually? 
# Which one(s)? 

library(ggplot2)
hist(A)
# Outlier has the value of 75

# 2.	Compute the Z-value of each data point.
# Which of these values can be considered the most extreme value?

Data <- data.frame(A)

Data %>% 
  mutate(zscore = (A- mean(A))/sd(A))

# 3.	Determine the nearest neighbor (k=1) of each data point. 
# Which data points have the largest value of the nearest neighbor distance?  
# Are they the correct outliers? 
library(FNN)
get.knn(Data, k=1,algorithm=c("brute"))

# The data show that value with index [7] have the largest value of the nearest 
# neighbor distance. Thus it is a outlier.

# 4.	Apply a k-means clustering algorithm (k=2) to the data set.
# Which data points lie furthest from the two means (the centroids of the two 
# clusters) found? Are they the correct outliers? 

clusters <- kmeans(Data[,1], 2)

str(clusters)
Data$Borough <- as.factor(clusters$cluster)

clusters[["centers"]]


