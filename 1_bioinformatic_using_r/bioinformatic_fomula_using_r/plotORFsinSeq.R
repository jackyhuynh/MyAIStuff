plotORFsinSeq <- function(sequence)
{
  # Make vectors "positions" and "types" containing information on the positions of ATGs in the sequence:
    mylist <- findPotentialStartsAndStops2(sequence)
    positions <- mylist[[1]]
    types <- mylist[[2]]
    # Make vectors "orfstarts" and "orfstops" to store the predicted start and stop codons of ORFs
    orfstarts <- numeric()
    orfstops <- numeric()
    # Make a vector "orflengths" to store the lengths of the ORFs
    orflengths <- numeric()
    # Print out the positions of ORFs in the sequence:
    numpositions <- length(positions) # Find the length of vector "positions"
    # There must be at least one start codon and one stop codon to have an ORF.
    if (numpositions >= 2)
    {
      for (i in 1:(numpositions-1))
      {
        posi <- positions[i]
        typei <- types[i]
        found <- 0
        while (found == 0)
        {
          for (j in (i+1):numpositions)
          {
            posj <- positions[j]
            typej <- types[j]
            posdiff <- posj - posi
            posdiffmod3 <- posdiff %% 3
            orflength <- posj - posi + 3 # Add in the length of the stop codon
            if (typei == "atg" && (typej == "taa" || typej == "tag" || typej == "tga") && posdiffmod3 == 0)
            {
              # Check if we have already used the stop codon at posj+2 in an ORF
              numorfs <- length(orfstops)
              usedstop <- -1
              if (numorfs > 0)
              {
                for (k in 1:numorfs)
                {
                  orfstopk <- orfstops[k]
                  if (orfstopk == (posj + 2)) { usedstop <- 1 }
                }
              }
              if (usedstop == -1)
              {
                orfstarts <- append(orfstarts, posi, after=length(orfstarts))
                orfstops <- append(orfstops, posj+2, after=length(orfstops)) # Including the stop codon.
                orflengths <- append(orflengths, orflength, after=length(orflengths))
              }
              found <- 1
              break
            }
            if (j == numpositions) { found <- 1 }
          }
        }
      }
    }
    # Sort the final ORFs by start position:
    indices <- order(orfstarts)
    orfstarts <- orfstarts[indices]
    orfstops <- orfstops[indices]
    # Make a plot showing the positions of ORFs in the input sequence:
    # Draw a line at y=0 from 1 to the length of the sequence:
    x <- c(1,nchar(sequence))
    y <- c(0,0)
    plot(x, y, ylim=c(0,3), type="l", axes=FALSE, xlab="Nucleotide", ylab=
           ?????"Reading frame", main="Predicted ORFs")
    segments(1,1,nchar(sequence),1)
    segments(1,2,nchar(sequence),2)
    # Add the x-axis at y=0:
    axis(1, pos=0)
    # Add the y-axis labels:
    text(0.9,0.5,"+1")
    text(0.9,1.5,"+2")
    text(0.9,2.5,"+3")
    # Make a plot of the ORFs in the sequence:
    numorfs <- length(orfstarts)
    for (i in 1:numorfs)
    {
      orfstart <- orfstarts[i]
      orfstop <- orfstops[i]
      remainder <- (orfstart-1) %% 3
      if (remainder == 0) # +1 reading frame
      {
        rect(orfstart,0,orfstop,1,col="cyan",border="black")
      }
      else if (remainder == 1)
      {
        rect(orfstart,1,orfstop,2,col="cyan",border="black")
      }
      else if (remainder == 2)
      {
        rect(orfstart,2,orfstop,3,col="cyan",border="black")
      }
    }
}