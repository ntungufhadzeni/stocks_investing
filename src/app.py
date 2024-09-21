import streamlit as st
from data_fetching import get_ticker_data, get_financial_data, get_company_info
from data_processing import calculate_ratios
from plotting import plot_financial_ratio
from helpers import get_threshold, display_pe_ratio, get_chart_footnote


def main():
    st.title('Financial Ratio Analysis')

    # User Input for Ticker Symbol
    ticker_symbol = st.text_input('Enter Ticker Symbol:', 'AAPL')

    # Fetch and Process Data
    ticker_data = get_ticker_data(ticker_symbol)

    try:
        financial_data = get_financial_data(ticker_data)
        df = calculate_ratios(financial_data)

        df_info = get_company_info(ticker_data)

        # Display P/E Ratio Information
        st.markdown(display_pe_ratio(df_info), unsafe_allow_html=True)

        for selected_ratio in df.columns:
            threshold, better_is_higher = get_threshold(selected_ratio)
            fig = plot_financial_ratio(df.copy(), selected_ratio, threshold, better_is_higher)
            st.plotly_chart(fig)
            footnote = get_chart_footnote(selected_ratio)
            st.markdown(footnote)
    except Exception as e:
        st.write("No data")


if __name__ == '__main__':
    main()
