import numpy as np
import pandas as pd
from scipy.stats import binom

# Function to calculate the probability of a CDO^2 default
def cdo2_default_probability(ind_default_prob, tranche):
    prob_cdo_default = 1 - binom.cdf(tranche - 1, 100, ind_default_prob)
    prob_cdo2_default = 1 - binom.cdf(tranche - 1, 100, prob_cdo_default)
    return prob_cdo2_default

# Generate data
ind_default_probs = np.linspace(0, 1, 500)  # Adjusted range of individual default probabilities to 0 to 1
tranches = range(101)  # Range of tranches

# Prepare a DataFrame to hold the data
data = {'ind_default_prob': ind_default_probs}
for tranche in tranches:
    data[f'tranche_{tranche}'] = [cdo2_default_probability(ind_default_prob, tranche) for ind_default_prob in ind_default_probs]

df = pd.DataFrame(data)

# Save the DataFrame to a file
df.to_csv('cdo2_default_probabilities_updated.csv', index=False)
