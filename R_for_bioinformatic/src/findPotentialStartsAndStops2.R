findPotentialStartsAndStops2 <- function(MySeq)
{
  # Define a vector with the sequences of potential start and stop codons
  codons <- c("atg", "taa", "tag", "tga")
  
  # Find the start positions of all occurrences of "atg" in sequence "sequence"
  positions <- start(matchPattern("atg", MySeq ))
  # Find the total number of potential start and stop codons in sequence "sequence"
  numoccurrences <- length(positions)
  # Make a vector "types" containing "numoccurrences" copies of "codon"
  types <- rep("atg", numoccurrences)
  
  # Find the number of occurrences of each type of potential start or stop codon
  for (i in 2:4)
  {
    codon <- codons[i]
    # Find the start positions of all occurrences of "codon" in sequence "sequence"
    codonpositions <- start(matchPattern(codon,MySeq ))
    # Find the total number of potential start and stop codons in sequence "sequence"
    numoccurrences <- length(codonpositions)
    # Add the vector "codonpositions" to the end of vector "positions":
    positions <- append(positions, codonpositions, after=length(positions))
    # Add the vector "rep(codon, numoccurrences)" to the end of vector "types":
    types <- append(types, rep(codon, numoccurrences), after=length(types))
  }
  # Sort the vectors "positions" and "types" in order of position along the input sequence:
  indices <- order(positions)
  positions <- positions[indices]
  types <- types[indices]
  # Return a list variable including vectors "positions" and "types":
  mylist <- list(positions,types)
  names(mylist) <- c("positions", "types")
  return(mylist)
}