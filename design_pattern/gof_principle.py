"""
Notes:
What is "Composition Over  Inheritance"?
- inheritances when a class inherit (gets) feature from parent class.
- composition means a class uses other classes by including them as parts instead of inheriting from them.

The idea is:
It's usually better to build classes using composition (has-a relationship) instead of inheritance (is-a relationship) because it's  more flexible and easier to maintain
"""

# using inheritance 

class User:
    def __init__(self, name):
        self.name = name
    

class AdminUser(User):
    def has_permission(self,action):
        return True
    
"""
Here AdminUser inherits from User. This seems fine, but if your logic get more complex it becomes hard to manage or change.
"""

# using composition

class User:
    def __init__(self, name):
        self.name = name

class Permission:
    def has_permission(self,action):
        return True
    
class AdminUser:
    def __init__(self, user, permission):
        self.user = user
        self.permission = permission

"""
Why is composition better?
- More Flexible : You can change parts (like permission) without changing the while class hierarchy.
- less Fragile : Changes in parent classes wont't accidentally break child classes
- easier to understand : Smaller, reusable parts are easier to test and debug.  
"""

# Adapter Pattern

"""
The Adapter pattern lets you wrap an object so that it fits another interface.
eg: Power adapter : your laptop plug doesn't fit  a European socket, so you use an adapter
"""

class EuropeanSocket:
    def plug_in(self):
        return "220V"
    
class USASocket:
    def connect(self):
        return "110V"

class SocketAdapter:
    def __init__(self, usa_socket):
        self.usa_socket = usa_socket
    
    def plug_in(self):
        return self.usa_socket.connect()
    

usa_socket = USASocket()
adapter = SocketAdapter(usa_socket)
print(adapter.plug_in())

# Bridge Pattern

"""
The Bridge Pattern is about separating abstraction from implementation so you can change them independently.

eg: TV remote: you ca have different remotes and different TVs, but they still work together because they've separated
"""

# Implementation:

class SonyTV:
    def on(self):
        print("Sony TV is on")

    def off(self):
        print("Sony TV is off")

class SamsungTV:
    def on(self):
        print("Samsung TV is on")
    
    def off(self):
        print("Samsung TV is off")


class RemoteControl:
    def __init__(self,tv):
        self.tv = tv

        
    def turn_on(self):
        self.tv.on()

    def turn_off(self):
        self.tv.off()

sony_remote = RemoteControl(SonyTV())
samsung_remote = RemoteControl(SamsungTV())

sony_remote.turn_on()
sony_remote.turn_off()

samsung_remote.turn_on()
samsung_remote.turn_off()

"""
How These Connect to "Composition over Inheritance":

- Both Adapter and Bridge rely on composition: they contain other  objects and use their behavior
- They don't inherit ond override everything instead they delegate work to internal components.
- This makes the code flexible, reusable and testable 
"""