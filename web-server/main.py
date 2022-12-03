import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()
@app.get('/')
def get_list():
    return [1, 2, 3]

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return """
    <h1>Hola primera pagina en python</h1>
    <p>primer parrafo</p>
    """

def run():
    store.get_categorias()

if __name__ == '__main__':
    run()