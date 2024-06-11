from app import create_app, db
from flask_migrate import upgrade

app = create_app()

@app.before_first_request
def setup():
    upgrade()

if __name__ == '__main__':
    app.run(debug=True)
