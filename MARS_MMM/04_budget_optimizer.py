import numpy as np
import pymc as pm
from scipy.optimize import minimize

def calculate_roi(trace, data):
    """Calculate ROI for each channel"""
    channels = Config.CHANNELS
    roi = {}
    
    for i, channel in enumerate(channels):
        # Posterior mean of coefficients
        coef = trace.posterior['coefficients'].sel(channel=channel).mean().item()
        
        # Calculate incremental sales per dollar
        roi[channel] = coef * 1000  # Assuming spend in thousands
        
    return roi

def optimize_budget(total_budget, roi, min_spend=None, max_spend=None):
    """Optimize budget allocation using ROI"""
    channels = list(roi.keys())
    n = len(channels)
    
    # Objective function: maximize total revenue
    def objective(x):
        return -sum(roi[ch] * x[i] for i, ch in enumerate(channels))
    
    # Constraints
    constraints = (
        {'type': 'eq', 'fun': lambda x: total_budget - sum(x)},  # Total budget
    )
    
    # Bounds
    bounds = [(0, total_budget) for _ in range(n)]
    
    if min_spend:
        for i, ch in enumerate(channels):
            if ch in min_spend:
                bounds[i] = (min_spend[ch], bounds[i][1])
    
    if max_spend:
        for i, ch in enumerate(channels):
            if ch in max_spend:
                bounds[i] = (bounds[i][0], max_spend[ch])
    
    # Initial guess (equal allocation)
    x0 = [total_budget / n] * n
    
    # Solve
    res = minimize(objective, x0, method='SLSQP', 
                   bounds=bounds, constraints=constraints)
    
    return {ch: res.x[i] for i, ch in enumerate(channels)}