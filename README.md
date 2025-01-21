# Ventral Nerve Cord Matching of Drosophila by Sex

<img src="https://github.com/user-attachments/assets/dfe4bb8e-b1cd-40c5-8a35-56161c893f3b" alt="brain" width="120" />

## File Structure 
`paper` - Paper summarizing the results of this project.

`model` - Contains the construction for the final model.

`align` - Contains algorithms for different model components. 
  - `decompositon`
  - `reconstuction`
  - `split`
  - `similarity`
    
`preprocess` - Contains all code used for preprocessing. 

`literature` - Literature used for this project. 

## Reproducibility
For reproducibility purposes the Anaconda package manager is reccomended. 
Paste the following in your terminal to install dependencies. 
```
conda env create -f environment.yml
conda activate iso
```
