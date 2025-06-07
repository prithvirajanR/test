# PanCancer Immune Age Pipeline

This repository contains a minimal Python implementation for exploring epigenetic age acceleration and immune landscape across TCGA pan-cancer cohorts.

The code is structured as a package named `pancancer_immune_age` and provides utilities for loading data, computing epigenetic ages (placeholder implementations of GrimAge and stemTOC), estimating immune cell fractions, performing clustering with PCA + UMAP, and fitting a gradient boosting survival model.

The `main.py` script demonstrates how these pieces can be combined on tab-delimited expression, methylation, and clinical datasets located under a `data/` directory.
