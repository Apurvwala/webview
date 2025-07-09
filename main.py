from threading import Thread
from kivy.app import App
from kivy.uix.label import Label
import webbrowser
from app import app as flask_app

def run_flask():
    flask_app.run(host='0.0.0.0', port=5000)

class FaceApp(App):
    def build(self):
        Thread(target=run_flask, daemon=True).start()
        webbrowser.open('http://localhost:5000')
        return Label(text="FaceApp Running...\nPlease wait...")

if __name__ == '__main__':
    FaceApp().run()
