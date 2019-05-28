import flask
from flask import Flask, request

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")

@app.route("/")
def root():
    return flask.render_template(
        'index.html'
    )

@app.route('/translate', methods=['GET'])
def translate():
    txt = request.args.get('text')

    if txt == None:
        txt = "Пробный текст"

    translates = {
        ("А", "а"): "A", ("Б", "б"): "B", ("В", "в"): "V",
        ("Г", "г"): "G", ("Д", "д"): "D", ("Е", "е"): "E",
        ("Ё", "ё"): "E", ("Ж", "ж"): "zh", ("З", "з"): "z",
        ("И", "и"): "N", ("Й", "й"): "y", ("К", "к"): "K",
        ("Л", "л"): "L", ("М", "м"): "M", ("Н", "н"): "H",
        ("О", "о"): "O", ("П", "п"): "p", ("Р", "р"): "P",
        ("С", "с"): "S", ("Т", "т"): "T", ("У", "у"): "u",
        ("Ф", "ф"): "F", ("Х", "х"): "X", ("Ц", "ц"): "ts",
        ("Ч", "ч"): "ch", ("Ш", "ш"): "sh", ("Щ", "щ"): "csh",
        ("Ъ", "ъ"): "b", ("Ы", "ы"): "bI", ("Ь", "ь"): "b",
        ("Э", "э"): "e", ("Ю", "ю"): "U", ("Я", "я"): "R",
    }

    res = ''
    for i in txt:
        f = True
        for j in translates.keys():
            if f and i in j:
                res += translates.get(j)
                f = False
        if f:
            res += i

    return flask.render_template(
        'translate.html',
        res=res,
        num=txt,
        method=request.method
)

if __name__ == '__main__':
    app.run(debug=True)