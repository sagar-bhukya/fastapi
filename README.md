A super fast Python web framework

1-create virtual environment
   pip install virtualen
   virtualenv fastapi-env
   \ cd fastapi-env
   \cd Scripts
   \activate
   \cd..
   \cd..
   now in fastapi folder
2. pip install fastapi -in the environment
3.pip install uvicorn - uvicorn is 


running the file-----------------
uvicorn main:app --reload


if the functions name are same but request and path is different its okay, so its no matter if the functions has same name



path parameters========
      @app.get('/blog/{id}') # dynamically given 
      def show(id):
         #fetch blog with id
         return {'data':id}

      output:
      {
      "data": 100
      }

      --with type in function
      @app.get('/blog/{id}') # dynamically given  # by default id takes strings if you want give type goto fucntion
      def show(id : int): #mention here which type do you want
         #fetch blog with id
         return {'data':id}

      output:
      {
      "data": "100"
      }


