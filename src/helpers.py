def get_threshold(column_name):
    thresholds = {
        "Gross Margin %": (40, True),
        "Net Margin %": (20, True),
        "Long Term Debt over Earnings": (4, False),
        "Expenditure over Income %": (25, False)
    }
    return thresholds.get(column_name, (0, True))

def display_pe_ratio(df_info):
    pe_text = '<p style="margin: 0; font-size: 16px;"><b>Price Earnings Ratio</b></p><p style="margin-top: 0; font-size:14px">'
    try:
        trailing_pe = df_info['trailingPE'][0]
        forward_pe = df_info['forwardPE'][0]

        trailing_pe_color = "green" if trailing_pe < 40 else "red"
        forward_pe_color = "green" if forward_pe < 40 else "red"

        trailing_text = f'<br/><b>Trailing P/E:</b><span style="color:{trailing_pe_color}"> {trailing_pe}</span>'
        forward_text = f'<br/><b>Forward P/E:</b><span style="color:{forward_pe_color}"> {forward_pe}</span></p>'
    except KeyError:
        trailing_text = '<br/>Trailing P/E not found'
        forward_text = '<br/>Forward P/E not found</p>'

    return pe_text + trailing_text + forward_text
