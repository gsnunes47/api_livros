from biblioteca import app

with app.app_context():
    app.run(port=5000, host='localhost', debug=True)
