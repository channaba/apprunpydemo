from flask import Flask
import os

PORT = 8080

name=os.environ['NAME']
# name2=os.environ['NAME2']

if name == None or name == "None" or len(name) == 0:  
   name = "AWS"
MESSAGE = "Good morning, " + name  + "!"
print("Message: '" + MESSAGE + "'")

app = Flask(__name__)
@app.route("/")
def root():  
  print("Handling web request. Returning message.")  
  result = MESSAGE.encode("utf-8")  
  return result
 
if __name__ == "__main__":  
  app.run(debug=True, host="0.0.0.0", port=PORT)

