import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Data parameters
    CHANNELS = ['TV', 'Digital', 'Radio', 'Print', 'Outdoor']
    TARGET = 'Sales'
    DATE_COL = 'date'
    
    # Model parameters
    ADSTOCK_MAX = 8
    N_SAMPLES = 2000
    TUNE = 1000
    
    # API keys (if using real data)
    GOOGLE_ANALYTICS_KEY = os.getenv("GOOGLE_ANALYTICS_KEY")
    FACEBOOK_ADS_KEY = os.getenv("FACEBOOK_ADS_KEY")