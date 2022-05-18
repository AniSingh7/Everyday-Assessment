# Python is Interpreted − Python is processed at runtime by the Interpreter.
#                           You do not need to compile your program before executing it.
# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Python features
# Easy to code: Python is a high-level programming language.
# Free and Open Source:
# Object-Oriented Language: One of the key features of python is Object-Oriented programming.
#                           Python supports object-oriented language and concepts of classes, objects encapsulation, etc
# GUI Programming Support:
# High-Level Language: Python is a high-level language.
#                       When we write programs in python, we do not need to remember the system architecture
# Extensible feature: can write other languages also
# Python is Portable language: ...
# Python is Integrated language:Python is an Interpreted Language because Python code is executed line by line at a time.
# --------------------------------------------------------------------------------------------------------------------------------------------------------
#Flavors of python:
# Cpython:The default implementation of the Python programming language is Cpython.
#        As the name suggests Cpython is written in C language.
#Jython: It is an implementation of the Python programming language that can run on the Java platform.
#IronPython:A Python implementation written in C# targeting Microsoft’s .NET framework.
# --------------------------------------------------------------------------------------------------------------------------------------------------------
#Dynamically typed languages:Python is a dynamically typed language.
#                           It doesn’t know about the type of the variable until the code is run. So declaration is of no use.
#Procedure Oriented vs Object oriented programming languages
#In procedural programming, the program is divided into small parts called functions.
#   In object-oriented programming, the program is divided into small parts called objects.
#There is no access specifier in procedural programming.
#   Object-oriented programming has access specifiers like private, public, protected, etc
#Procedural programming does not have any proper way of hiding data so it is less secure
#   Object-oriented programming provides data hiding so it is more secure.
#In procedural programming, overloading is not possible.
#   Overloading is possible in object-oriented programming.
#In procedural programming, there is no concept of data hiding and inheritance.
#   In object-oriented programming, the concept of data hiding and inheritance is used.
#Procedural programming is based on the unreal world.
#   Object-oriented programming is based on the real world.
# --------------------------------------------------------------------------------------------------------------------------------------------------------
#To check version of python on cmd: python --version
# --------------------------------------------------------------------------------------------------------------------------------------------------------
#settings path
#using cmd :type:python -------------->command prompt (Temporary)
#by Environmental Variable Setup(Permanent)
#My Computer -> Properties -> Advanced System Settings ->Environment Variables -> User Variables ->

#There are 3 different ways to start Python –
#1. Interactive Interpreter :
# 2.	Script from the Command-line:
# 3. Integrated Development Environment:

#Automatic garbage collection
# Python deletes unwanted objects (built-in types or class instances) automatically to free the memory space.
# The process by which Python periodically frees and reclaims blocks of memory that no longer are in use is called Garbage Collection.

#Python deletes unwanted objects (built-in types or class instances) automatically to free the memory space.
# The process by which Python periodically frees and reclaims blocks of memory that no longer are in use is called Garbage Collection.




print("printing type of x and id(address) of x")
x=10.5
print(type(x), id(x))

y="Hello World!"
print("type of y is ", type(y))