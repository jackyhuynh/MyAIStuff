library("seqinr")
source("printMultipleAlignment.R")
source("cleanAlignment.R")
library(tidyverse)

read.alignment(file="virus.phy", format = 'phylip')%>%printMultipleAlignment()

# Alignment Object
obj<-read.alignment(file="virus.phy", format = 'phylip')

# clean Alignment
cleanObj <- cleanAlignment(obj,30,30)

dist.alignment(obj)

scores <- read.table(file="score.qscores")

mean(scores$V5)


poorlyConservedVirusaln<-function(alignment,minpcgap)  {
  
  # make a copy of the alignment to store the new alignment in:
  newalignment <- alignment
  
  # find the number of sequences in the alignment
  numseqs <- alignment$nb
  
  # empty the alignment in "newalignment")
  for (j in 1:numseqs) { newalignment$seq[[j]] <- "" }
  
  # find the length of the alignment
  alignmentlen <- nchar(alignment$seq[[1]])
  
  # look at each column of the alignment in turn:
  for (i in 1:alignmentlen)
    # Travel through the length of the alignment
  {
    # see what percent of the letters in this column are non-gaps:
    gap <- 0
    for (j in 1:numseqs)
    {
      seqj <- alignment$seq[[j]]
      letterij <- substr(seqj,i,i)
      if (letterij == "-") { gap <- gap + 1}
    }
    pcgap <- (gap*100)/numseqs
    # Only consider this column if at least minpcnongap % of the letters are not gaps:
    if (pcgap >= minpcgap)
    {
      # see what percent of the pairs of letters in this column are identical
      for (j in 1:numseqs)
      {
        seqj <- alignment$seq[[j]]
        letterij <- substr(seqj,i,i)
        newalignmentj <- newalignment$seq[[j]]
        newalignmentj <- paste(newalignmentj,letterij,sep="")
        newalignment$seq[[j]] <- newalignmentj
      }
    }
  }
  return(newalignment)
}


LongestStretch <- function(alignment,maxpc)
{
  # make a copy of the alignment to store the new alignment in:
  newalignment <- alignment
  
  # find the number of sequences in the alignment
  numseqs <- alignment$nb
  
  # empty the alignment in "newalignment")
  for (j in 1:numseqs) { newalignment$seq[[j]] <- "" }
  
  # find the length of the alignment
  alignmentlen <- nchar(alignment$seq[[1]])
  
  # look at each column of the alignment in turn:
  for (i in 1:alignmentlen)
  {
    
      # see what percent of the pairs of letters in this column are identical:
      numpairs <- 0; numid <- 0
      # find the letters in all of the sequences in this column:
      for (j in 1:(numseqs-1))
      {
        seqj <- alignment$seq[[j]]
        letterij <- substr(seqj,i,i)
        for (k in (j+1):numseqs)
        {
          seqk <- alignment$seq[[k]]
          letterkj <- substr(seqk,i,i)
          if (letterij != "-" && letterkj != "-")
          {
            numpairs <- numpairs + 1
            if (letterij == letterkj) { numid <- numid + 1}
          }
        }
      }
      pcid <- (numid*100)/(numpairs)
      
      # Only consider this column if at least %minpcid of the pairs of letters are identical:
      if (pcid >= maxpc)
      {
        for (j in 1:numseqs)
        {
          seqj <- alignment$seq[[j]]
          letterij <- substr(seqj,i,i)
          newalignmentj <- newalignment$seq[[j]]
          newalignmentj <- paste(newalignmentj,letterij,sep="")
          newalignment$seq[[j]] <- newalignmentj
        }
      }
    
  }
  return(newalignment)
}