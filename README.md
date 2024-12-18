# Isomorphix

<img src="https://github.com/user-attachments/assets/dfe4bb8e-b1cd-40c5-8a35-56161c893f3b" alt="brain" width="120" />


Isomorphix is a project created for the Princeton University VNC Matching Challenge which aims to create an optimal mapping alignment score between the connectomes of male and female drosophila. 
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

`data` - Contains all data used for the project as well as the code used to download it.
## Reproducibility
For reproducibility purposes the Anaconda package manager is reccomended. 
Paste the following in your terminal to install dependencies. 
```
conda env create -f environment.yml
conda activate myenv
```

## Disclaimer 
No large language models were used for this project. 
