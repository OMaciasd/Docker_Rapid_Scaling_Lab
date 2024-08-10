def init_app(app):
    @app.route('/app')
    def app_route():
        return "This is the app route!"
