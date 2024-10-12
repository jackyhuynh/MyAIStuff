printPairwiseAlignment <- function(alignment, chunksize=60, returnlist=FALSE)
{
  require(Biostrings) # This function requires the Biostrings package
  seq1aln <- pattern(alignment) # Get the alignment for the first sequence
  seq2aln <- subject(alignment) # Get the alignment for the second sequence
  alnlen <- nchar(seq1aln) # Find the number of columns in the alignment
  starts <- seq(1, alnlen, by=chunksize)
  n <- length(starts)
  seq1alnresidues <- 0
  seq2alnresidues <- 0
  for (i in 1:n) {
    chunkseq1aln <- substring(seq1aln, starts[i], starts[i]+chunksize-1)
    chunkseq2aln <- substring(seq2aln, starts[i], starts[i]+chunksize-1)
    # Find out how many gaps there are in chunkseq1aln:
    gaps1 <- countPattern("-",chunkseq1aln) # countPattern() is from Biostrings package
    # Find out how many gaps there are in chunkseq2aln:
    gaps2 <- countPattern("-",chunkseq2aln) # countPattern() is from Biostrings package
    # Calculate how many residues of the first sequence we have printed so far in the alignment:
    seq1alnresidues <- seq1alnresidues + chunksize - gaps1
    # Calculate how many residues of the second sequence we have printed so far in the alignment:
      seq2alnresidues <- seq2alnresidues + chunksize - gaps2
    if (returnlist == 'FALSE')
    {
      print(paste(chunkseq1aln,seq1alnresidues))
      print(paste(chunkseq2aln,seq2alnresidues))
      print(paste(' '))
    }
  }
  if (returnlist == 'TRUE')
  {
    vector1 <- s2c(substring(seq1aln, 1, nchar(seq1aln)))
    vector2 <- s2c(substring(seq2aln, 1, nchar(seq2aln)))
    mylist <- list(vector1, vector2)
    return(mylist)
  }
}