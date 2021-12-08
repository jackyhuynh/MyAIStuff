
#------------------------------------------------------------------------------ 
# STEP 1: READ DATA & PREPARE DATA FRAME
#------------------------------------------------------------------------------
# libray for needed package
library(dplyr)
library("arules")
library(foreign)
library(bannerCommenter)

#------------------------------------------------------------------------------ 
# STEP 1: READ DATA & PREPARE DATA FRAME
# 
#read the data from the data file
adult <- read.csv("~/R/DataMining/HW2/adult.data", header = FALSE)

#Assign header
names(adult) <-
  c(
    "age",
    "workclass",
    "fnlwgt",
    "education",
    "educationNum",
    "maritalStatus",
    "occupation",
    "relationship",
    "race",
    "sex",
    "capitalGain",
    "capitalLoss",
    "hoursPerWeek",
    "naitiveCountry",
    "salary"
  )
#Review
summary(adult)
str(adult)

#------------------------------------------------------------------------------
# STEP 2: TRANSFORM DATA:
#   Convert numeric to category
#   Create data frame
#   Delete the non-category data
# 
# Convert numeric to category
adult$age <- ifelse(adult$age %in% 0:29,
                    "young",
                    ifelse(
                      adult$age %in% 30:49,
                      "middle-aged",
                      ifelse(adult$age %in% 50:69, "senior", "old")
                    ))
# Convert numeric to category
adult$capitalGain <- ifelse(
  adult$capitalGain <= 0,
  "none ",
  ifelse(
    adult$capitalGain %in% 1:1999,
    "small ",
    ifelse(adult$capitalGain %in% 2000:4999, "medium", "high")
  )
)
# Convert numeric to category
adult$capitalLoss <- ifelse(
  adult$capitalLoss <= 0,
  "none ",
  ifelse(
    adult$capitalLoss %in% 1:1999,
    "small ",
    ifelse(adult$capitalLoss %in% 2000:4999, "medium", "high")
  )
)
# Convert numeric to category
adult$hoursPerWeek <- ifelse(
  adult$hoursPerWeek <= 25,
  "half-time",
  ifelse(
    adult$hoursPerWeek %in% 26:40,
    "full-time",
    ifelse(adult$hoursPerWeek %in% 41:60, "overtime", "too-many")
  )
)
# Delete the fnlwgt variable
adult$fnlwgt <- NULL

#------------------------------------------------------------------------------
#QUESTION 1.1:
## (1) How many features are in the dataset?
#   > summary(adult_transaction.data)
#   transactions as itemMatrix in sparse format with
#   32562 rows (elements/itemsets/transactions) and
#   32689 columns (items) and a density of 0.0004305024
#
# (2) Briefly describe your procedure about the data preprocessing
#    Before create the transaction data, I need to clean up the
# original data frame by transfrom the continuous variable int to
# category. After that I need to remove the un-used variable (fnlwgt).
# Then I write the data to a new csv file, and read it in again as a transaction
# data file
#
# (3) If any, the program code for the data preprocessing
# Read that csv back in to create the transaction data
#   adult_transaction.data <- read.transactions(
#       file = "./tmp/adult_transaction.data.csv",
#       format = "basket",
#       sep = ",",
#       rm.duplicates = T,
#       cols = NULL
#     )
# create datafile and store in tmp folder
#   write(adult_transaction.data, file = "./tmp/adult_transaction.data", 
#         format ="basket")
# (4) adult_transaction.data file.
#   Include in the source file
#
# Create transaction data
# Create a temporary directory to store the transaction data fie
dir.create(path = "tmp", showWarnings = FALSE)

# Write our data.frame to a csv
write.csv(adult, "./tmp/adult_transaction.data.csv")

# Read that csv back in to create the transaction data
adult_transaction.data <- read.transactions(
  file = "./tmp/adult_transaction.data.csv",
  format = "basket",
  sep = ",",
  rm.duplicates = T,
  cols = NULL
)
#Review
summary(adult_transaction.data)
inspect(adult_transaction.data)
#Plot the 20 item to review the adult transaction.data
itemFrequencyPlot(
  adult_transaction.data,
  topN = 20,
  type = "absolute",
  main = "Absolute Item Frequency Plot"
)
#create datafile and store in tmp folder
write(adult_transaction.data, file = "./tmp/adult_transaction.data", format =
        "basket")
#------------------------------------------------------------------------------
#QUESTION 1.2
# (1) How many features are in the dataset?
#   Large matrix with 1064419218 elements
#
# (2) Briefly describe your procedure about the data preprocessing
#   Convert the transaction data "adult_transaction.data" in to binary matrix
#
# (3) If any, the program code for the data preprocessing
#   Create transaction data with binary by transform transaction data into matrix
#   adult_transaction.binary <- as(adult_transaction.data, "matrix")
#
# (4) adult_transaction_binary.data file.
#   Include in the source file
# 
# Create transaction data with binary by transform transaction data into matrix
adult_transaction.binary <- as(adult_transaction.data, "matrix")
#Review
str(adult_transaction.binary)
head.matrix(adult_transaction.binary)
#write adult_transaction_binary.data
write(adult_transaction.binary,
      file = "./tmp/adult_transaction_binary.data"
      )
#------------------------------------------------------------------------------
#QUESTION 2
# (1) How many frequent itemsets you get?
#     > rules.freq
#     set of 19 itemsets
#
# (2) Which algorithm did you use for solving this problem? 
#     Give the algorithm name and briefly describe it.
#     Apriori is an algorithm for frequent item set mining and association 
#     rule learning over relational databases. It proceeds by identifying 
#     the frequent individual items in the database and extending them to 
#     larger and larger item sets as long as those item sets appear sufficiently 
#     often in the database.
#     Source: https://en.wikipedia.org/wiki/Apriori_algorithm
#     
# (3) The result file name with frequent_itemsets_0.6s.txt
#     Include in source file
#
# (4) The computer program (software) you used, e.g., the website, or tool name. 
#     Or if any program you developed for this problem.
#     I am using R studio with the apriori() function
#     #Create apriori()
#     rules.freq <-
#       apriori(adult_transaction.data,
#               parameter = list(target = "frequent itemsets", support = 0.6))
#       more details: https://cran.r-project.org/web/packages/arules/arules.pdf
#       
# 
#Create apriori()
rules.freq <-
  apriori(adult_transaction.data,
          parameter = list(target = "frequent itemsets", support = 0.6))
#Review
rules.freq
rules.freq.text<-inspect(rules.freq)

#Write to source
write.csv(rules.freq.text,
      file = "./tmp/frequent_itemsets_0.6s.txt"
)

#------------------------------------------------------------------------------
#QUESTION 3:
# (1) How many closedimal itemsets you get?
#     5 itemsets
#     > summary(max.freq)
#     Mode   FALSE    TRUE 
#     logical      14       5 
#
# (2) Which algorithm did you use for solving this problem? 
#     Give the algorithm name and briefly describe it.
#     Answer:
#     Apriori is an algorithm for frequent item set mining and association 
#     rule learning over relational databases. It proceeds by identifying 
#     the frequent individual items in the database and extending them to 
#     larger and larger item sets as long as those item sets appear sufficiently 
#     often in the database.
#     Source: https://en.wikipedia.org/wiki/Apriori_algorithm
#
# (3) The result file named maximal_itemsets_0.6s.txt
#     Source file include
#
# (4) The computer program (software) you used, e.g., the website, or tool name. 
#     Or if any program you developed for this problem.
#     Answer:
#        I am using R studio with the apriori() function and is.maximal() function
#       details:
#       is.maximal(x,…)
#       # S4 method for itemMatrix
#       is.maximal(x)  
#     Provides the generic function and the S4 method is.maximal for finding maximal itemsets.
#     Source: https://www.rdocumentation.org/packages/arules/versions/1.6-6/topics/is.maximal
#
#Maximal frequent itemset
max.freq <- is.maximal(rules.freq)
#Review
View(max.freq)
summary(max.freq)

#Concatenate the rules and result to get a clearer view
write.csv(subset(cbind(rules.freq.text,max.freq), max.freq==TRUE),
          file = "./tmp/maximal_itemsets_0.6s.txt"
)

#------------------------------------------------------------------------------
#QUESTION 4
#Closed frequent itemset
# (1) How many cloased itemsets you get?
#     10 itemsets
#     > summary(closed.freq)
#     Mode   FALSE    TRUE 
#     logical       9      10 
#
# (2) Which algorithm did you use for solving this problem? 
#     Give the algorithm name and briefly describe it.
#     Answer:
#     Apriori is an algorithm for frequent item set mining and association 
#     rule learning over relational databases. It proceeds by identifying 
#     the frequent individual items in the database and extending them to 
#     larger and larger item sets as long as those item sets appear sufficiently 
#     often in the database.
#     Source: https://en.wikipedia.org/wiki/Apriori_algorithm
#     a logical vector with the same length as x indicating for 
#     each element in x if it is a closed itemset.
#
# (3) The result file named closed_itemsets_0.6s.txt
#     In source file
#
# (4) The computer program (software) you used, e.g., the website, 
#     or tool name. Or if any program you developed for this problem.
#     Answer:
#        I am using R studio with the apriori() function and is.closed() function
#     a logical vector with the same length as x indicating for 
#     each element in x if it is a closed itemset.
#
#Closed frequent itemset
closed.freq <- is.closed(rules.freq)
#Review
View(closed.freq)
summary(closed.freq)

#Concatenate the rules and result to get a clearer view
write.csv(subset(cbind(rules.freq.text,closed.freq), closed.freq==TRUE),
          file = "./tmp/closedimal_itemsets_0.6s.txt"
)
#------------------------------------------------------------------------------
#QUESTION 5
# (1) How many association rules you get?
#     > rules.association
#     set of 12 rules
# (2) What are the rules with the highest support and highest confidence?
#     rule 1
#   lhs                           rhs               support   confidence coverage  lift     count
#   [1]  {}                      => {none}          0.9999693 0.9999693  1.0000000 1.000000 32561
#
# (3) Which algorithm did you use for solving this problem? 
#     Give the algorithm name and briefly describe it.
#     Answer:
#     Apriori is an algorithm for frequent item set mining and association 
#     rule learning over relational databases. It proceeds by identifying 
#     the frequent individual items in the database and extending them to 
#     larger and larger item sets as long as those item sets appear sufficiently 
#     often in the database.
#     Source: https://en.wikipedia.org/wiki/Apriori_algorithm

# (4) The result file named association_rules_0.6s_0.9c.txt
# (5) The computer program (software) you used, e.g., the website, or tool name. 
#     Or if any program you developed for this problem.
#     Answer:
#       I am using R studio with the apriori() function 
# 
rules.association <-
  apriori(adult_transaction.data, parameter = list(supp = 0.6, conf = 0.9))
#Review
inspect(rules.association)
rules.association

#Write to source
write.csv(inspect(rules.association),
          file = "./tmp/association_rules_0.6s_0.9c.txt"
)
