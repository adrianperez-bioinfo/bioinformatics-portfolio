# Applied Bioinformatics & Computational Biology Projects

Welcome to my repository. I am an undergraduate student in my third year of a Double Degree in **Biochemistry and Biotechnology**, actively expanding my skills into computational biology, biocomputing, and genomic data processing.

This repository collects applied bioinformatics projects developed to bridge molecular biology concepts with algorithmic problem-solving using Python and standard biocomputing libraries.

---

## Featured Projects

### 1. [mRNA FIV Vaccine Design Pipeline](vacunas_mRNA_VIF/)
An exploratory biocomputational workflow developed to model the design of a modular mRNA vaccine targeting the Envelope (Env) glycoprotein of the Feline Immunodeficiency Virus (FIV).
* **Biological Framework:** Implements *Felis catus* codon optimization considering co-translational folding constraints, endogenous Caveolin-1 UTR selection (5'-UTR and 3'-UTR), 5' capping, poly-A tailing, and **pseudouridination ($\psi$)** to simulate immune evasion strategies.
* **Validation Steps:** Incorporates thermodynamic stability verification via GC content calculation (>40%) and an *in silico* translation check to ensure the Open Reading Frame (ORF) integrity is preserved after modification.
* **Libraries Used:** `Biopython` (`SeqIO`, `Seq`, `SeqUtils`), Pandas, NumPy.

### 2. [Pairwise Mutation Finder & Variant Classifier](mutation_finder/)
A Python tool designed to perform pairwise sequence alignments between reference and mutated protein sequences, identifying and annotating amino acid modifications.
* **Methodology:** Implements Needleman-Wunsch/Smith-Waterman optimal alignments via Biopython's `PairwiseAligner` to accurately map variants even in the presence of sequence length discrepancies.
* **Variant Annotation:** Maps modified positions using standard 1-based clinical numbering and automatically categorizes evolutionary events into **Insertions (INS)**, **Deletions (DEL)**, and **Substitutions (SUS)**.
* **Libraries Used:** `Biopython` (`Bio.Align`), `pandas`.

---

## Technical Skills

* **Programming & Scripting:** Python (Intermediate level), Bash/Linux terminal (in progress), R (in progress).
* **Bioinformatics Ecosystem:** Biopython, Pandas, NumPy.
* **Core Competencies:** Sequence Alignment, Variant Classification, mRNA Therapeutics Modeling, Codon Optimization, FASTA Parsing.
* **Version Control:** Git & GitHub.

---

## Usage and Setup

To run these scripts or notebooks locally, clone the repository and install the required Python dependencies:

```bash
git clone [https://github.com/adrianperez-bioinfo/bioinformatics-portfolio.git](https://github.com/adrianperez-bioinfo/bioinformatics-portfolio.git)
cd bioinformatics-portfolio
pip install biopython pandas numpy