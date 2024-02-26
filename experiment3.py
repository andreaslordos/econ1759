import plotly.graph_objects as go
import pandas as pd
import streamlit as st

# Load the updated data from the CSV file
df = pd.read_csv('cdo2_default_probabilities_updated.csv')

# Initialize the figure
fig = go.Figure()

default_tranche = 10

# Add the initial trace using the default tranche data
fig.add_trace(go.Scatter(x=df['ind_default_prob'], y=df[f'tranche_{default_tranche}'], mode='lines'))

# Update layout with the slider for tranche adjustments
fig.update_layout(
    title="Probability of CDO^2 Default based on Individual Default Probability",
    xaxis_title="Individual Default Probability",
    xaxis_range=[0, 1],  # Set the x-axis range to 0 to 1
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
            'args': [{'y': [df[f'tranche_{i}']]}]
        } for i in range(101)]
    }]
)

# Set the default slider value to 10
fig['layout']['sliders'][0]['active'] = default_tranche

# Display the figure in Streamlit
st.plotly_chart(fig)
