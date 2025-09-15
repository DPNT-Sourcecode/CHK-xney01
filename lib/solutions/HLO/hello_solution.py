
class HelloSolution:
    
    # friend_name = unicode string
    def hello(self, friend_name:str)->str:
        if not isinstance(friend_name,str):
            raise TypeError(f"'friend_name' must be of type {type(friend_name)}")
        return f"Hello, World!"


