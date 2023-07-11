# E-WAITER

A python application created using Tkinter and Mysql for restaurants.  
Included speech to text module for additional support for the visually impaired.  

- dbcreate.py        creates the required database and tables in the local mysql database. Add the db credentials to the connector functions
- tkinter.py         includes the application using tkinter
- tkinter_speech.py  includes the sppech to text module along with appliucation


## Run Locally

Clone the project

```bash
  git clone https://github.com/MeTuL10/e-waiter.git
```

Go to the project directory

```bash
  cd e-waiter
```
Edit the following command in the 3 scripts, add credentials
```Python
mydb=msql.connect(host='',user='',passwd='')
```
Run the scripts in the following order
```bash
pip install mysql-connector-python
pip install pyttsx3
pip install matplotlib
python3  dbcreate.py
python3 tkinter.py
```
Or you can run  ```tkinter_speech.py``` for speech to text option
