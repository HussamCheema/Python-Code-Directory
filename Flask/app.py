from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [

    {
        "author": "Hussam Cheema",
        "title": "First Post",
        "published_on": "20 June, 2020",
        "content": "This is my First Blog"
    },
    {
        "author": "Haseeb Hassan",
        "title": "Second Post",
        "published_on": "21 July, 2020",
        "content": "This is about Artificial Intelligence"
    },

]


@app.route('/')
@app.route('/home/')
def hello_world():
    return render_template('home.html', posts=posts)


@app.route('/about/')
def about():
    return render_template('about.html', title="About")


if __name__ == '__main__':
    app.run(debug=True)
