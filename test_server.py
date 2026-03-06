"""Quick test script to verify all MCP server tools work correctly."""
import asyncio
from fastmcp import Client
from fastmcp.exceptions import ToolError


async def test():
    client = Client("main.py")
    async with client:
        # List all tools
        tools = await client.list_tools()
        print(f"✅ Tools found: {len(tools)}")
        for t in tools:
            print(f"   - {t.name}")

        print("\n=== Testing All Tools ===")

        r = await client.call_tool("add", {"a": 5, "b": 3})
        print(f"add(5, 3) = {r}")

        r = await client.call_tool("subtract", {"a": 10, "b": 4})
        print(f"subtract(10, 4) = {r}")

        r = await client.call_tool("multiply", {"a": 8, "b": 2})
        print(f"multiply(8, 2) = {r}")

        r = await client.call_tool("divide", {"a": 16, "b": 4})
        print(f"divide(16, 4) = {r}")

        r = await client.call_tool("modulo", {"a": 17, "b": 5})
        print(f"modulo(17, 5) = {r}")

        r = await client.call_tool("power", {"base": 2, "exponent": 10})
        print(f"power(2, 10) = {r}")

        r = await client.call_tool("square_root", {"n": 16})
        print(f"square_root(16) = {r}")

        r = await client.call_tool("absolute_value", {"n": -42})
        print(f"absolute_value(-42) = {r}")

        r = await client.call_tool("factorial", {"n": 5})
        print(f"factorial(5) = {r}")

        r = await client.call_tool("floor", {"n": 3.7})
        print(f"floor(3.7) = {r}")

        r = await client.call_tool("ceiling", {"n": 3.2})
        print(f"ceiling(3.2) = {r}")

        r = await client.call_tool("logarithm", {"n": 100, "base": 10})
        print(f"logarithm(100, 10) = {r}")

        r = await client.call_tool("sine", {"angle_degrees": 90})
        print(f"sine(90) = {r}")

        r = await client.call_tool("cosine", {"angle_degrees": 0})
        print(f"cosine(0) = {r}")

        r = await client.call_tool("tangent", {"angle_degrees": 45})
        print(f"tangent(45) = {r}")

        r = await client.call_tool("gcd", {"a": 12, "b": 8})
        print(f"gcd(12, 8) = {r}")

        r = await client.call_tool("lcm", {"a": 4, "b": 6})
        print(f"lcm(4, 6) = {r}")

        print("\n=== Error Handling ===")

        try:
            r = await client.call_tool("divide", {"a": 1, "b": 0})
        except ToolError as e:
            print(f"divide(1, 0) -> ✅ Caught: {e}")

        try:
            r = await client.call_tool("square_root", {"n": -4})
        except ToolError as e:
            print(f"square_root(-4) -> ✅ Caught: {e}")

        print("\n✅ All tests passed!")


asyncio.run(test())
