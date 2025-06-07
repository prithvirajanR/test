import pandas as pd
from typing import Literal


# This is a placeholder; real implementation would wrap tools like CIBERSORTx
# or quanTIseq. Here we approximate with a simple transformation.

def deconvolute(expression_df: pd.DataFrame, method: Literal['cibersortx', 'quantiseq'] = 'cibersortx') -> pd.DataFrame:
    """Return dummy immune-cell fractions based on expression data."""
    if method not in {'cibersortx', 'quantiseq'}:
        raise ValueError('Unsupported method: ' + method)

    # For demonstration, compute relative expression of some marker genes.
    markers = ['CD3D', 'CD8A', 'MS4A1', 'NKG7']
    fractions = expression_df[markers].div(expression_df[markers].sum(axis=1), axis=0)
    fractions.columns = [f'{col}_frac' for col in fractions.columns]
    return fractions.fillna(0)
