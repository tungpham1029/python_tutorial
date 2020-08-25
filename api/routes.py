from flask import Flask, jsonify
from app import app, db


@app.route('/view_test', methods=['GET'])  # viewing all contents of bucketList
def get_test():
    users = db.users
    results = []
    result = users.find()
    for re in result:
        re.pop('_id')
        results.append(re)
    return jsonify(results)
