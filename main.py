from flask import Flask,jsonify,request
import db_insert
import db_query

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['JSON_SORT_KEYS'] = False
app.config['ENV'] = 'development'

@app.route('/test',methods=['POST'])
def test():
	print('[INFO]--[test]--[FUNCTION]')
	id = request.form['id']
	quer = db_query.Query()
	response = quer.faculty_id_query(id)
	return jsonify({'names': response})

if __name__ == '__main__':
	app.run()
