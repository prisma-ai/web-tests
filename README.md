# web-tests
To install all libraries run 
```
pip install -r requirements.txt
```
Then install browsers 
```
playwright install
```
To launch tests run command  
```
python -m pytest - to run all tests
python -m pytest tests/test_check_signin.py - to run specific test suite
python -m pytest tests/test_check_signin.py::xxx - xxx is the name of test, to run specific test
```
