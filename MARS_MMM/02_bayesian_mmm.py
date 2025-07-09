import pymc as pm
import numpy as np
import pandas as pd
from config import Config
from .adstock import apply_adstock_vectorized

def build_model(data):
    channels = Config.CHANNELS
    n_channels = len(channels)
    n_obs = len(data)
    
    coords = {
        "channel": channels,
        "obs": np.arange(n_obs),
        "adstock_max": np.arange(Config.ADSTOCK_MAX)
    }
    
    with pm.Model(coords=coords) as model:
        # Data containers
        channel_spend = pm.MutableData(
            "channel_spend", 
            data[channels].values.T, 
            dims=("channel", "obs")
        )
        
        # Priors
        intercept = pm.Normal("intercept", mu=0, sigma=10)
        sigma = pm.HalfNormal("sigma", sigma=10)
        
        # Channel coefficients (non-negative)
        coefficients = pm.HalfNormal("coefficients", sigma=1, dims="channel")
        
        # Adstock parameters
        alpha = pm.Beta("alpha", alpha=1, beta=3, dims="channel")
        lag_weight = pm.Dirichlet("lag_weight", a=np.ones(Config.ADSTOCK_MAX), dims="channel")
        
        # Adstock transformation
        adstocked = apply_adstock_vectorized(channel_spend, alpha, lag_weight)
        
        # Media contribution
        media_effect = pm.math.sum(adstocked * coefficients[:, None], axis=0)
        
        # Seasonality component
        time = np.arange(n_obs)
        seasonality = pm.Fourier("seasonality", n=2, period=365, dims="obs")
        
        # Sales prediction
        mu = intercept + media_effect + seasonality
        sales = pm.Normal("sales", mu=mu, sigma=sigma, 
                          observed=data[Config.TARGET].values, dims="obs")
        
    return model