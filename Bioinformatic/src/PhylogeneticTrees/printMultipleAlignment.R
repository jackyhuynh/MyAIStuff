printMultipleAlignment <- function(alignment, chunksize=60)
{
  # this function requires the Biostrings package
  require("Biostrings")
  # find the number of sequences in the alignment
  numseqs <- alignment$nb
  # find the length of the alignment
  alignmentlen <- nchar(alignment$seq[[1]])
  starts <- seq(1, alignmentlen, by=chunksize)
  n <- length(starts)
  # get the alignment for each of the sequences:
  aln <- vector()
  lettersprinted <- vector()
  for (j in 1:numseqs)
  {
    alignmentj <- alignment$seq[[j]]
    aln[j] <- alignmentj
    lettersprinted[j] <- 0
  }
  # print out the alignment in blocks of 'chunksize' columns:
  for (i in 1:n) { # for each of n chunks
    for (j in 1:numseqs)
    {
      alnj <- aln[j]
      chunkseqjaln <- substring(alnj, starts[i], starts[i]+chunksize-1)
      chunkseqjaln <- toupper(chunkseqjaln)
      # Find out how many gaps there are in chunkseqjaln:
      gapsj <- countPattern("-",chunkseqjaln) # countPattern() is from Biostrings package
      # Calculate how many residues of the first sequence we have printed so far in the alignment:
        lettersprinted[j] <- lettersprinted[j] + chunksize - gapsj
      print(paste(chunkseqjaln,lettersprinted[j]))
    }
    print(paste(' '))
  }
}