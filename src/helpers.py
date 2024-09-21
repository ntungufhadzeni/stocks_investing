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


def get_chart_footnote(column_name):
    footnote_text = {
        "Gross Margin %": "**Gross Margin %:** *Represents the percentage of revenue that exceeds the cost of goods "
                          "sold (COGS). A higher gross margin indicates more efficient production and greater pricing "
                          "power, while a lower margin suggests higher production costs relative to revenue.*",
        "Net Margin %": "**Net Margin %:** *Indicates the percentage of revenue that remains as profit after all "
                        "expenses, including operating costs, interest, taxes, and other expenses, are deducted. A "
                        "higher net margin reflects better overall profitability, while a lower margin may signal "
                        "higher costs or lower revenue retention.*",
        "Long Term Debt over Earnings": "**Long-Term Debt Over Earnings:** *Measures a company's ability to cover "
                                        "its long-term debt obligations with its earnings. A lower ratio indicates "
                                        "stronger financial stability and a better capacity to manage debt, while a "
                                        "higher ratio may signal potential challenges in meeting debt obligations.*",
        "Expenditure over Income %": "**Expenditure Over Income %:** *Represents the proportion of a company’s income "
                                     "that is spent on expenses. A lower percentage indicates greater efficiency in "
                                     "managing expenses relative to income, while a higher percentage may suggest "
                                     "that a significant portion of income is consumed by costs.*",
    }
    return footnote_text.get(column_name)
