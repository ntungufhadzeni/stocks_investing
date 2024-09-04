import pandas as pd


def calculate_ratios(financial_data):
    df = pd.DataFrame(index=financial_data['financial'].index)
    df['Gross Margin %'] = financial_data['financial']['Gross Profit'] / financial_data['financial'][
        'Total Revenue'] * 100
    df['Net Margin %'] = financial_data['financial']['Net Income'] / financial_data['financial']['Total Revenue'] * 100

    if 'Long Term Debt' in financial_data['income']:
        df['Long Term Debt over Earnings'] = financial_data['income']['Long Term Debt'] / financial_data['income'][
            'Retained Earnings']
    else:
        df['Long Term Debt over Earnings'] = 0

    df['Expenditure over Income %'] = - financial_data['cashflow']['Capital Expenditure'] / financial_data['financial'][
        'Net Income'] * 100
    return df
