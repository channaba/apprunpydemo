from flask import Flask
import os

PORT = 8080
name = os.environ['NAME']

if name == None or name.len() == 0:
  name = "AWS" 
  
 MESSAGE = "Hello, " + name + "!\n"
  
