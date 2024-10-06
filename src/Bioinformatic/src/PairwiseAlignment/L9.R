library(seqinr)
library(Biostrings)
data("BLOSUM50")


choosebank("swissprot")
Q1 <- query("Q1", "AC=Q9CD83")
Q2 <-read.fasta("A0PQ23.fasta")

#
Seq11<- getSequence(Q1[['req']][[1]])
Seq22<- toupper(getSequence(Q2[[1]]))

# DotPlot
dotPlot(Seq11,toupper(Seq22))

Seq4 <- "PAWHEAE"
Seq5 <- "HEAGAWGHEE"

pairwiseAlignment(Seq4, Seq5, gapOpening = -2, gapExtension = -8,substitutionMatrix =BLOSUM50)

pairwiseAlignment(Seq4, Seq5, gapOpening = -2, gapExtension = -8,substitutionMatrix =PAM250)

AlignGlobal<- pairwiseAlignment(c2s(Seq11), c2s(Seq22), gapOpening = -2, gapExtension = -8,substitutionMatrix =BLOSUM50)

AlignLobal<-pairwiseAlignment(c2s(Seq11), c2s(Seq22), gapOpening = -2, gapExtension = -8,substitutionMatrix =BLOSUM50, type="local")

printPairwiseAlignment(Align)
printPairwiseAlignment(AlignLobal)

Multi<-generateSeqsWithMultinomialModel(Seq22,10)
