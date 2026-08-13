# 1011_multicellularity
Python and R scripts were used to analyze multicellular phenotypes and genotypes in the 1011 *S. cerevisiae* genome panel.

## Phenotyping

Contains scripts used to analyze multicellular phenotypes:

1. `Preprocessing/split image.ipynb`: Splits a full 96-well plate image into an 8 × 12 grid of individual well images; it can process either one image or every TIFF image in a folder.
2. `CCM_Model_Train.ipynb`: Trains and evaluates a seven-class convolutional neural network (CNN) image classifier for complex colony morphology (CCM) phenotypes, generates a confusion matrix, and exports the trained model.
3. `CCM_Model_Predict.ipynb`: Uses the trained seven-class CCM model to classify well images, sorts copies into predicted-class folders, and saves class and confidence results to Excel.
4. `PSH_Categorization_Model_Train.ipynb`: Trains and evaluates a four-class convolutional neural network (CNN) model that categorizes well images as: no growth, no PSH (pseudohyphal growth), PSH, or contamination, then exports the model.
5. `PSH_Categorization_Model_Predict.ipynb`: Uses the trained four-class CNN model to classify well images, sorts copies into predicted-class folders, and saves class and confidence results to Excel.
6. `PSH_quantification.ipynb`: Segments the colony center and surrounding pseudohyphal growth in each well image, calculates social growth as the outer-growth area relative to the center, and saves masks and an Excel summary.
7. `Phylogenetically Corrected Correlation Analysis/PhylogeneticComparisons.R`: Tests phylogenetic signal with Pagel's lambda and evaluates relationships among multicellular traits using phylogenetically independent contrasts and phylogenetic generalized least-squares models.
8. `Phylogenetically Corrected Correlation Analysis/phyloCorrelationMatrixPCA.R`: Calculates a phylogenetically corrected trait-correlation matrix from independent contrasts, visualizes the correlations, and performs PCA on the corrected traits.

## Genotyping

Contains scripts used to analyze genotypes associated with multicellularity:

1. `Preprocessing/Pheno_normalization_GWAS.ipynb`: Reorders phenotype values to match strain IDs, applies Yeo–Johnson or quantile normalization while preserving missing-value codes, plots normalization diagnostics, and exports GWAS-ready phenotype files.
2. `GWAS_FastLMM.ipynb`: Runs a single-SNP FastLMM GWAS while excluding chromosome 17 from association testing and kinship estimation, then saves complete and thresholded results plus Manhattan and Q–Q plots.
3. `permutation test for GWAS.ipynb`: Generates 100 reproducible phenotype permutations, runs FastLMM on the shuffled phenotypes, and saves the permutation GWAS p-values. The final empirical threshold is selected manually in Excel by retaining the lowest 5% of permutation p-values and choosing the highest p-value in that subset.
