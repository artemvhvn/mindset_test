from flask import Flask, request, jsonify, redirect, render_template
from neo4j import GraphDatabase

driver = GraphDatabase.driver(uri="bolt://localhost:7687", auth=("artemvhvn", "12345678"))
session = driver.session(database='testdb')

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/<string:name>', methods=['GET', 'POST'])
def display(name):
    q = '''
    MATCH (name)-[rel]-(secname) WHERE name.name = $name return name, rel, secname
    '''
    map = {'name': name}
    results = session.run(q, map)
    data = results.data()
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5050)
