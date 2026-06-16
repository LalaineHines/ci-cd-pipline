"""
Calculator Module

Used to demonstrate:
- Unit testing
- Ci/CD automation
- Secure coding practices
"""


class Calculator:

    @staticmethod
    def add(a, b):
        """Add two numbers."""
        return a + b
    
    @staticmethod
    def subtract(a, b):
        """Subtract two numbers."""
        return a - b
    
    @staticmethod
    def multiply(a, b):
        """Multiply two numbers."""
        return a * b
    
    @staticmethod
    def divide(a, b):
        """Divide two numbers."""

        if b == 0:
            raise ValueError("Cannot divide by zero")
        
        return a / b