library(seqinr)
tablecode()

#Ex1
# random sequence
nucleotides <- c("a", "t", "c", "g") # Define the alphabet of nucleotides
probabilities1 <- c(0.2, 0.3, 0.3, 0.2) # Set the values of the probabilities
seqlength <- 200 # Set the length of the sequence
s<- sample(nucleotides, seqlength, rep=TRUE, prob=probabilities1) # Generate a
t = table(s)
# check distribution
t["a"]/length(s)
t["t"]/length(s)
t["g"]/length(s)
t["c"]/length(s)

#gene finding..
#method 1
# Find all ATGs in the sequence
library(Biostrings)
# Convert the vector to a string of characters
MySeq <- c2s(s)
matchPattern("tag",MySeq ) #stop codon
# extract a gene
substring(MySeq,76,81)

#method 2
findPotentialStartsAndStops2(MySeq)

#Ex2
#get the data
choosebank("refseqViruses")
Q2 <- query("Q2", "AC=NC_001477")
MySeq <- getSequence(Q2$req[[1]])
g <- findPotentialStartsAndStops2(c2s(MySeq))

#Ex3
plotPotentialStartsAndStops(c2s(MySeq))
#for the first 500 bases
s = c2s(MySeq[1:500])
plotPotentialStartsAndStops(s)
ORF <- findORFsinSeq(s)
plotORFsinSeq(s)
gene <- substring(s, ORF[[1]][1], ORF[[2]][1] )
nchar(gene)
seqinr::translate(s)
s = s2c(gene)

#Ex4
choosebank("refseqViruses")
Q2 <- query("Q2", "AC=NC_001477")
MySeq <- getSequence(Q2$req[[1]])
ORF <- findORFsinSeq(c2s(MySeq))
geneLen <- ORF[[3]]
max(geneLen)

#generate random sequences
randseqs <- generateSeqsWithMultinomialModel(dengueseqstring, 10)
# find ORF
randseqorflengths <- numeric() # Tell R that we want to make a new vector of numbers
for (i in 1:10)
{
  print(i)
  randseq <- randseqs[i] # Get the ith random sequence
  mylist <- findORFsinSeq(randseq) # Find ORFs in "randseq"
  lengths <- mylist[[3]] # Find the lengths of ORFs in "randseq"
  randseqorflengths <- append(randseqorflengths, lengths, after=length(randseqorflengths))
}

# plot a histogram of the lengths of the ORFs real vs. random
par(mfrow = c(1,2)) # Make a picture with two plots side-by-side (one row, two columns)
bins <- seq(0,11000,50) # Set the bins for the histogram
hist(randseqorflengths, breaks=bins, col="red", xlim=c(0,1000))
hist(orflengths, breaks=bins, col="red", xlim=c(0,1000))

#find the longest random gene
x = max(randseqorflengths)

#use it as a threshold, and discard all ORFs found in the real sequence that are shorter than this
summary(orflengths > x)

#find and use the 99th quantile as a threshold
quantile(randseqorflengths, probs=c(0.99))

# DotPlot to see what is different.
choosebank("swissprot")

Q1 <- query("Q1", "AC=Q9CD83")
Q2 <- query("Q2", "AC=A0Px17")

MySeq1 <- getSequence(Q1$req[[1]])
MySeq2 <- getSequence(Q2$req[[1]])

dotPlot(MySeq1,MySeq2)

library(Biostrings)

nucleotideSubstitutionMatrix(baseOnly=TRUE)
nucleotideSubstitutionMatrix(mismatch = -1)
nucleotideSubstitutionMatrix(match = 2)
# penalty of a mismatch