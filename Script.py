import pyshorteners


link = input("Digite a URL: ")
url = pyshorteners.Shortener ()

url_curta = url.tinyurl.short(link)

print(f'Link Encurtado: {url_curta}')