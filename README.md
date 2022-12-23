<div align="center">
<h1>PYTHON</h1>
<p>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/1200px-Python.svg.png" alt="Python" width=200px/>
</p>
<br>
<p> <b>The Python project is an API to create posts in a simple social media<b> </p>
 
 ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
 
 ## INSTALLATION
 
 ```
# Clone this repository
$ git clone https://github.com/Rodolpho-Oliveira/projeto-python.git

# Go into the repository
$ cd projeto-python

 ```
 
 ## USAGE
 
 POST ```/sign-up```<br>
 
 Need to receive through the body a parameter ```username``` and an ```avatar```
 ```
 {
    username: "randomName",
    avatar: "https://www...."
 }
 ```
 
 POST ```/tweets```<br>
 
 Need to receive through the body a parameter ```username``` and ```tweet```
 ```
 {
    username: "randomName",
    tweet: "I want to hire this dev!"
 }
 ```
 
 GET ```/tweets```<br>
 
 Return the last 10 tweets
 ```
 [
   {
      username: "randomName",
      avatar: "https://www...",
      tweet: "I want to hire this dev!"
   }
 ]
 ```
 
 
