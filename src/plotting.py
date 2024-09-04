import plotly.graph_objects as go


def plot_financial_ratio(df, column_name, threshold=0, better_is_higher=True):
    colors = ['green' if (value >= threshold) == better_is_higher else 'red' for value in df[column_name].values]
    line_values = [threshold] * len(df)

    fig = go.Figure(data=[go.Bar(
        x=df.index.to_series().apply(lambda x: str(x.year)),
        y=df[column_name],
        marker_color=colors,
        text=df[column_name],
        textposition='auto',
        showlegend=False
    )])

    fig.update_layout(
        title=column_name,
        xaxis_title='Year',
        yaxis_title=column_name,
        font=dict(family="Arial, sans-serif", size=12, color="RebeccaPurple"),
        autosize=True
    )

    fig.add_trace(go.Scatter(
        x=df.index.to_series().apply(lambda x: str(x.year)),
        y=line_values,
        opacity=0.7,
        line=dict(color=('blue' if better_is_higher else 'orange'), width=2),
        name='Guidance Line'
    ))

    return fig
