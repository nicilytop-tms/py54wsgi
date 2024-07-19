import json
from urllib.parse import parse_qsl


def get_summ(env):
    result = env["wsgi.input"].read()  # [('first', '876'), ('second', '434')]
    res_dict = dict(parse_qsl(result.decode()))
    result_summ = int(res_dict["first"]) + int(res_dict["second"])
    return f"""
    <html>
    <head><title>This is summ</title></head>
    <body>
    <h3>{result_summ}</h3>
    <form method="POST" action="http://localhost:8000/">
    <input type="number" name="first" placeholder="Input first n">
    <input type="number" name="second" placeholder="Input second n">
    <input type="submit" value="Summ please">
    </form>
    </body>
    </html>
    """


def get_html(env):
    body = """
    <html>
    <head><title>This is summ</title></head>
    <body>
    <form method="POST" action="http://localhost:8000/">
    <input type="number" name="first" placeholder="Input first n" value="3">
    <input type="number" name="second" placeholder="Input second n" value="4">
    <input type="submit" value="Summ please">
    </form>
    </body>
    </html>
    """
    return body


def app(env, start_resp):
    methods_and_func = {
        'POST': get_summ,
        'GET': get_html,
    }

    method = env['REQUEST_METHOD']
    result = methods_and_func[method](env)
    start_resp("200", [("Content-Type", "text/html")])
    return (result.encode(),)
