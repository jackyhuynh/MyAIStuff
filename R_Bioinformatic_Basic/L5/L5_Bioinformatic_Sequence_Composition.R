library(seqinr)

choosebank("genbank")

# Q <- query("Q", "AC= ") giving 
# SP(name) or AC to retrieve the data.
Q <- query("Q", "SP=Schistosoma mansoni") 

# Length 
length(Q$req)

# Write the file to fasta file.
write.fasta(getSequence(Q$req[[100]]), getName(Q$req[[100]]), file.out = "Seq_100.fasta")

# Read the fasta file 
S <- read.fasta("Seq_100.fasta")

MySeq <- getSequence(S[[1]])
# Vectorize OPeration

#
t["a"]/sum(t)

plot(t)

t = count(MySeq,wordsize = 1)

t

library(ggplot2)

#
pie(t)

#
(t["c"]+t["g"])/sum(t)*100

# Same as GC
GC(MySeq)

choosebank("refseqViruses")

Q1<-query( "Q1", "AC=NC_001477")

slidingwindowplot(2000, getSequence(Q1$req[[1]]))

GC(getSequence(Q1$req[[1]]))

length(getSequence(Q1$req[[1]]))

vector = c()

for (val in 1:length(Q$req)){
  vector <- c(vector, length(getSequence(Q$req[[val]])))
}

sapply(vector,max())

t = count(getSequence(Q1$req[[1]]),wordsize = 2)

t2 = count(getSequence(Q1$req[[1]]),wordsize = 1)

(t["cg"]/(t2["c"]*t2["g"]))/sum(t)

getwd()
setwd("C:/Users/jacky/Documents/R_Project/R_for_Bioinformatic/R_Bioinformatic_Basic")

windowsize <- 200
inputseq <- getSequence(Q$req[[1]])

starts <- seq(1, length(inputseq)-windowsize, by = windowsize)

n <- length(starts) # Find the length of the vector "starts"

chunkGCs <- numeric(n) # Make a vector of the same length as vector "starts", but just containing zeroes

for (i in 1:n) {
  chunk <- inputseq[starts[i]:(starts[i]+windowsize-1)]
  chunkGC <- GC(chunk)
  print(chunkGC)
  chunkGCs[i] <- chunkGC
}
plot(starts,chunkGCs,type="b",xlab="Nucleotide start position",ylab="GC content")
