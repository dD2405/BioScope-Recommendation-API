from flask import Flask,request,jsonify
import recommendation
from flask_cors import CORS

app = Flask(__name__)
CORS(app)    
        
@app.route('/movie', methods=['GET'])
def recommend_movies():
        res = recommendation.results(request.args.get('title'))
        return jsonify(res)

if __name__=='__main__':
        app.run(port = 5000, debug = True)
