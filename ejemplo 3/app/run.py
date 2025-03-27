from flask import Flask, request, jsonify, abort, render_template, redirect, url_for, session, escape
import sys

# Config Flask
app = Flask(__name__)
app.secret_key = 'jupiter'
app.config.update(
    DEBUG=True,
    JSON_SORT_KEYS=True
)

# Root
@app.route('/')
@app.route('/index')
def main():
        return render_template('index.html')
    
if __name__ == '__main__':
    if len(sys.argv) < 2:
        #print "usage: %s port" % (sys.argv[0])
        sys.exit(-1)

    p = int(sys.argv[1])
    app.run(host='0.0.0.0', port=p, debug=True, threaded=True)