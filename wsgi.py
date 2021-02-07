# from app import app
# 
# if __name__ == "__main__":
#     app.run()

from sunrise_lamp import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
