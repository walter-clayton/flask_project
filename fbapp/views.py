from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    description = """Welcome"""
    return render_template('index.html',
                            user_name="Walter",
                            user_image=url_for('static', filename="tmp/cover_111823112767411.jpg"),
                            description=description,
                            blur = True)


@app.route('/result/')
def result():
    description = """Results Page !"""
    return render_template('result.html',
                            user_name="Walter",
                            user_image=url_for('static', filename="tmp/cover_111823112767411.jpg"),
                            description=description)


if __name__ == "__main__":
    app.run()


app.config.from_object('config')