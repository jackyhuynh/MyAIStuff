##################################
#LEc 9
###################################
library("seqinr")
#Ex1:
#read the file
mySeq = getSequence(read.fasta(file = "Q9CD83.fasta.txt"))
#get the length
length(mySeq[[1]])
#Print the amino acid composition
t = table(mySeq[[1]])
t["k"]
plot(t)

#Ex2
#retrieve sequence data
library("seqinr")
choosebank("swissprot")
leprae<- query("leprae", "AC=Q9CD83")
lepraeseq <- getSequence(q1$req[[1]])
ulcerans<-query("ulcerans", "AC=A0PQ23")
ulceransseq <- getSequence(ulcerans$req[[1]])
closebank()
#in case of the error "unknown accession number"
#download it and reload it
ulcerans = read.fasta(file = "A0PQ23.fasta.txt")
ulceransseq = getSequence(ulcerans[[1]])

# Display the contents of "lepraeseq"
lepraeseq
ulceransseq = toupper(ulceransseq)
dotPlot(lepraeseq, ulceransseq)

#scoring matrices
library(Biostrings)
data(package="Biostrings")
data(BLOSUM62)
BLOSUM62 # Print out the data
B62 = BLOSUM62  # show the data in viewer

#Ex3
s1<-"PAWHEAE"
s2<-"HEAGAWGHEE"
globalAligns1s2 <- pairwiseAlignment(s1, s2, substitutionMatrix = "BLOSUM50", gapOpening = -2, gapExtension = -8, scoreOnly = FALSE)
globalAligns1s2
globalAligns1s2 <- pairwiseAlignment(s1, s2, substitutionMatrix = "PAM250", gapOpening = -2, gapExtension = -8, scoreOnly = FALSE)
globalAligns1s2

#Ex4
#load the data
leprae = read.fasta(file = "Q9CD83.fasta.txt")
lepraeseq = getSequence(leprae[[1]])
ulcerans = read.fasta(file = "A0PQ23.fasta.txt")
ulceransseq = getSequence(ulcerans[[1]])

lepraeseqstring <- toupper(c2s(lepraeseq))
ulceransseqstring <- toupper(c2s(ulceransseq))
globalAlignLepraeUlcerans <- pairwiseAlignment(lepraeseqstring, ulceransseqstring,
                                               substitutionMatrix = BLOSUM50, gapOpening = -2, gapExtension = -8, scoreOnly = FALSE)
globalAlignLepraeUlcerans # Print out the optimal global alignment and its score
localAlignLepraeUlcerans <- pairwiseAlignment(lepraeseqstring, ulceransseqstring,type="local",
                                              substitutionMatrix = BLOSUM50, gapOpening = -2, gapExtension = -8, scoreOnly = FALSE)
localAlignLepraeUlcerans
printPairwiseAlignment(localAlignLepraeUlcerans, chunksize = 40)
                                              
#stat significance
#test...
#be careful with expected parameter data types
randomseqs <- generateSeqsWithMultinomialModel('PAWHEAE',10)
randomseqs[1:5] # Print out the first 10 random sequences

randomseqs <- generateSeqsWithMultinomialModel(lepraeseq,10)

randomscores <- double(10) # Create a numeric vector with 1000 elements
for (i in 1:10)
{
  score <- pairwiseAlignment(lepraeseqstring, toupper(c2s(randomseqs[i])), substitutionMatrix = "BLOSUM50",
                             gapOpening = -2, gapExtension = -8, scoreOnly = TRUE)
  randomscores[i] <- score
}
hist(randomscores, col="blue") # Draw a red histogram
#The number of random alignments scoring >= actual alignement
sum(randomscores > 627)
#the p-value
p = sum(randomscores > 627)/length(randomscores)
p
