from flask import Flask, request, jsonify
from flask_cors import CORS
import corrector
import transliterate
import phrase_maker

app = Flask(__name__)
CORS(app)    

grammar_corrector_model = corrector.correct_sentence
transliterator_model = transliterate.predict_sentence
sentence_maker = phrase_maker.sentence_builder


@app.route("/grammar_corrector", methods=["POST"])
def grammar_corrector():
    text = request.json["text"]

    corrected_text, error_type, explanation = grammar_corrector_model(text)

    return jsonify({
        "output": corrected_text,
        "error_type": error_type,
        "explanation": explanation
    })


@app.route("/transliterator", methods=["POST"])
def transliterator_route():
    text = request.json["text"]

    tamil_text = transliterator_model(text)

    return jsonify({
        "output": tamil_text
    })


@app.route("/sentence_builder", methods=["POST"])
def sentence_builder():
    subject = request.json["subject"]
    object_ = request.json["object"]
    verb = request.json["verb"]
    tense = request.json["tense"]

    sentence = sentence_maker(subject, object_, verb, tense)

    return jsonify({
        "output": sentence
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)