plotPotentialStartsAndStops <- function(sequence)
{
  # Make a plot showing the positions of the start and stop codons in the input sequence:
  # Draw a line at y=0 from 1 to the length of the sequence:
  x <- c(1, nchar(sequence))
  print(x)
  y <- c(0, 0)
  y
  plot(
    x,
    y,
    ylim = c(0, 3),
    type = "l",
    axes = FALSE,
    xlab = "Nucleotide",
    ylab = "Reading frame",
    main = "Predicted start (red) and stop (blue) codons"
  )
  segments(1, 1, nchar(sequence), 1)
  segments(1, 2, nchar(sequence), 2)
  # Add the x-axis at y=0:
  axis(1, pos = 0)
  # Add the y-axis labels:
  text(0.9, 0.5, "+1")
  text(0.9, 1.5, "+2")
  text(0.9, 2.5, "+3")
  
  # Draw in each predicted start/stop codon:
  mylist <- findPotentialStartsAndStops2(sequence)
  positions = mylist[["positions"]]
  types = mylist[["types"]]
  numcodons <- length(positions)
  for (i in 1:numcodons)
  {
    position <- positions[i]
    type <- types[i]
    remainder <- (position - 1) %% 3
    if (remainder == 0)
      # +1 reading frame
    {
      if (type == "atg") { 
        segments(position, 0, position, 1, lwd = 1,col = "red")}
      else {
        segments(position, 0, position, 1, lwd = 1,col = "blue")}
    }
    else if (remainder == 1){
      if (type == "atg") {
        segments(position, 1, position, 2, lwd = 1, col = "red")}
      else {
      segments(position, 1, position, 2, lwd = 1, col = "blue")}
    }
    else if (remainder == 2){
      if (type == "atg") {
      segments(position, 2, position, 3, lwd = 1, col = "red")}
    else {
      segments(position, 2, position, 3, lwd = 1, col = "blue")}
    }
  }
}