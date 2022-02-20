from bbquote.quote import get_quote

def test_quote_type():
    quote_type = type(get_quote())
    assert quote_type == str