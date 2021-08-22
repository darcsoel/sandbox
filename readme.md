This repository was created for learning purpose

Sync dependencies with `pip-compile --output-file requirements.txt requirements.in`


You need Python 3.7 to run async code

Folder `pure_python` contains legacy code, it need refactoring

For use graphic library <br>
`sudo apt-get install graphviz`

If problems with basemap package:

`sudo apt-get install libgeos-dev` 
<br>
`pip3 install -U git+https://github.com/matplotlib/basemap.git`


For launch GUI tkinter <br>
`sudo apt-get install python3-tk`

Install flake8 <br>
`pip3 install flake8` <br>
`flake8 --install-hook git`

Enable strict and lazy check <br>
`git config --bool flake8.strict true` <br>
`git config --bool flake8.lazy true`

Docs <br>
https://flake8.pycqa.org/en/latest/user/using-hooks.html