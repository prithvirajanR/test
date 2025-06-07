import pandas as pd
from lifelines import GradientBoostingSurvivalRegression


def fit_survival_model(features: pd.DataFrame, durations: pd.Series, events: pd.Series) -> GradientBoostingSurvivalRegression:
    """Fit a gradient boosting survival model."""
    model = GradientBoostingSurvivalRegression()
    model.fit(features, durations=durations, event_observed=events)
    return model
