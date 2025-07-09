import pandas as pd
import numpy as np
from config import Config

def generate_data(n=365):
    dates = pd.date_range(start='2024-01-01', periods=n)
    data = pd.DataFrame({'date': dates})
    
    # Generate channel spends with seasonality
    for channel in Config.CHANNELS:
        base = np.random.uniform(5000, 20000)
        trend = np.linspace(1, 1.5, n)
        seasonality = np.sin(np.linspace(0, 10*np.pi, n)) * 0.3
        noise = np.random.normal(0, 0.1, n)
        data[channel] = base * trend * (1 + seasonality + noise)
    
    # Generate sales with adstock effects
    coefficients = {'TV': 0.35, 'Digital': 0.25, 'Radio': 0.15, 
                   'Print': 0.10, 'Outdoor': 0.05}
    adstock_params = {'TV': 0.75, 'Digital': 0.5, 'Radio': 0.4, 
                     'Print': 0.3, 'Outdoor': 0.2}
    
    sales = 0
    for channel in Config.CHANNELS:
        channel_effect = apply_adstock(data[channel], adstock_params[channel])
        sales += coefficients[channel] * channel_effect
    
    # Add baseline sales and noise
    baseline = 50000 + 200 * np.arange(n) 
    data[Config.TARGET] = baseline + sales * 1000 + np.random.normal(0, 5000, n)
    
    return data

def apply_adstock(x, alpha):
    x = np.array(x)
    x_adstock = np.zeros_like(x)
    x_adstock[0] = x[0]
    for t in range(1, len(x)):
        x_adstock[t] = x[t] + alpha * x_adstock[t-1]
    return x_adstock