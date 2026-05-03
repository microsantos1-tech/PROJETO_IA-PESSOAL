import requests
from bs4 import BeautifulSoup

def ler_site(url):
  

  headers = {"User-Agent": "Mozilla/5.0"}
  resposta = requests.get(url, headers=headers, timeout=8)
 
  sopa = BeautifulSoup(resposta.text, "html.parser")

  parágrafos = [p.get_text() for p in sopa.find_all("p")]
  return "\n".join(parágrafos)[:2000]