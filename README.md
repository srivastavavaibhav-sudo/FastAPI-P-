IN This project, I created Address book using FastAPI and sqlite with langauge python.

for run :

step=1) 1.1) if venv not present in dir please create virtualenv first.
                                                 OR
         1.2) if venv present in dir. then activate it .
        1.2.1) activate environment <<----this environment is create in window OS ---->>> 
                    a)cd venv b)cd scripts c)activate
        1.2.2) activate environment <<----this environment is create in Linux OS ---->>>
                    a)come in dir where enviroment are present 
                    b)Source (name of enviroment)/bin/activate

1.1) for deactivate.
    a)cd venv
    b)cd scripts
    c)deactivate

step = 2) install requirements.txt fil.

        with cmd ( pip install -r requirements.txt )
        make sure you are in dir. of requirement.txt
        
step = 3) <<<<--- project_name == FastAPI_Eastvantage -->>>>>


    For run using cmd: ( uvicorn main:app --reload )
