def url_shortener(long_url):
    return str(hash(long_url))[:10]
