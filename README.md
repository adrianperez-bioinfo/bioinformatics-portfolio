# Applied Bioinformatics & Computational Biology Projects

Welcome to my repository. I am an undergraduate student in my third year of a Double Degree in **Double Degree in Biochemistry and Molecular Biology, and Biotechnology**, actively expanding my skills into computational biology, biocomputing, and genomic data processing.

This repository collects applied bioinformatics projects developed to bridge molecular biology concepts with algorithmic problem-solving using Python and standard biocomputing libraries.

---

## Featured Projects

### 1. [mRNA FIV Vaccine Design Pipeline](vacunas_mRNA_VIF/)
An exploratory biocomputational workflow developed to model the design of a modular mRNA vaccine targeting the Envelope (Env) glycoprotein of the Feline Immunodeficiency Virus (FIV).
* **Biological Framework:** Implements *Felis catus* codon optimization considering co-translational folding constraints, endogenous Caveolin-1 UTR selection (5'-UTR and 3'-UTR), 5' capping, poly-A tailing, and **pseudouridination ($\psi$)** to simulate immune evasion strategies.
* **Validation Steps:** Incorporates thermodynamic stability verification via GC content calculation (>40%) and an *in silico* translation check to ensure the Open Reading Frame (ORF) integrity is preserved after modification.
* **Libraries Used:** `Biopython` (`SeqIO`, `Seq`, `SeqUtils`), Pandas, NumPy.

### 2. [Pairwise Mutation Finder & Variant Classifier](mutation_finder/)
A modular command-line (CLI) Python tool designed to perform pairwise sequence alignments between reference and mutated protein sequences, identifying and annotating amino acid modifications.
* **Methodology:** Implements Needleman-Wunsch/Smith-Waterman optimal alignments via Biopython's `PairwiseAligner` to accurately map variants even in the presence of sequence length discrepancies.
* **Variant Annotation:** Maps modified positions using standard 1-based clinical numbering and automatically categorizes evolutionary events into Insertions (INS), Deletions (DEL), and Substitutions (SUS).
* **CLI Architecture & Reliability:** Engineered as a dynamic command-line tool utilizing `sys.argv` for seamless integration into high-throughput Bash pipelines, featuring robust exception handling and automated usage validation.
* **Libraries Used:** `Biopython` (`Bio.Align`), Pandas.

## Technical Skills

* **Programming & Scripting:** Python (Intermediate level), Bash / Linux Shell Scripting, R (in progress).
* **Systems & Environment Management:** Native Linux workflows (Ubuntu/WSL), virtual environment isolation (`venv` / Conda) for scientific reproducibility, and data hygiene (`.gitignore`).
* **Bioinformatics Ecosystem:** Biopython, Pandas, NumPy.
* **Core Competencies:** Command-Line Tool Development (CLI), Sequence Alignment, Variant Classification, Codon Optimization, FASTA Parsing.
* **Version Control:** Git & GitHub.

## Usage and Setup

To run these tools locally in a clean, reproducible environment, clone the repository and set up a Python virtual environment:

```bash
# 1. Clone the repository and navigate into it
git clone [https://github.com/adrianperez-bioinfo/bioinformatics-portfolio.git](https://github.com/adrianperez-bioinfo/bioinformatics-portfolio.git)
cd bioinformatics-portfolio

# 2. Create and activate an isolated virtual environment
python3 -m venv bio_env
source bio_env/bin/activate

# 3. Install the required biocomputing dependencies
pip install biopython pandas numpy

# 4. Run the Mutation Finder CLI tool with a sample FASTA file
python3 mutation_finder/mutation_finder.py prot_seq.fasta
