#####################
### Sequences     ###
#####################

#The bioconductor Package
#download
if (!require(BiocManager)) 
  install.packages("BiocManager", repos = "https://cran.r-project.org")
#istall specific packages
BiocManager::install(c("seqinR", "Biostrings", "GenomicRanges"))


#Ex 2
#read the sequence data file
library(seqinr)
mySeq <- read.fasta(file = "DEN1_Seq.fasta")

#Get the sequence data
s = getSequence(mySeq)

#Print the first 10 bases in the sequence
s[[1]][1:10]

##Ex3
choosebank()
choosebank("refseqViruses") 
Q<-query( "Q", "AC=NC_001477")
Q$name
Q$nelem
s<-getSequence(Q$req[[1]])
s[1:50]
closebank()

##Ex4
#get data
choosebank("genbank")
Q2 <- query("Q2", "SP=Schistosoma mansoni AND M=mrna")

#check data
Q2$nelem

#the accession numbers of the first 2?
Q2$req[[1]][1]
Q2$req[[2]][1]

#or
getName(Q2$req[[1]])

#export data
write.fasta(getSequence(Q2$req[[10]]), getName(Q2$req[[10]]), file.out = "Myfile2.fasta")
closebank()


getncbiseq <- function(accession)
{
  require("seqinr") 
  # this function requires the SeqinR R package
  # first find which ACNUC database the accession is stored in:
  dbs <- c("genbank","refseq","refseqViruses","bacterial")
  numdbs <- length(dbs)
  for (i in 1:numdbs)
  {
    db <- dbs[i]
    choosebank(db)
    # check if the sequence is in ACNUC database 'db':
    resquery <- try(query(".tmpquery", paste("AC=", accession)), silent = TRUE)
    if (!(inherits(resquery, "try-error")))
    {
      queryname <- "query2"
      thequery <- paste("AC=",accession,sep="")
      query(`queryname`,`thequery`)
      # see if a sequence was retrieved:
      seq <- getSequence(query2$req[[1]])
      closebank()
      return(seq)
    }
    closebank()
  }
}