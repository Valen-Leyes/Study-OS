import streamlit as st
import random

class QuotesDisplay:
    def __init__(self, quotes):
        # Define the quotes
        self.quotes = quotes
        # Create an empty container for the quote
        self.quote_container = st.empty()

    def get_random_quote(self):
        # Get a random quote
        random_quote = random.choice(self.quotes)
        return f"\"{random_quote['quote']}\" - {random_quote['author']}"

    def update_quote(self):
        # Get a random quote
        quote = self.get_random_quote()
        # Update the quote display
        self.quote_container.markdown(f"<p style='text-align: center; font-size: 20px;'>{quote}</p>", unsafe_allow_html=True)

    # Display the quote
    def display(self):
        self.update_quote()
