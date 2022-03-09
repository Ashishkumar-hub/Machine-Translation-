from flask import Flask, request, jsonify,render_template
import os
from flask_cors import CORS, cross_origin
from translator import translation

#predict(text)
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    text = request.json["text"]
    trans = translation(text)
    result = trans.translate_word()
    print(result)
    print(type(result))
    return {"Result": str(result)}


#port = int(os.getenv("PORT"))
if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=port)
    app.run(host='127.0.0.1', port=8000, debug=True)

