import streamlit as st

from bbquote.quote import get_quote

quote, author = get_quote()  # assuming the function returns an author and a quote

f"{quote}, by {author}"