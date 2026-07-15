from urllib.parse import urlparse
import webbrowser

def open_url(url:str):
    if not url.startswith(("http://","https://")):
        url="https://"+url
    parsed=urlparse(url)
    if not parsed.netloc:
        return {"error":"Invalid URL"}
    try:
        webbrowser.open(url)
        return {"status":"opened","url":url}
    except Exception as e:
        return {"error":str(e)}
