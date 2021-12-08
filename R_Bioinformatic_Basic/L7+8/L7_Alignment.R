library(seqinr)
choosebank("swissprot")
leprae <- query("leprae", "AC=Q9CD83")
lepraeseq <- getSequence(leprae$req[[1]])
ulcerans<- query("ulcerans", "AC=A0PX17")
ulceransseq <- getSequence(ulcerans$req[[1]])
dotPlot(lepraeseq, ulceransseq)

#alignment
library(Biostrings)
s1 <- "GAATTC"
s2 <- "GATTA"
sigma <- nucleotideSubstitutionMatrix(match = 2, mismatch = -1, baseOnly = TRUE)
globalAligns1s2 <- pairwiseAlignment(s1, s2, substitutionMatrix = sigma,
                                       gapOpening = -2,
                                       gapExtension = -8, scoreOnly = FALSE)
globalAligns1s2
localAligns1s2 <- pairwiseAlignment(s1, s2, substitutionMatrix = sigma,
                                     gapOpening = -2,
                                     gapExtension = -8, scoreOnly = FALSE, type="local")

#Ex
#get the data
choosebank("refseqViruses")
Q1 <- query("Q1", "AC=NC_001477")
MySeq1 <- DNAString(c2s(getSequence(Q1$req[[1]])))
Q2 <- query("Q2", "AC=NC_001474")
MySeq2 <- DNAString(c2s(getSequence(Q2$req[[1]])))
globalAlign3 <- pairwiseAlignment(MySeq1, MySeq2, substitutionMatrix = sigma,
                                     gapOpening = -2,
                                     gapExtension = -8, scoreOnly = TRUE)
  
closebank()
