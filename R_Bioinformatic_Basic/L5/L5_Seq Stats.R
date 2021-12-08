############################
### Sequence statistics  ###
############################

library(seqinr)
##Ex1
#get data
choosebank("genbank")
Q1 <- query("Q1", "SP=Schistosoma mansoni AND M=dna")
Q1$nelem
#extract sequence
MySeq <- getSequence(Q1$req[[10]])
MySeqName <- getName(Q1$req[[10]])

closebank()

#export data
write.fasta(MySeq, MySeqName, file.out = "Seq10.fasta")

#read data
MySeq <- read.fasta("Seq10.fasta")
MySeq<- MySeq[[1]]

#Seq Stats..
length(MySeq)

#Base composition
bases <- table(MySeq)
plot(bases)
barplot(bases)

#word composition
words <- count(MySeq, 1)
words["a"]

words <- count(MySeq, 2)
words["cg"]

words <- count(MySeq, 3)
words["agt"]

#GC content
GC_per = GC(MySeq)

#My function!
Mycount <- table(MySeq)
myGC <- sum(Mycount["c"], Mycount["g"])/sum(Mycount)

#Ex2
#get the data
choosebank("refseqViruses")
Q2 <- query("Q2", "AC=NC_001477")
MySeq <- getSequence(Q2$req[[1]])
closebank()

#CG Variation
slidingwindowplot(2000, MySeq)
slidingwindowplot(3000, MySeq)
slidingwindowplot(1000, MySeq)


#Ex3
#Calculate the CG content
word_frq = count(MySeq, 2)/sum(count(MySeq, 2)) 
Base_frq = count(MySeq, 1)/sum(count(MySeq, 1)) 
raho = word_frq["cg"]/(Base_frq["c"] * Base_frq["g"])
