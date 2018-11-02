from flask import jsonify

preds = {'scores': [0.99, 0.12]}

def test1():
    if not any([score > 0.9 for score in preds['scores']]):
        return jsonify(result=False)    

