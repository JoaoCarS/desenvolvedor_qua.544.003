from flask import Flask, request, render_template
import pyautogui as auto
from datetime import date
import webview
import os
import sys 


if getattr(sys, 'frozzen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys.MEIPASS, 'static')
    app = Flask(__name__, teemplate_folder=template_folder, static_folder=static_folder)
else:
    app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/commitar', methods = ['POST'])
def commitar():
    hoje = date.today().strftime("%d/%m/%Y")
    repositorio = None
    if request.method == "POST":
        repositorio = request.form.get("repositorio","")

    if repositorio:
        auto.PAUSE = 1
        auto.hotkey("win", "r")
        auto.write("cmd")
        auto.press("enter")
        auto.write(f"cd {repositorio}")
        auto.press("enter")
        auto.write("git add .")
        auto.press("enter")
        auto.write(f'git commit -m "Commit do dia {hoje}"')
        auto.press("enter")
        auto.write("git push")
        auto.press("enter")
        auto.sleep(3)
        auto.write("exit")
        auto.press("enter")

    return render_template('index.html')

if __name__ == "__main__":
    # app.run(debug=True)
    window = webview.create_window(
        title="poltergit",
        url=app,
        width=1000,
        height=700
    )

    webview.start()