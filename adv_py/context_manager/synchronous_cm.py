"""
Synchronous Context Managers
- are implemented using the __enter__() and __exit__() methods

# The __enter__() Method:
- The __enter__(self) method is  called when execution enters the context of the with statement.
- This method should return the resource to   be used  within the with block

# The __exit__() Method:
- The __exit__(self, exc_type,exc_value, traceback) method is called when execution leaves the context of the with statement. It can  handle exceptions if any occur, and it returns a Boolean flag indicating if the exception should be suppressed.

## params of __exit__
- exc_type: The exception class/type (e.g. ZeroDivisionError) if aan exception occurred. If no exception occurred, This will be None.
- exc_value: The actual exception instance(e.g. ZeroDivisionError("division by zero")). This  provides the error message and other data if no exception occurred, this is None.
-  traceback: A traceback object that contains information about where the exception occurred (file name, line number, etc.). If not exception occurred, this is None.
"""
import traceback

class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")

with MyContextManager():
    print("body")

print("-"*64)

# with exception example of exit

class MySecondContextManger:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, tb):
        print("Exiting the context")
        if exc_type:
            print("An exception has occurred")
            print(f"exc_value : {exc_value}")
            print("traceback : ")
            traceback.print_exception(exc_type,exc_value,tb)
        return True

with MySecondContextManger():
    print("body")
    name = "Test"/3 # will rase exception