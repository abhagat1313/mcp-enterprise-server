from mcp.server import Server
from mcp.types import Tool, TextContent


def register_search_tool(server: Server):
    @server.tool(
        name="simple_search",
        description="Search across example documents using a simple keyword match",
    )
    def simple_search(query: str) -> list[TextContent]:
        """
        This is intentionally naive.
        Real search logic will live in the domain layer later.
        """
        if "mcp" in query.lower():
            return [
                TextContent(
                    text="MCP stands for Model Context Protocol. It standardizes how models access tools and context."
                )
            ]

        return [
            TextContent(
                text="No relevant documents found."
            )
        ]
