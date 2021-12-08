#-----------------------------------
library(tidyverse)
library(dplyr)
library(gdata)
library(ggplot2)
library(janitor)   #convert row to column names
library(lubridate) #convert char to date datatype
library(knitr)     #create knitr table

#Set work space
setwd("C:/Users/jacky/Documents/R_Project/Huynh_Truc_midterm")


#-----------------------------------------------------------
#'
#' Objective: Function to read the data from the csv file
#'  and store it in local dataframe
#'
#' Parameter: the file name as a string value(file.name)
#'
#' Return: un-tidy data frame
#'
read.data.input <- function(file.name)
{
  un.clean.data <-
    read.csv(
      file.name ,
      header = FALSE,
      quote = "\"",
      stringsAsFactors = FALSE,
      strip.white = TRUE
    )
  
  
  returnValue(un.clean.data)
}

#-----------------------------------------------------------
#'
#' Fuction to create sequence vector
#'
#' Parmeter: minimum number (min.num)
#' Parmeter: maximum number (max.num)
#'
#' Return: a vector of column index
vector.creator <- function(min.num, max.num)
{
  cols.nums <- c()
  cols.nums[1] = min.num
  for (i in seq(min.num, max.num, 1)) {
    cols.nums[i] = i + 1
  }
  returnValue(cols.nums)
}
#-----------------------------------------------------------
#'
#' Objective: Get the total number of case in the same country
#'
#' Parameter: Receive an untidy data frame
#'
#' Return: return a cleaner dataframe
#'
get.country.total.case <- function (un.clean.data)
{
  #clear unnecessary column latitude, longtitude, Province, State
  un.clean.data$V3 <- NULL
  un.clean.data$V4 <- NULL
  un.clean.data$V1 <- NULL
  # store the first column to sort the data
  col.data.name <- data.frame(un.clean.data[1, ])
  # removing first row to get the sum of each country
  temp.data <- un.clean.data[-(1), ]
  #Call vector Creator to create a vector to store column index
  cols.nums <- vector.creator(2, 60)
  #convert char column to integer column
  temp.data[cols.nums] <- sapply(temp.data[cols.nums], as.numeric)
  #sum up all state/province in one country
  clean.data <- aggregate(. ~ V2, temp.data, sum)
  #add the first row back to the datafra
  clean.data <- rbind(col.data.name, clean.data)
  returnValue(clean.data)
}

#-----------------------------------------------------------
#'
#' Objective: tidy the dataframe
#' Objective: adjust all datatype, column names, and values correctly
#'
#' Parameter: Receive an untidy data frame
#'
#' Return: return tidy dataframe
#'
tidy.dataframe <- function(clean.data)
{
  #Change the top row to column
  temp.data <- data.frame(t(clean.data))
  #
  temp.data <-
    data.frame(lapply(temp.data, as.character), stringsAsFactors = FALSE)
  #Change the first value to Date
  temp.data[1, 1] <- 'Date'
  clean.data <- data.frame(temp.data, header = TRUE)
  #Convert first row to column header
  clean.data <- temp.data %>%
    row_to_names(row_number = 1) %>%
    clean_names()
  #Convert first column to date data type
  clean.data <- clean.data %>%
    mutate(date = mdy(date))
  #Create the column vector
  cols.nums <- vector.creator(2, 166)
  # Convert Character into numeric
  clean.data[cols.nums] <- sapply(clean.data[cols.nums], as.numeric)
  returnValue(clean.data)
}

#-----------------------------------------------------------
#'
#' Import and Tidy data from the Confirmed.csv
#'
#Import the data from csv file
un.clean.data <-
  read.data.input('data/time_series_19-covid-Confirmed.csv')
# Get the sum of case in each country
clean.data <- get.country.total.case(un.clean.data)
# Tidy the data set
confirmed.case <- tidy.dataframe(clean.data)

#-----------------------------------------------------------
#'
#' Import and Tidy data from the Deaths.csv
#'
#Import the data from csv file
un.clean.data <-
  read.data.input('data/time_series_19-covid-Deaths.csv')
# Get the sum of case in each country
clean.data <- get.country.total.case(un.clean.data)
# Tidy the data set
deaths.case <- tidy.dataframe(clean.data)


#-----------------------------------------------------------
#'
#' Import and Tidy data from the Recovered.csv
#'
#Import the data from csv file
un.clean.data <-
  read.data.input('data/time_series_19-covid-Recovered.csv')
# Get the sum of case in each country
clean.data <- get.country.total.case(un.clean.data)
# Tidy the data set
recovered.case <- tidy.dataframe(clean.data)

#-------------------------------------------------
#'
#' Remove un-use data frame
#'
rm("un.clean.data", "clean.data")

#-------------------------------------------------
#'
#' Calculate worldwide total death, recoved, and confirmed
#'
# Calculate the total death world wide each day
total.death <- data.frame(rowSums(deaths.case[, 2:167]))
# Calculate the total confirmed world wide each day
total.confirmed <- data.frame(rowSums(confirmed.case[, 2:167]))
# Calculate the total recovered case world wide each day
total.recovered <- data.frame(rowSums(recovered.case[, 2:167]))
# Get the date
date.data <- data.frame(confirmed.case[1])
# Combine the 4 data frame to the report day
worldwide.trend <-
  cbind(date.data, total.confirmed, total.death, total.recovered)
colnames(worldwide.trend) <-
  c("date", "confirmed", "death", "recovered")


#-------------------------------------------------
#'
#' Remove un-use data frame
#'
rm("total.death",
   "total.confirmed",
   "total.recovered",
   "date.data")
#-------------------------------------------------
#' 2.1
#' Print out plot
#'
ggplot(data = worldwide.trend) +
  geom_line(mapping = aes(x = date,
                          y = confirmed, color = "confirmed")) +
  geom_point(mapping = aes(x = date,
                           y = confirmed, color = "confirmed")) +
  geom_line(mapping = aes(x = date,
                          y = death, color = "death")) +
  geom_point(mapping = aes(x = date,
                           y = death, color = "death")) +
  geom_line(mapping = aes(x = date,
                          y = recovered, color = "recovered")) +
  geom_point(mapping = aes(x = date,
                           y = recovered, color = "recovered"))
#-------------------------------------------------
#'
#' 2.2 Case world by date
#' Create active column
#'

worldwide.trend$active <- worldwide.trend$confirmed -
  worldwide.trend$death - worldwide.trend$recovered
# Create recovery % column
worldwide.trend$recovery.percent <-
  round((worldwide.trend$recovered / worldwide.trend$confirmed) * 100,
        3)
# Create mortality % column
worldwide.trend$mortality.percent <-
  round((worldwide.trend$death / worldwide.trend$confirmed) * 100, 3)

# Knit table
dt <- worldwide.trend[1:10,]
dt %>%
  kable()
#-------------------------------------------------
#'
#' 2.3 Case world by country
#' Create active column
#' #-------------------------------------------------
#'
#' Calculate worldwide total death, recoved, and confirmed
#'
# Calculate the total death world wide each day
total.death <- data.frame(colSums(deaths.case[1:60, -1]))
# Calculate the total confirmed world wide each day
total.confirmed <- data.frame(colSums(confirmed.case[1:60, -1]))
# Calculate the total recovered case world wide each day
total.recovered <- data.frame(colSums(recovered.case[1:60, -1]))
# Get the country name
df <- tibble::rownames_to_column(total.confirmed, "country")
# add the data together
case.by.country <- cbind(df, total.death, total.recovered)
colnames(case.by.country) <-
  c("country", "confirmed", "death", "recovered")
#-------------------------------------------------
#'
#' Create active column
case.by.country$active <- case.by.country$confirmed -
  case.by.country$death - case.by.country$recovered
# Create recovery % column
case.by.country$recovery.percent <-
  round((case.by.country$recovered / case.by.country$confirmed) * 100,
        3)
# Create mortality % column
case.by.country$mortality.percent <-
  round((case.by.country$death / case.by.country$confirmed) * 100, 3)

case.by.country <-
  case.by.country[order(-case.by.country$confirmed),]

# Knit table
df <- case.by.country[1:10,]
row.names(df) <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
df %>%
  kable()
#-------------------------------------------------
#'
#' Remove un-use data frame
#'
rm("total.death", "total.confirmed", "total.recovered", "df")



#-------------------------------------------------
#'
#' 2.4
#' Create new table without china
#'
#' Calculate worldwide total death, recoved, and confirmed
#'
# exclude china
exclude.china <- function(dataframe)
{
  local.frame <- dataframe
  local.frame$china <- NULL
  # Calculate the total death world wide each day
  local.frame <-
    data.frame(rowSums(local.frame[, 2:166]))
}

# Calculate the total confirmed world wide each day
total.death <- exclude.china(deaths.case)
total.confirmed <- exclude.china(confirmed.case)
total.recovered <- exclude.china(recovered.case)

# Get the date
date.data <- data.frame(confirmed.case[1])

# Combine the 4 data frame to the report day
worldwide.no.china <-
  cbind(date.data, total.confirmed, total.death, total.recovered)
colnames(worldwide.no.china) <-
  c("date", "confirmed", "death", "recovered")
#-------------------------------------------------
#'
#' Remove un-use data frame
#'
rm("total.death",
   "total.confirmed",
   "total.recovered",
   "date.data")
#-------------------------------------------------
#' 2.4
#' Print out plot
#'
ggplot(data = worldwide.no.china) +
  geom_line(mapping = aes(x = date,
                          y = confirmed, color = "confirmed")) +
  geom_point(mapping = aes(x = date,
                           y = confirmed, color = "confirmed")) +
  geom_line(mapping = aes(x = date,
                          y = death, color = "death")) +
  geom_point(mapping = aes(x = date,
                           y = death, color = "death")) +
  geom_line(mapping = aes(x = date,
                          y = recovered, color = "recovered")) +
  geom_point(mapping = aes(x = date,
                           y = recovered, color = "recovered"))

#-------------------------------------------------
#'
#' 2.5 Case world by date
#' Create active column
worldwide.no.china$active <- worldwide.no.china$confirmed -
  worldwide.no.china$death - worldwide.no.china$recovered
# Create recovery % column
worldwide.no.china$recovery.percent <-
  round((worldwide.no.china$recovered / worldwide.no.china$confirmed) *
          100,
        3)
# Create mortality % column
worldwide.no.china$mortality.percent <-
  round((worldwide.no.china$death / worldwide.no.china$confirmed) * 100,
        3)

# Knit table
dt <- worldwide.no.china[1:10,]
dt %>%
  kable()

#---------------------------------------------------------
clean.data.2 <- function(un.clean.data)
{
  newdata <- un.clean.data[which(un.clean.data$V2 == 'US'),]
  temp.data <- data.frame(un.clean.data[1, ])
  clean.data <- rbind(temp.data, newdata)
  clean.data$V2 <- NULL
  clean.data$V3 <- NULL
  clean.data$V4 <- NULL
  temp.data <- data.frame(t(clean.data))
  #
  temp.data <-
    data.frame(lapply(temp.data, as.character), stringsAsFactors = FALSE)
  #Change the first value to Date
  temp.data[1, 1] <- 'Date'
  clean.data <- data.frame(temp.data, header = TRUE)
  #Convert first row to column header
  clean.data <- temp.data %>%
    row_to_names(row_number = 1) %>%
    clean_names()
  #Convert first column to date data type
  clean.data <- clean.data %>%
    mutate(date = mdy(date))
  #Create the column vector
  cols.nums <- vector.creator(2, 247)
  # Convert Character into numeric
  clean.data[cols.nums] <- sapply(clean.data[cols.nums], as.numeric)
  returnValue(clean.data)
}

#Import the US confirmed data from csv file
un.clean.data <-
  read.data.input('data/time_series_19-covid-Confirmed.csv')
clean.data <- clean.data.2(un.clean.data)
total.confirmed.us <- clean.data

#Import the US deaths data from csv file
un.clean.data <-
  read.data.input('data/time_series_19-covid-Deaths.csv')
clean.data <- clean.data.2(un.clean.data)
total.deaths.us <- clean.data

#Import the US recovered data from csv file
un.clean.data <-
  read.data.input('data/time_series_19-covid-Recovered.csv')
clean.data <- clean.data.2(un.clean.data)
total.recovered.us <- clean.data

#Create the US summary Cases by date
us.summary.cases <- cbind(
  data.frame(total.recovered.us[, 1]),
  data.frame(rowSums(total.confirmed.us[, 2:247])),
  data.frame(rowSums(total.deaths.us[, 2:247])),
  data.frame(rowSums(total.recovered.us[, 2:247]))
)

# Create the US summary cases by col names
colnames(us.summary.cases) <-
  c("date", "confirmed", "death", "recovered")

rm("un.clean.data", "clean.data", "temp.data")

#-------------------------------------------------
#' 3.1
#' Print out plot
#'
attach(us.summary.cases)
ggplot(data = us.summary.cases) +
  geom_line(mapping = aes(x = date,
                          y = confirmed, color = "confirmed")) +
  geom_point(mapping = aes(x = date,
                           y = confirmed, color = "confirmed")) +
  geom_line(mapping = aes(x = date,
                          y = death, color = "death")) +
  geom_point(mapping = aes(x = date,
                           y = death, color = "death")) +
  geom_line(mapping = aes(x = date,
                          y = recovered, color = "recovered")) +
  geom_point(mapping = aes(x = date,
                           y = recovered, color = "recovered"))
detach(us.summary.cases)
#-------------------------------------------------
#'
#' 3.2 Case world by date
#' Create active column
#'
attach(us.summary.cases)
us.summary.cases$active <- confirmed - death - recovered
# Create recovery % column
us.summary.cases$recovery.percent <-
  round((recovered / confirmed) * 100, 3)

# Create mortality % column
us.summary.cases$mortality.percent <-
  round((death / confirmed) * 100, 3)
detach(us.summary.cases)
# Knit table
dt <- us.summary.cases[1:10,]
dt %>%
  kable()

#Create the US summary Cases by state and province
us.summary.cases.by.state <- cbind(data.frame(colSums(total.confirmed.us[,-1])),
                                   data.frame(colSums(total.deaths.us[,-1])),
                                   data.frame(colSums(total.recovered.us[,-1])))

us.summary.cases.by.state <-
  tibble::rownames_to_column(us.summary.cases.by.state, "state.province")
colnames(us.summary.cases.by.state) <-
  c("state.province", "confirmed", "death", "recovered")

attach(us.summary.cases)
us.summary.cases$active <- confirmed - death - recovered
# Create recovery % column
us.summary.cases$recovery.percent <-
  round((recovered / confirmed) * 100, 3)

# Create mortality % column
us.summary.cases$mortality.percent <-
  round((death / confirmed) * 100, 3)
detach(us.summary.cases)
# Knit table
dt <- us.summary.cases[1:10,]
dt %>%
  kable()
