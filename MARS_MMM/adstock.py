import pytensor.tensor as pt

def apply_adstock_vectorized(x, alpha, weights):
    """
    Vectorized adstock transformation with carryover
    x: (channels, time)
    alpha: (channels,) retention rate
    weights: (channels, max_lag) lag weights
    """
    max_lag = weights.shape[1]
    x = pt.as_tensor_variable(x)
    
    # Create lagged matrix
    lagged = pt.zeros((x.shape[0], x.shape[1], max_lag))
    for lag in range(max_lag):
        lagged = pt.set_subtensor(
            lagged[:, max_lag-lag-1:, lag],
            x[:, :x.shape[1]-(max_lag-1)+lag]
        )
    
    # Apply weights and sum
    weighted = pt.sum(lagged * weights[:, None, :], axis=2)
    
    # Apply retention
    adstocked = pt.zeros_like(x)
    adstocked = pt.set_subtensor(adstocked[:, :max_lag], weighted[:, :max_lag])
    for t in range(max_lag, x.shape[1]):
        adstocked = pt.set_subtensor(
            adstocked[:, t],
            weighted[:, t] + alpha * adstocked[:, t-1]
        )
    
    return adstocked