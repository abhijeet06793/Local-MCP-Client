# Local MCP Client

A local implementation of a **Model Context Protocol (MCP)** server and client using [FastMCP](https://gofastmcp.com). This project exposes a **Maths MCP Server** with 17 mathematical tools and connects an LLM agent to it via `langchain-mcp-adapters`.

---

## 📁 Project Structure

```
Local_MCP_client/
├── main.py          # FastMCP server — exposes 17 async math tools
├── client1.py       # LangChain agent client that connects to the MCP server
├── test_server.py   # Test script to verify all MCP tools work correctly
├── pyproject.toml   # Project dependencies
├── .env             # API keys (not committed)
└── README.md
```

---

## 🧮 Maths MCP Server (`main.py`)

Built with **FastMCP 3.1.0**, the server exposes 17 async mathematical tools over `stdio` transport.

### Available Tools

| Tool | Description | Input | Output |
|---|---|---|---|
| `add(a, b)` | Add two numbers | `float, float` | `float` |
| `subtract(a, b)` | Subtract b from a | `float, float` | `float` |
| `multiply(a, b)` | Multiply two numbers | `float, float` | `float` |
| `divide(a, b)` | Divide a by b | `float, float` | `float` |
| `modulo(a, b)` | Remainder of a ÷ b | `float, float` | `float` |
| `power(base, exponent)` | Raise base to exponent | `float, float` | `float` |
| `square_root(n)` | Square root of n | `float` | `float` |
| `absolute_value(n)` | Absolute value of n | `float` | `float` |
| `factorial(n)` | Factorial of n | `int` | `int` |
| `floor(n)` | Floor of n | `float` | `int` |
| `ceiling(n)` | Ceiling of n | `float` | `int` |
| `logarithm(n, base)` | Log of n (default: natural log) | `float, float` | `float` |
| `sine(angle_degrees)` | Sine of angle in degrees | `float` | `float` |
| `cosine(angle_degrees)` | Cosine of angle in degrees | `float` | `float` |
| `tangent(angle_degrees)` | Tangent of angle in degrees | `float` | `float` |
| `gcd(a, b)` | Greatest common divisor | `int, int` | `int` |
| `lcm(a, b)` | Least common multiple | `int, int` | `int` |

All tools include **input validation** and raise descriptive errors for invalid inputs (e.g. division by zero, negative square root).

### Running the Server

```bash
uv run fastmcp run main.py
```

### Inspecting the Server (interactive UI)

```bash
uv run fastmcp dev main.py
```

---

## 🤖 LangChain Agent Client (`client1.py`)

Connects to the MCP server using `langchain-mcp-adapters` and uses a LangChain agent to perform multi-step calculations using the MCP tools.

### How It Works

```
client1.py
  └─► MultiServerMCPClient connects to MCP server via stdio
        └─► Spawns main.py as a subprocess automatically
              └─► Fetches 17 tools as LangChain tool objects
                    └─► LLM agent uses tools step-by-step to answer the prompt
```

### Configuration

The client uses `stdio` transport — **no need to start the server manually**. The client spawns it automatically.

```python
SERVERS = {
    "maths": {
        "transport": "stdio",
        "command": "C:\\Python314\\Scripts\\uv.exe",
        "args": ["run", "fastmcp", "run", "C:\\EGA\\code\\Local_MCP_client\\main.py"]
    }
}
```

---

## ⚙️ Setup & Installation

### Prerequisites

- Python 3.14+
- [uv](https://docs.astral.sh/uv/) package manager

### Install Dependencies

```bash
uv sync
```

Or with pip:

```bash
pip install fastmcp langchain langchain-mcp-adapters langchain-openai euriai python-dotenv
```

### Environment Variables

Create a `.env` file in the project root:

```env
key=your_euri_api_key_here
GOOGLE_API_KEY=your_google_api_key_here   # Required only for Gemini models
```

- Get your **Euri API key** from [euron.one](https://euron.one)
- Get your **Google API key** from [Google AI Studio](https://aistudio.google.com/apikey)

---

## 🧪 Testing the MCP Server

Run the test script to verify all 17 tools work correctly:

```bash
uv run python test_server.py
```

Expected output:
```
✅ Tools found: 17
   - add
   - subtract
   ...

=== Testing All Tools ===
add(5, 3) = 8.0
subtract(10, 4) = 6.0
...

=== Error Handling ===
divide(1, 0) -> ✅ Caught: Division by zero is not allowed.
square_root(-4) -> ✅ Caught: Cannot compute square root of a negative number.

✅ All tests passed!
```

---

## 🔧 Dependencies

| Package | Version | Purpose |
|---|---|---|
| `fastmcp` | ≥3.1.0 | MCP server framework |
| `langchain` | ≥1.2.10 | Agent framework |
| `langchain-mcp-adapters` | ≥0.2.1 | Bridge between LangChain and MCP |
| `langchain-openai` | ≥1.1.10 | OpenAI-compatible LLM client |
| `langchain-google-genai` | latest | Google Gemini LLM client |
| `euriai` | ≥1.0.32 | Euri AI API client |
| `python-dotenv` | ≥1.2.2 | Environment variable management |

---

## ⚠️ Known Limitations

- The **Euri API proxy** does not support multi-turn tool calling message format (strips `tool_calls` from assistant messages). This causes `400` errors when using LangChain agents with `create_agent` or `create_react_agent`.
- The `euriai` LangChain wrapper (`create_chat_model`) does **not** support tool/function calling — tools are silently dropped.
- For full tool calling support, use **Google Gemini** via `langchain-google-genai` (direct API, not via Euri proxy).

---

## 📄 License

MIT
