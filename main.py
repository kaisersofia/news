from flask import Flask, render_template, request
news = {}
# созд объект
app = Flask(__name__)

@app.route("/") # созд url  к след функции
def home_page():  # создаем views
    return render_template("index.html")


# динамичная ссылка
@app.route("/user/<int:pk>/news/<string:name>")
def user_info(pk, name): # сохраняю число в переменную
    return f"информация о новости {name} юзера {pk}"


@app.route("/add-news", methods=["POST", "GET"])
def add_question():
    if request.method == "POST":
       title = request.form.get("title")
       main_text = request.form.get("main_text")
       news[title] = main_text
       return render_template("news.html")
    elif request.method == "GET":
        return "так по ссылке переходит нельзя"

app.run(debug=True)