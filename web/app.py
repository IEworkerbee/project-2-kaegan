"""
Kaegan Koski's Flask API.
"""

from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__)

@app.route("/<string:page_r>")
def page_server(page_r):
    if (".." in page_r or "~" in page_r):
        abort(403)

    elif (os.path.isfile("pages/{}".format(page_r))):
        return send_from_directory("pages/", page_r), 200

    else:
        abort(404)

# Could not find page in pages directory
@app.errorhandler(404)
def page_not_found(e):
    return send_from_directory("pages/", "404.html"), 404

# Illegal characters in page request
@app.errorhandler(403)
def forbidden_request(e):
    return send_from_directory("pages/", "403.html"), 403

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
