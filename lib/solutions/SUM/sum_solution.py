
class SumSolution:
    
    def compute(self, x:int, y:int)->int:
        """Adds two integers between 0 and 100 (inclusive)

        Args:
            x (int): First integer (0<=x<=100)
            y (int): Second integer (0<=y<=100)

        Raises:
            TypeError: If inputs aren't integers.
            ValueError: If inputs aren't in the valid range.

        Returns:
            int: The sum of x and y
        """
        if not isinstance(x,int):
            raise TypeError(f"'x' must be of type {type(x)}")
        if not isinstance(y,int):
            raise TypeError(f"'y' must be of type {type(y)}")
        if not (0<=x<=100):
            raise ValueError(f"'x' must be between 0 and 100, got {x}")
        if not (0<=y<=100):
            raise ValueError(f"'y' must be between 0 and 100, got {y}")
        return x + y
