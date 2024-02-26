import plotly.graph_objects as go
from scipy.stats import binom
import numpy as np
import streamlit as st

# Calculate prob of a CDO^2 default
def cdo2_default_probability(ind_default_prob, tranche):
    prob_cdo_default = 1 - binom.cdf(tranche - 1, 100, ind_default_prob)
    prob_cdo2_default = 1 - binom.cdf(tranche - 1, 100, prob_cdo_default)
    return prob_cdo2_default

fig = go.Figure()

default_tranche = 10

# Generate data for graph
ind_default_probs = np.linspace(0, 0.5, 500)  # Range of individual default probabilities
probs = [cdo2_default_probability(ind_default_prob, default_tranche) for ind_default_prob in ind_default_probs]

# Add the initial trace
fig.add_trace(go.Scatter(x=ind_default_probs, y=probs, mode='lines'))

# Update layout with the slider for tranche adjustments
fig.update_layout(
    title="Probability of CDO^2 Default based on Individual Default Probability",
    xaxis_title="Individual Default Probability",
    yaxis_title="Probability of CDO^2 Default",
    sliders=[{
        'pad': {'t': 50},
        'len': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'y': 0,
        'currentvalue': {
            'prefix': 'Tranche: ',
            'visible': True,
            'xanchor': 'center'
        },
        'steps': [{
            'label': f'{i}',
            'method': 'restyle',
            'args': [{'y': [[cdo2_default_probability(x, i) for x in ind_default_probs]]}]
        } for i in range(101)]
    }]
)

# Set the default slider value to 10
fig['layout']['sliders'][0]['active'] = default_tranche

st.plotly_chart(fig)