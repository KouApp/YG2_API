from flask import Flask,jsonify,request

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['JSON_SORT_KEYS'] = False
app.config['ENV'] = 'development'

@app.route('/test',methods=['POST'])
def test():
	print('[INFO]--[test]--[FUNCTION]')
	name = request.form['name']
	return jsonify({'names': name})

if __name__ == '__main__':
	app.run()