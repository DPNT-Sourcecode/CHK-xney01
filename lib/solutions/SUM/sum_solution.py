
class SumSolution:
    
    def compute(self, x:int, y:int)->int:
        """Adds two integers (strictly) between 0 and 100

        Args:
            x (int): First integer (0<x<100)
            y (int): Second integer (0<y<100)

        Raises:
            TypeError: _description_
            ValueError: _description_

        Returns:
            int: The sum of x and y
        """
        if not isinstance(x,int):
            raise TypeError(f"'x' must be of type {type(x)}")
        if not isinstance(y,int):
            raise TypeError(f"")
        if not (0<x<100):
            raise ValueError(f"'x' must be between 0 and 100, got {x}")
        if not (0<y<100):
            raise ValueError(f"'y' must be between 0 and 100, got {y}")
        return x + y




