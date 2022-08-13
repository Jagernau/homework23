import os
from flask import Flask, request
from utils import check_count_args, foo

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query")
def perform_query():
    kwargs = {
    "cmd1": request.args.get('cmd1'),
    "cmd2": request.args.get('cmd2'),
    "val1": request.args.get('val1'),
    "val2": request.args.get('val2'),
    "file_name": request.args.get('file_name')
}
    kwargs["file_path"] = os.path.join(DATA_DIR, str(kwargs["file_name"]))
    

    check_count_args(**kwargs)
    
    f = open(kwargs["file_path"])
    res = foo(f, kwargs["cmd1"], kwargs["val1"])
    

    if kwargs["cmd2"] and kwargs["val2"]:
        res = foo(res, kwargs["cmd2"], kwargs["val2"])
    res = res = "\n".join(res)
    f.close()

    return app.response_class(res, content_type="text/plain"), 200

if __name__ == "__main__":
    app.run()
