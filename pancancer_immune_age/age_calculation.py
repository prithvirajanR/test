import pandas as pd


def compute_grim_age(methylation_df: pd.DataFrame) -> pd.Series:
    """Dummy GrimAge implementation.

    In reality, this should implement the full GrimAge clock or use an
    external package. Here we implement a placeholder that returns the mean
    methylation value per sample as a stand-in for illustration.
    """
    return methylation_df.mean(axis=1)


def compute_stemtoc_age(methylation_df: pd.DataFrame) -> pd.Series:
    """Dummy stemTOC implementation (placeholder)."""
    return methylation_df.median(axis=1)


def delta_age(chronological_age: pd.Series, predicted_age: pd.Series) -> pd.Series:
    """Calculate delta age as predicted minus chronological age."""
    return predicted_age - chronological_age
