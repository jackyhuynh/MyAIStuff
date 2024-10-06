#Lec11_PhyTrees

library(seqinr)
library(ape)

#Ex1:
#-----

#read the alignement
virusaln <- read.alignment(file = "Phosphoprotein_Seqs.phy", format = "phylip")

#build the tree
unrootedNJtree(virusaln, "protein")

#rebuild the tree based on a cleaned  alignment
cleanedvirusaln <- cleanAlignment(virusaln, 30, 30)
unrootedNJtree(cleanedvirusaln, "protein")

#Ex2:
#-----

#read the alignement
Foxaln <- read.alignment(file = "FoxProtein_Seqs_2.phy", format = "phylip")
Foxaln$nam[6]

#print the distance matrix
Foxdist <- dist.alignment(Foxaln)
Foxdist
min(Foxdist)

#build the tree
FoxTree<-rootedNJtree(Foxaln, "tr|Q9VT99|", "protein")

#save the tree
write.tree(FoxTree, "FoxTree.tre")
