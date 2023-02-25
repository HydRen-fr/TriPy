import algorithm
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tri', methods=['GET'])
def tri():
    array_length = int(request.args.get('array-length'))
    array = algorithm.set_random_array(array_length)

    sort_name = request.args.get('sort')
    sort_algo = algorithm.create(sort_name, array)

    template_content = sort_algo.video

    return render_template('tri.html', array=array, sort_algo=sort_algo, template_content=template_content)

if __name__ == "__main__":
    app.run(debug=True)