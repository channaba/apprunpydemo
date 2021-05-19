from flask import Flask
import os

PORT = 8080
name = os.environ['NAME']

if name == None or len(name) == 0:
   name = "AWS" 
    
MESSAGE = "Hello, " + name + "!\n"
