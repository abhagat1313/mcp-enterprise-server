from mcp.server import Server
from mcp.types import Resource


def register_document_resources(server: Server):
    @server.resource(
        uri="documents://example/intro",
        name="Example Document",
        description="Introductory document explaining the system",
    )
    def get_intro_document() -> str:
        return (
            "This is an example MCP resource.\n"
            "Resources are read-only context exposed to models.\n"
            "They are safe, cacheable, and side-effect free."
        )
