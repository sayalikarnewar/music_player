from script import get_input, play, display

def routes(app):
    
    app.router.add_get('/', get_input)
    app.router.add_post('/', play, name='play')