"""Entry point for running a simplified pan-cancer immune-age analysis."""

from pathlib import Path
import pandas as pd

from .data_loading import load_expression_data, load_methylation_data, load_clinical_data
from .age_calculation import compute_grim_age, compute_stemtoc_age, delta_age
from .immune_deconvolution import deconvolute
from .clustering import cluster_features
from .survival_model import fit_survival_model


DATA_DIR = Path('data')


def main():
    # Load data (placeholder paths)
    expression = load_expression_data(DATA_DIR / 'expression.tsv')
    methylation = load_methylation_data(DATA_DIR / 'methylation.tsv')
    clinical = load_clinical_data(DATA_DIR / 'clinical.tsv')

    # Epigenetic age calculations
    grim_age = compute_grim_age(methylation)
    stem_age = compute_stemtoc_age(methylation)

    ages = pd.DataFrame({'GrimAge': grim_age, 'stemTOC': stem_age}, index=methylation.index)
    ages['Delta_GrimAge'] = delta_age(clinical['age'], ages['GrimAge'])
    ages['Delta_stemTOC'] = delta_age(clinical['age'], ages['stemTOC'])

    # Immune deconvolution
    immune = deconvolute(expression)

    # Integrate features
    features = pd.concat([ages[['Delta_GrimAge', 'Delta_stemTOC']], immune], axis=1)

    # Dimensionality reduction
    embedding = cluster_features(features)

    # Survival model
    model = fit_survival_model(features, clinical['survival_time'], clinical['event'])

    print('UMAP embedding head:')
    print(embedding.head())
    print('Survival model fitted with', model.n_estimators_, 'estimators')


if __name__ == '__main__':
    main()
