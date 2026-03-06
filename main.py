from fastmcp import FastMCP
import math

mcp = FastMCP(
    name="maths",
    instructions="A server that provides mathematical operations and functions.",
)


@mcp.tool()
async def add(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b


@mcp.tool()
async def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


@mcp.tool()
async def multiply(a: float, b: float) -> float:
    """Multiply two numbers together."""
    return a * b


@mcp.tool()
async def divide(a: float, b: float) -> float:
    """Divide a by b. Raises an error if b is zero."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b


@mcp.tool()
async def modulo(a: float, b: float) -> float:
    """Return the remainder of a divided by b."""
    if b == 0:
        raise ValueError("Modulo by zero is not allowed.")
    return a % b


@mcp.tool()
async def power(base: float, exponent: float) -> float:
    """Raise base to the power of exponent."""
    return base ** exponent


@mcp.tool()
async def square_root(n: float) -> float:
    """Return the square root of n. Raises an error if n is negative."""
    if n < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return math.sqrt(n)


@mcp.tool()
async def absolute_value(n: float) -> float:
    """Return the absolute value of n."""
    return abs(n)


@mcp.tool()
async def factorial(n: int) -> int:
    """Return the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(n)


@mcp.tool()
async def floor(n: float) -> int:
    """Return the floor of n (largest integer <= n)."""
    return math.floor(n)


@mcp.tool()
async def ceiling(n: float) -> int:
    """Return the ceiling of n (smallest integer >= n)."""
    return math.ceil(n)


@mcp.tool()
async def logarithm(n: float, base: float = math.e) -> float:
    """Return the logarithm of n with the given base (default: natural log).
    
    Args:
        n: The number to compute the logarithm of (must be positive).
        base: The logarithm base (default is Euler's number e for natural log).
    """
    if n <= 0:
        raise ValueError("Logarithm is only defined for positive numbers.")
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1.")
    return math.log(n, base)


@mcp.tool()
async def sine(angle_degrees: float) -> float:
    """Return the sine of an angle given in degrees."""
    return math.sin(math.radians(angle_degrees))


@mcp.tool()
async def cosine(angle_degrees: float) -> float:
    """Return the cosine of an angle given in degrees."""
    return math.cos(math.radians(angle_degrees))


@mcp.tool()
async def tangent(angle_degrees: float) -> float:
    """Return the tangent of an angle given in degrees."""
    return math.tan(math.radians(angle_degrees))


@mcp.tool()
async def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor (GCD) of two integers."""
    return math.gcd(a, b)


@mcp.tool()
async def lcm(a: int, b: int) -> int:
    """Return the least common multiple (LCM) of two integers."""
    return math.lcm(a, b)


if __name__ == "__main__":
    mcp.run()

