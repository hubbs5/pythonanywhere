from app import app
import index

app.layout = index.layout

if __name__ == '__main__':
    app.run_server(port=8880, debug=True)