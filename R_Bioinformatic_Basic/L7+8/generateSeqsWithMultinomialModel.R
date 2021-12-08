generateSeqsWithMultinomialModel <- function(inputsequence, n)
{
  # Change the input sequence into a vector of letters
    require("seqinr") # This function requires the SeqinR package.
    #inputsequencevector <- s2c(inputsequence)
    inputsequencevector <- inputsequence
    # Find the frequencies of the letters in the input sequence "inputsequencevector":
    mylength <- length(inputsequencevector)
    mytable <- table(inputsequencevector)
    # Find the names of the letters in the sequence
    letters <- rownames(mytable)
    numletters <- length(letters)
    probabilities <- numeric() # Make a vector to store the probabilities of letters
    for (i in 1:numletters)
    {
      letter <- letters[i]
      count <- mytable[[i]]
      probabilities[i] <- count/mylength
    }
    # Make n random sequences using the multinomial model with probabilities "probabilities"
    seqs <- vector("list", n)
    for (j in 1:n)
    {
      seq <- sample(letters, mylength, rep=TRUE, prob=probabilities) # Sample
      seq <- c2s(seq)
      seqs[[j]] <- seq
    }
    
    
# Return the vector of random sequences
return(seqs)
}