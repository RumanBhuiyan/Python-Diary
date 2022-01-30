import traceback

# traceback helps us to access the error tree thrown in terminal
try :
    quotient = 5/0
except Exception as e:
    print(e)
    traceback.print_exc()