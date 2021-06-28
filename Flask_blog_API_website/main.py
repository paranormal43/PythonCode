from flask import Flask, render_template
from post import Post

app = Flask(__name__)
all_data = Post()
data = all_data.get_data()

@app.route('/')
def home():
    return render_template("index.html", post_data = data)

@app.route('/post/<int:title_id>')
def get_post(title_id):
    # print(data[int(title_id)])
    return render_template("post.html",post_data = data[title_id-1])

if __name__ == "__main__":
    app.run(debug=True)
