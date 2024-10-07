

# Bioinformatics Genes, ORFs, and Sequences

### Major Topics

#### 1. Finding Genes

**What is a gene?**  
A gene is the basic physical and functional unit of heredity, made up of DNA. Some genes act as instructions to create molecules (proteins), while others do not code for proteins. In humans, genes can vary in size from a few hundred DNA bases to over 2 million bases.

**The Genetic Code:**  
Each group of three nucleotides in a DNA sequence codes for a specific amino acid in a protein sequence. For example, the first three nucleotides, ATG, code for methionine (M).

- **Finding the frequency of DNA “words”** using the `count(seq, wordsize)` function:  
  - `wordsize=1`: Bases  
  - `wordsize=2`: bp words  
  - `wordsize=3`: Codons (a sequence of three nucleotides forming a unit of genetic code in a DNA or RNA molecule). Each codon specifies an amino acid.

**Start and Stop Codons:**  
Special codons that signal the start and end of a protein-coding gene:
- **Start codon:** ATG
- **Stop codons:** TGA, TAA, TAG  

Use the `tablecode()` function in the SeqinR package to identify codons.

**How to find a gene:**  
A protein-coding gene starts with ATG (start codon), followed by an integer number of codons, and ends with a stop codon (TGA, TAA, or TAG).

---

#### 2. Open Reading Frames (ORFs)

**What is an mRNA?**  
mRNA is the messenger RNA that carries genetic information from DNA to the ribosome, where proteins are synthesized.

**What is an ORF?**  
An ORF is a portion of a DNA molecule that, when translated into amino acids, contains no stop codons. The genetic code reads DNA sequences in groups of three base pairs, which can result in six possible reading frames for a double-stranded DNA molecule.

Genes in a genome can occur on either the forward (plus) strand or the reverse (minus) strand. Use the `comp()` and `rev()` functions in the SeqinR package to analyze sequences.

**True vs. False Positive Gene Predictions:**  
Many ORFs in a DNA sequence may not correspond to real genes and might occur by chance. Gene prediction can result in true or false positives.

**Significant ORFs:**  
- Locate an ORF using `plotPotentialStartsAndStop2()`.  
- Use `findORFsinSeq()` to return a list of ORFs' start and end positions and lengths.  
- A real gene is typically the longest ORF found in random sequences of the same length and nucleotide composition as the original sequence.

**Methods:**  
- Generate random sequences using a multinomial model with `generateSeqsWithMultinomialModel()`.  
- Use `findORFsinSeq()` to define a threshold for filtering out shorter ORFs.
- Compare the longest ORF in random sequences using `max()` and `quantile()` functions.

**R Examples:**  
- Use `matchPatterns()` from the BioString package to find occurrences of a specific pattern in a reference sequence.
- Use `sample()` to randomly select bases for a sequence of a specific length.

---

#### 3. Pairwise Sequence Alignment

**Introduction:**  
Homologous organs in living organisms derive from a recent common ancestor, whereas analogous organs have similar functions but different structures.

**What is alignment?**  
Pairwise sequence alignment identifies regions of similarity between two biological sequences (DNA, RNA, or protein), which may indicate functional, structural, or evolutionary relationships.

**Applications of Sequence Data:**  
- Inferring the function of a newly sequenced gene by finding similarities with known genes.
- Estimating protein structure from a related protein with known structure and sequence.

**Scoring an Alignment:**  
- **Mutations:** Changes in DNA and protein sequences over evolutionary time. Point mutations and insertions/deletions (indels) are common mutations.
- **Scoring schema:**
  - `+1`: Match premium
  - `-u`: Mismatch penalty
  - `-o`: Indel penalty
  - **Score Formula:** `Score = #matches - u(#mismatches) - o(#indels)`

---

#### 4. Dot Plot Method

**Overview:**  
A dot plot is a graphical method for comparing two protein, RNA, or DNA sequences. It involves a two-dimensional matrix where matching residues are marked, forming diagonal lines that indicate regions of similarity.

---

#### 5. Dynamic Programming Method for Alignment

**Algorithms:**
- **Needleman and Wunsch Algorithm (1970):** Global alignment for homologous sequences across their entire length.
- **Smith and Waterman Algorithm:** Local alignment for homologous regions within otherwise unrelated sequences.

**Computational Complexity:**  
- Running time for sequence alignment is `O(m*n)`, where `m` and `n` are the lengths of the two sequences.

**Statistical Significance:**  
- Create random sequences with the same amino acid composition and length as one of the two sequences.
- Align the sequences using the Needleman-Wunsch Algorithm.
- Repeat with random sequences and compare alignment scores. If `P_value > 0.05`, the alignment score is not statistically significant, indicating the sequences are unrelated.

---

#### 6. Pairwise Protein Sequence Alignment

**Protein Sequence Data:**  
Proteins consist of hundreds or thousands of amino acids. Each group of three bases in mRNA (codon) specifies a particular amino acid, and there are 20 amino acids that can be combined to form a protein.

**Databases:**  
- **NCBI:** Database for DNA sequences.
- **RefSeq and Uniprot:** Manually curated databases, with Uniprot having higher quality entries. Additional information includes scientific papers, biological functions, and protein-protein interactions.

---

#### 7. Sequence Alignment Metrics

- **PAM vs. BLOSUM:**  
  Matrices used for scoring alignments based on evolutionary distances between sequences.

**Statistical Significance in Alignment:**  
The importance of statistical significance in determining whether sequence alignments are meaningful, or merely coincidental.

---

This refined version organizes the topics more clearly and eliminates redundant wording, making the guide easier to follow.