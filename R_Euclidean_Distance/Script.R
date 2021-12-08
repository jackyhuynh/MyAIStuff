# Needed library
library(readr)
library(tidyverse)
library(philentropy)

# Using Excel to import the ionosphere.data into Data.csv
MyRData <- read.csv("Data.csv", header = TRUE)

# View the data to analyze
View (MyRData)

#Using only 34 continuous attributes for analyst
MyRData<-MyRData %>% select(1:34)

#apply the distance function to compute the 
#L2 distance (Euclidean distance) between all pairs of data points.
distance(MyRData, method = "euclidean")

# Result of the first 10 pair
# Metric: 'euclidean'; comparing: 351 vectors.
#             v1       v2        v3       v4       v5        v6        v7       v8        v9
# v1   0.0000000 2.776359 1.1697276 4.772563 1.377347 3.0490724 1.5304711 4.803640 1.2050179
# v2   2.7763589 0.000000 3.3800330 4.454509 2.540531 2.7838832 2.7539302 4.859196 3.4724946
#           v10       v11      v12       v13      v14       v15      v16       v17      v18
# v1   3.564314 1.5055474 3.584336 1.3487913 3.113995 3.1023366 3.851302 2.2606502 6.728122
# v2   3.271473 3.4588373 5.073432 3.7733247 4.540863 4.8713059 2.901313 4.1755709 7.017637
# [ reached getOption("max.print") -- omitted 349 rows ]