from flask import Flask

from main.core import home, get_all_candidates, get_candidate_by_uuid, get_candidate_section


# Defining Flask App
app = Flask(__name__)

# Defining URLs
app.add_url_rule('/', 'home', view_func=home, methods=['GET'])
app.add_url_rule('/candidates', view_func=get_all_candidates, methods=['GET'])
app.add_url_rule('/candidates/<string:uuid>', view_func=get_candidate_by_uuid, methods=['GET'])
app.add_url_rule('/candidates/<string:uuid>/<string:section>', view_func=get_candidate_section, methods=['GET'])

# Just for testing purposes
@app.cli.command()
def print_data():
    response = get_all_candidates()
    data = response.data.decode("utf-8")
    print(data)


if __name__ == "__main__":
    app.run(debug=True)
