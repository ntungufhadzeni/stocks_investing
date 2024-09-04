import streamlit as st
from data_fetching import get_ticker_data, get_financial_data, get_company_info
from data_processing import calculate_ratios
from plotting import plot_financial_ratio
from helpers import get_threshold, display_pe_ratio


def main():
    st.title('Financial Ratio Analysis')

    # User Input for Ticker Symbol
    ticker_symbol = st.text_input('Enter Ticker Symbol:', 'AAPL')

    # Fetch and Process Data
    ticker_data = get_ticker_data(ticker_symbol)
    financial_data = get_financial_data(ticker_data)

    try:
        df = calculate_ratios(financial_data)
        df_info = get_company_info(ticker_data)

        # Display P/E Ratio Information
        st.markdown(display_pe_ratio(df_info), unsafe_allow_html=True)

        # Select and Plot Financial Ratios
        selected_ratio = st.selectbox('Select Ratio to View:', df.columns)
        threshold, better_is_higher = get_threshold(selected_ratio)
        fig = plot_financial_ratio(df.copy(), selected_ratio, threshold, better_is_higher)
        st.plotly_chart(fig)

    except KeyError:
        st.write("No data")


if __name__ == '__main__':
    main()
