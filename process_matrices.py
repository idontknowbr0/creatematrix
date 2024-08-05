import os
import scipy.io
import pandas as pd
import numpy as np
#import subprocess
print("Creating matrix. This may take a while")
def process_matrix(dir_path, output_file):
    # Read the matrix
    dir_path = os.path.dirname(dir_path)

    mat = scipy.io.mmread(os.path.join(dir_path, "matrix.mtx")).tocsr()
    
    # Read features (genes) and barcodes
    features = pd.read_csv(os.path.join(dir_path, "features.tsv"), sep='\t', header=None)
    barcodes = pd.read_csv(os.path.join(dir_path, "barcodes.tsv"), sep='\t', header=None)
    
    # Check dimensions
    print(f"Dimensions for {dir_path}")
    print(f"Matrix: {mat.shape}")
    print(f"Features: {features.shape}")
    print(f"Barcodes: {barcodes.shape}")
    
    # Create a DataFrame
    df = pd.DataFrame.sparse.from_spmatrix(mat)
    df.index = features[1]  # Assuming gene names are in the second column
    df.columns = barcodes[0]
    
    # Add gene names as a column
    df.insert(0, "gene", df.index)
    
    # Write to CSV
    df.to_csv(output_file, index=False)
    
    # Confirm file creation and size
    print(f"File saved: {output_file}")
    print(f"File exists: {os.path.exists(output_file)}")
    print(f"File size: {os.path.getsize(output_file)} bytes")
    return df

base_path = os.environ['BASE_PATH']

gene_processed_path = base_path+"/gene_processed_feature_bc_matrix"
gene_raw_path = base_path+"/gene_raw_feature_bc_matrix"
transcript_processed_path = base_path+"/transcript_processed_feature_bc_matrix"
transcript_raw_path = base_path+"/transcript_raw_feature_bc_matrix"

#subprocess.call(['sh', '/Users/scheng/Documents/gzip_files.sh'])

# Process gene-level data (directory)
gene_processed = os.path.join(gene_processed_path, "gene_processed_feature_bc_matrix")
gene_processed_result = process_matrix(gene_processed, os.path.join(base_path, "gene_processed_count_matrix.csv"))

gene_raw = os.path.join(gene_raw_path, "gene_raw_feature_bc_matrix")
gene_raw_result = process_matrix(gene_raw, os.path.join(base_path, "gene_raw_count_matrix.csv"))

# Process transcript-level data (directory)
transcript_processed = os.path.join(transcript_processed_path, "transcript_processed_feature_bc_matrix")
transcript_processed_result = process_matrix(transcript_processed, os.path.join(base_path, "transcript_processed_count_matrix.csv"))

transcript_raw = os.path.join(transcript_raw_path, "transcript_raw_feature_bc_matrix")
transcript_raw_result = process_matrix(transcript_raw, os.path.join(base_path, "transcript_raw_count_matrix.csv"))

# View the first few rows of each result
#print("Gene Processed data:")
#print(gene_processed_result.head())

#print("Gene Raw data:")
#print(gene_raw_result.head())

#print("Transcript Processed data:")
#print(transcript_processed_result.head())

#print("Transcript Raw data:")
#print(transcript_raw_result.head())
