
class SumSolution:
    
    def compute(self, x:int, y:int)->int:
        """_summary_

        Args:
            x (int): _description_
            y (int): _description_

        Raises:
            TypeError: _description_
            TypeError: _description_
            ValueError: _description_
            ValueError: _description_

        Returns:
            int: _description_
        """
        if not isinstance(x,int):
            raise TypeError(f"'x' must be of type ")
        if not isinstance(y,int):
            raise TypeError(f"")
        if not (0<=x<=100):
            raise ValueError(f"'x' must be between 0 and 100, got {x}")
        if not (0<=y<=100):
            raise ValueError(f"'y' must be between 0 and 100, got {y}")
        return x + y



