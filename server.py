#This code is from AWS Sample code for my personal study.
#https://docs.aws.amazon.com/apprunner/latest/dg/getting-started.html

from flask import Flask
import os

PORT = 8080
name = os.environ['NAME']
if name == None or len(name) == 0:
  name = "world"
MESSAGE = "<html><meta charset=\"utf-8\"/><body>Hello こんにちは, " + name + "!</body></html>"
print(MESSAGE)

app = Flask(__name__)


@app.route("/")
def root():
  print("Handling web request. Returning message.")
  result = MESSAGE.encode("utf-8")
  return result


if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=PORT)