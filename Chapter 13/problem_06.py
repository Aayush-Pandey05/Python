'''
Question:- Run pip freeze for the system interpreter. Take the contents and create a similar 
virtualenv.

'''
'''
Answer:- Basically we need to create a requirement.txt file in 
an env and input all the libraries that are present there, which 
we already did using the freeze (pip freeze > requirements.txt)
Now we will create another env and then import all these files 
from requirements.txt into it (pip install -r \.requrements.txt)

'''