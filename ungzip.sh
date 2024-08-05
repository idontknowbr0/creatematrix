#!/bin/bash
#command run: source gzip_files.sh
# Loop through all .gz files in the current directory

#change this path to single-cell donor/cell directory.
export BASE_PATH="/Volumes/Lab_Group/BoltonFCS/Sophia/epi2me_output/single-cell/NP1695_don3"



dir=${BASE_PATH}/gene_processed_feature_bc_matrix
dir2=${BASE_PATH}/gene_raw_feature_bc_matrix
dir3=${BASE_PATH}/transcript_processed_feature_bc_matrix
dir4=${BASE_PATH}/transcript_raw_feature_bc_matrix
for file in "$dir"/*.gz; do
    # Check if the file exists (this is necessary to avoid errors if no .gz files are found)
    if [ -f "$file" ]; then
        echo "Unzipping $file..."
        # Unzip the file
        gunzip "$file"
        fi
        done
for file in "$dir2"/*.gz; do
    # Check if the file exists (this is necessary to avoid errors if no .gz files are found)
    if [ -f "$file" ]; then
        echo "Unzipping $file..."
        # Unzip the file
        gunzip "$file"
    fi  
    done
for file in "$dir3"/*.gz; do
    # Check if the file exists (this is necessary to avoid errors if no .gz files are found)
    if [ -f "$file" ]; then
        echo "Unzipping $file..."
        # Unzip the file
        gunzip "$file"
    fi  
    done
for file in "$dir4"/*.gz; do
    # Check if the file exists (this is necessary to avoid errors if no .gz files are found)
    if [ -f "$file" ]; then
        echo "Unzipping $file..."
        # Unzip the file
        gunzip "$file"
    fi  
done
echo "All .gz files have been unzipped."
python process_matrices.py