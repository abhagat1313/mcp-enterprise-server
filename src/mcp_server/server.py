from mcp.server import Server
from mcp.server.stdio import stdio_server
from resources.documents import register_document_resources
from tools.search import register_search_tool

# This is the MCP server instance
server = Server(
    name="mcp-enterprise-server",
    version="0.1.0",
)


def main():
    # stdio transport = local dev, IDEs, Claude Desktop
    register_document_resources(server)
    register_search_tool(server)
    stdio_server(server)


if __name__ == "__main__":
    main()
