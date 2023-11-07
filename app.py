from flask import Flask, send_from_directory

app = Flask(__name__)

# Define the directory containing static files (Tiles)
STATIC_FOLDER = 'Tiles'

# Route to serve static files from the Tiles directory
@app.route('/Tiles/<path:filename>')
def tiles(filename):
    return send_from_directory(STATIC_FOLDER, filename)

# Run the Flask app on port 8080
if __name__ == '__main__':
    app.run(port=4000)