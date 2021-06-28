
## environment:


## june 28_2021:


## 0
```python
## sudo apt-get install python3-pip
## taxi@taxi-HP-ProBook-4540s:~/Python-3.9.4$ whereis pip
pip: /usr/bin/pip /home/taxi/.local/bin/pip /home/taxi/.local/bin/pip3.9 /usr/share/man/man1/pip.1.gz
taxi@taxi-HP-ProBook-4540s:~/Python-3.9.4$ sudo apt-get install python3-pip



```
## 1
```python
taxi@taxi-HP-ProBook-4540s:~/Programs/Python-Image-to-PDF-convert$ python3 -m pip install --upgrade pillow
Collecting pillow
  Downloading Pillow-8.2.0-cp38-cp38-manylinux1_x86_64.whl (3.0 MB)
     |████████████████████████████████| 3.0 MB 2.0 MB/s 
Installing collected packages: pillow
Successfully installed pillow-8.2.0
taxi@taxi-HP-ProBook-4540s:~/Programs/Python-Image-to-PDF-convert$ 

```

## 2

```python
taxi@taxi-HP-ProBook-4540s:~/Programs/Python-Image-to-PDF-convert$ code .
taxi@taxi-HP-ProBook-4540s:~/Programs/Python-Image-to-PDF-convert$ cd src/
taxi@taxi-HP-ProBook-4540s:~/Programs/Python-Image-to-PDF-convert/src$ python convert.py 
Traceback (most recent call last):
  File "/home/taxi/Programs/Python-Image-to-PDF-convert/src/convert.py", line 1, in <module>
    from PIL import Image
  File "/home/taxi/.local/lib/python3.9/site-packages/PIL/Image.py", line 31, in <module>
    import math
ModuleNotFoundError: No module named 'math'
taxi@taxi-HP-ProBook-4540s:~/Programs/Python-Image-to-PDF-convert/src$ python convert.py 
Traceback (most recent call last):
  File "/home/taxi/Programs/Python-Image-to-PDF-convert/src/convert.py", line 1, in <module>
    from PIL import Image
  File "/home/taxi/.local/lib/python3.9/site-packages/PIL/Image.py", line 31, in <module>
    import math
ModuleNotFoundError: No module named 'math'
taxi@taxi-HP-ProBook-4540s:~/Programs/Python-Image-to-PDF-convert/src$ python3 convert.py 
Done
taxi@taxi-HP-ProBook-4540s:~/Programs/Python-Image-to-PDF-convert/src$ 

```


## old ## old ## old ## old ## old ## old ## old ## old

## python -V Python 3.9.4

taxi@taxi-HP-ProBook-4540s:~/Programs/2021$ cd Python-Image-to-PDF-convert/
taxi@taxi-HP-ProBook-4540s:~/Programs/2021/Python-Image-to-PDF-convert$ 
## taxi@taxi-HP-ProBook-4540s:~/Programs/2021/Python-Image-to-PDF-convert$ pip -V
bash: /home/taxi/.local/bin/pip: /usr/local/bin/python3.9: bad interpreter: No such file or directory
## taxi@taxi-HP-ProBook-4540s:~/Programs/2021/Python-Image-to-PDF-convert$ python -m pip -V
pip 21.0.1 from /home/taxi/.local/lib/python3.9/site-packages/pip (python 3.9)
taxi@taxi-HP-ProBook-4540s:~/Programs/2021/Python-Image-to-PDF-convert$ 

## need to install this: https://pillow.readthedocs.io/en/latest/installation.html



## taxi@taxi-HP-ProBook-4540s:~/Programs/2021/Python-Image-to-PDF-convert$ python -m pip install --upgrade pip
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: pip in /home/taxi/.local/lib/python3.9/site-packages (21.0.1)
Collecting pip
  Downloading pip-21.1.1-py3-none-any.whl (1.5 MB)
     |████████████████████████████████| 1.5 MB 989 kB/s 
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 21.0.1
    Uninstalling pip-21.0.1:
      Successfully uninstalled pip-21.0.1
Successfully installed pip-21.1.1
## taxi@taxi-HP-ProBook-4540s:~/Programs/2021/Python-Image-to-PDF-convert$ python -m pip install --upgrade pillow
Defaulting to user installation because normal site-packages is not writeable
Collecting pillow
  Downloading Pillow-8.2.0-cp39-cp39-manylinux1_x86_64.whl (3.0 MB)
     |████████████████████████████████| 3.0 MB 717 kB/s 
Installing collected packages: pillow
Successfully installed pillow-8.2.0
taxi@taxi-HP-ProBook-4540s:~/Programs/2021/Python-Image-to-PDF-convert$ D
