# subtype_variability
This repository contains code and data for the paper: Neuroimaging-based variability in subtyping biomarkers for psychiatric heterogeneity.

The main folder contains all the notebooks for the main analysis. The order to run the codes:
1. step01_cluster_identification_kmeans.ipynb: conduct subtyping analysis using K-means;
2. step02_cluster_identification_HYDRA.ipynb: conduct subtyping analysis using K-means;
3. step03_prepare_data4R.ipynb: prepare data for internal validation of the identified subtypes;
The following files use R-based codes for the test: R_cluster_compare_centroid.ipynb; R_cluster_compare_feature.ipynb; R_cluster_sigclust_test.ipynb
4. step04_subtype_consistency_kmeans.ipynb: calculate the consistency of subtypes estimated using different data madality;
5. step05_subtype_clinic_measure.ipynb: compare clinic and cognitive measures between identified subtypes.

In case of any questions, please contact Zhenfu Wen (zhenfu.wen@uth.tmc.edu).
