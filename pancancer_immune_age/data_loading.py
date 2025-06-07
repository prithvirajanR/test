import pandas as pd
from pathlib import Path


def load_expression_data(path: Path) -> pd.DataFrame:
    """Load RNA-seq expression data from a TSV/CSV file."""
    return pd.read_csv(path, sep='\t', index_col=0)


def load_methylation_data(path: Path) -> pd.DataFrame:
    """Load 450k methylation data from a TSV/CSV file."""
    return pd.read_csv(path, sep='\t', index_col=0)


def load_clinical_data(path: Path) -> pd.DataFrame:
    """Load clinical metadata for samples."""
    return pd.read_csv(path, sep='\t', index_col=0)
