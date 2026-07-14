# Importamos las librerías
import pandas as pd

# Importamos funciones
from Bio import SeqIO
from Bio import Align

# Creamos una función que nos devuelva un DF con las posiciones de las mutaciones
def mutation_finder(archivo_fasta):
    
    aligner = Align.PairwiseAligner()
    
    # Hacemos una comprobación por si no encuentra el archivo o no hay suficientes secuencias.
    try:
        prot_seqs = list(SeqIO.parse(archivo_fasta,"fasta"))
    except FileNotFoundError:
        return "Error. No se ha encontrado el archivo."
    if len((prot_seqs)) < 2:
        return "Error. El archivo debe contener al menos 2 secuencias."
    
    # Definimos la secuencia de referencia y la secuencia a comparar
    seq_ref = str(prot_seqs[0].seq)
    seq_mut = str(prot_seqs[1].seq)
    
    aligned_seqs = aligner.align(seq_ref,seq_mut)
    best_alignement = aligned_seqs[0]
    
    seq_ref_aligned = best_alignement[0]
    seq_mut_aligned = best_alignement[1]
    
    list_mut_positions = []
    lista_tipos_mut = []
    
    # Hacemos que nos guarde la posición de la mutación y el tipo
    if seq_ref_aligned != seq_mut_aligned:
        for x,(a,b) in enumerate(zip(seq_ref_aligned,seq_mut_aligned), start = 1):
            if a != b:
                list_mut_positions.append(f"{a}{x}{b}")
                if a == "-":
                    lista_tipos_mut.append("INS")
                elif b == "-":
                    lista_tipos_mut.append("DEL")
                else:
                    lista_tipos_mut.append("SUS")
           
    
    df = pd.DataFrame({"POSICIÓN MUTACIONES" : list_mut_positions,"TIPO DE MUTACIÓN" : lista_tipos_mut})
    return df

print(mutation_finder("prot_seq.fasta"))