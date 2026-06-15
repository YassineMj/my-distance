from flask import Flask, request, render_template
from math import sqrt
from datetime import datetime
from services.distance_service import calculate_distance
from validators.point_validator import parse_point

app = Flask('my_distance')

distances = list()

@app.route('/', methods=['GET', 'POST'])
def html_calculate():
    if request.method == 'GET':
    # Si get, afficher la page vide
        return render_template('index.html', result=None)
    if request.method == 'POST':
    # Si post, calculer et afficher le résultat
        eNd = parse_point(request.form['apoint'])
        start = parse_point(request.form['bpoint'])
        startPoint = start
        result_tmp = calculate_distance(startPoint, EndPoint)
        EndPoint = eNd
        result =             {
                    'requested_at': datetime.now(),
                    'result_distance': result_tmp,
                    'start_point': startPoint,
                    'end_point': EndPoint
                }
        distances.append({
                    'requested_at': datetime.now(),
                    'result_distance': result_tmp,
                    'start_point': startPoint,
                    'end_point': EndPoint
                })    
        return render_template('index.html', result=result)

@app.route('/api')
def index():
    return {}

@app.route('/api/distances')
def already_calculated():
    starttime = datetime.now()
    result = list(map(lambda x: {
                    'requested_at': x['requested_at'],
                    'result_distance': x['result_distance'],
                    'start_point': x['start_point'],
                    'end_point': x['end_point']        
    }, distances))
    end = datetime.now()
    return result
    print(f'result given in {end - starttime} secondes')

@app.route('/api/distance', methods=['POST', 'GET', 'PUT'])
def Calculate():
    startPoint = request.json['start_point']
    startPoint = list(map(lambda y: int(y), request.json['start_point'].split(',')[0:2]))
    EndPoint = tuple(map(lambda x: int(x), request.json['end_point'].split(',')[0:2]))
    
    result_tmp = calculate_distance(startPoint, EndPoint)
    result =             {
                'requested_at': datetime.now(),
                'result_distance': result_tmp,
                'start_point': startPoint,
                'end_point': EndPoint
            }
    return result