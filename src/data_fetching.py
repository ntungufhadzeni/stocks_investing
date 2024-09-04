import yfinance as yf
import pandas as pd


def get_ticker_data(ticker_symbol):
    return yf.Ticker(ticker_symbol)


def get_financial_data(ticker_data):
    financials = ticker_data.financials.transpose().iloc[::-1].copy()
    incomes = ticker_data.balancesheet.transpose().iloc[::-1].copy()
    cashflows = ticker_data.cashflow.transpose().iloc[::-1].copy()
    return {
        'financial': financials,
        'income': incomes,
        'cashflow': cashflows
    }


def get_company_info(ticker_data):
    return pd.DataFrame([ticker_data.info])
