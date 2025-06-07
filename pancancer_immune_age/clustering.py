import pandas as pd
from sklearn.decomposition import PCA
import umap
from sklearn.preprocessing import StandardScaler


def cluster_features(df: pd.DataFrame, n_components: int = 30, n_neighbors: int = 15, min_dist: float = 0.1) -> pd.DataFrame:
    """Perform PCA followed by UMAP on the input features."""
    scaler = StandardScaler()
    scaled = scaler.fit_transform(df)

    pca = PCA(n_components=n_components)
    pca_result = pca.fit_transform(scaled)

    reducer = umap.UMAP(n_neighbors=n_neighbors, min_dist=min_dist)
    embedding = reducer.fit_transform(pca_result)

    return pd.DataFrame(embedding, index=df.index, columns=['UMAP1', 'UMAP2'])
