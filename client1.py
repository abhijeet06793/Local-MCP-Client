import os   
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
import warnings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
warnings.filterwarnings("ignore", category=UserWarning, module="pydantic")
from dotenv import load_dotenv
from euriai.langchain import EuriaiChatModel

load_dotenv()
key = os.getenv("key")

SERVERS= {
    "maths":{
        "transport":"stdio",
        "command":"C:\\Python314\\Scripts\\uv.exe",
        "args":["run", "fastmcp","run", "C:\\EGA\\code\\Local_MCP_client\\main.py"]
    }
}

chat_model = EuriaiChatModel(
    api_key=key,
    model="llama-3.3-70b-versatile"
)

response = chat_model.invoke("What is artificial intelligence?")
print(response)


async def main():
    client = MultiServerMCPClient(SERVERS)
    all_tools = await client.get_tools()
    print(f"Loaded {len(all_tools)} tools: {[t.name for t in all_tools]}\n")
    llm = EuriaiChatModel(api_key=key, model="llama-3.3-70b-versatile")
    agent = create_agent(llm, all_tools)
    prompt = "Calculate the result of (5 + 3) * 2 and then find the square root of that result using the tools provided by the MCP Server only. Dont use the llm for calculations, only use the tools provided by the MCP Server. Provide the final answer as well."
    response = await agent.ainvoke({"messages": [{"role": "user", "content": prompt}]})
    print("Agent response:", response)
    
    # Print the final response
    for msg in response["messages"]:
        print(f"[{msg.type}]: {msg.content}")

if __name__ == "__main__":
    asyncio.run(main())