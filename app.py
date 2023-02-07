from scrapper import Scrapper
from flask import Flask

app = Flask(__name__)

@app.route("/ficha")
def getFicha():
  scrapper = Scrapper()
  result = scrapper.run()
  return result