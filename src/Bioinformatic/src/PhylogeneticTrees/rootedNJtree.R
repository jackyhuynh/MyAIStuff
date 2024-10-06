rootedNJtree <- function(alignment, theoutgroup, type)
{
  # load the ape and seqinR packages:
  require("ape")
  require("seqinr")
  # define a function for making a tree:
  makemytree <- function(alignmentmat, outgroup=`theoutgroup`)
  {
    alignment <- ape::as.alignment(alignmentmat)
    if (type == "protein")
    {
      mydist <- dist.alignment(alignment)
    }
    else if (type == "DNA")
    {
      alignmentbin <- as.DNAbin(alignment)
      mydist <- dist.dna(alignmentbin)
    }
    mytree <- nj(mydist)
    mytree <- makeLabel(mytree, space="") # get rid of spaces in tip names.
    myrootedtree <- root(mytree, outgroup, r=TRUE)
    return(myrootedtree)
  }
  # infer a tree
  mymat <- as.matrix.alignment(alignment)
  myrootedtree <- makemytree(mymat, outgroup=theoutgroup)
  # bootstrap the tree
  myboot <- boot.phylo(myrootedtree, mymat, makemytree)
  # plot the tree:
  plot.phylo(myrootedtree, type="p") # plot the rooted phylogenetic tree
  nodelabels(myboot,cex=0.7) # plot the bootstrap values
  myrootedtree$node.label <- myboot # make the bootstrap values be the node labels
  return(myrootedtree)
}