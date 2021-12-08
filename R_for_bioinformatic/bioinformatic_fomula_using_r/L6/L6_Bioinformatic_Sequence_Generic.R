library(seqinr)
library(Biostrings)


?matchPattern

S="atgcgtgacacctga"

matchPattern('atg',S)

STRT <- matchPattern("tga",S)

str(STRT)

matchPattern("tga",S)

?sample

Random_Seq <- c('a','c','g','t')
Pro_Seq <- c(0.2,0.3,0.3,0.2)
# replace have to be true to execute
My_Seq <- sample(Random_Seq, 700,replace = TRUE, prob = Pro_Seq)

table(My_Seq)

length(My_Seq)

My_Seq<-c2s(My_Seq)

matchPattern("atg",My_Seq)

matchPattern("tga",My_Seq)

?substring

MySeq <- c(My_Seq)

# Not work due to need of specific data structure.
findPotentialStartsAndStops(My_Seq)

findPotentialStartsAndStops2(My_Seq)

choosebank("genbank")
My_Seq1 <- read.fasta("DEN1_Seq.fasta")

setwd("C:/Users/jacky/Documents/R_Project/R_for_Bioinformatic/R_Bioinformatic_Basic")

Sequence1 <- getSequence(My_Seq1[[1]])

Sequence1 <- c2s(Sequence1)

findPotentialStartsAndStops2(Sequence1)

g<- getSequence(My_Seq1[[1]][1:500])

g<- c2s(g)

# translate what is that a potential gene or not. Open reading frame.
# 6 frames Analyze a sequences, looking for a gene in a sequence, and in reverse direction.
# How to locate an ORF.
Sequence1 <- getSequence(My_Seq1[[1]])

Sequence1 <- c2s(Sequence1)
plotPotentialStartsAndStops(Sequence1)

plotPotentialStartsAndStops(g)

plotORFsinSeq(g)

findORFsinSeq(g)

S1 <- substring(g, 298,318)

seqinr::translate(s2c(S1))

seqinr::translate(s2c(substring(g,371,480)))
# Open reading frame. Generate a random sequences. 
