from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'data-analyst',
        'location': 'Astana, Kazakhstan',
        'salary': '900,000'
    },
    {
        'id': 2,
        'title': 'web-developer',
        'location': 'Astana, Kazakhstan',
        'salary': '1,800,000'
    },
    {
        'id': 3,
        'title': 'waiter',
        'location': 'Astana, Kazakhstan',
        'salary': '200,000'
    },
    {
        'id': 4,
        'title': 'ml engineer',
        'location': 'Astana, Kazakhstan',
        'salary': '4,800,000'
    },
]

@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name='Jovian')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
