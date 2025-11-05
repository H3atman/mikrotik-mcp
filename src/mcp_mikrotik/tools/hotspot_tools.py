"""Hotspot management tools for MikroTik MCP server."""

from typing import Dict, Any, List, Callable
from ..scope.hotspot import (
    mikrotik_create_hotspot_server,
    mikrotik_list_hotspot_servers,
    mikrotik_list_hotspot_users,
    mikrotik_add_hotspot_user,
    mikrotik_remove_hotspot_user,
    mikrotik_list_hotspot_active,
    mikrotik_remove_hotspot_active
)
from mcp.types import Tool


def get_hotspot_tools() -> List[Tool]:
    """Return the list of hotspot management tools."""
    return [
        Tool(
            name="mikrotik_create_hotspot_server",
            description="Creates a hotspot server (captive portal)",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Hotspot server name"
                    },
                    "interface": {
                        "type": "string",
                        "description": "Interface to bind to"
                    },
                    "address_pool": {
                        "type": "string",
                        "description": "IP pool name"
                    },
                    "profile": {
                        "type": "string",
                        "description": "Hotspot profile name"
                    },
                    "disabled": {
                        "type": "boolean",
                        "description": "Disable the server"
                    }
                },
                "required": ["name", "interface", "address_pool"]
            },
        ),
        Tool(
            name="mikrotik_list_hotspot_servers",
            description="Lists hotspot servers",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
        Tool(
            name="mikrotik_list_hotspot_users",
            description="Lists hotspot users",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
        Tool(
            name="mikrotik_add_hotspot_user",
            description="Adds a hotspot user",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Username"
                    },
                    "password": {
                        "type": "string",
                        "description": "Password"
                    },
                    "profile": {
                        "type": "string",
                        "description": "User profile"
                    },
                    "limit_uptime": {
                        "type": "string",
                        "description": "Uptime limit (e.g., '1h', '1d')"
                    },
                    "limit_bytes_total": {
                        "type": "string",
                        "description": "Total bytes limit (e.g., '1G', '500M')"
                    },
                    "comment": {
                        "type": "string",
                        "description": "Optional comment"
                    },
                    "disabled": {
                        "type": "boolean",
                        "description": "Disable the user"
                    }
                },
                "required": ["name", "password"]
            },
        ),
        Tool(
            name="mikrotik_remove_hotspot_user",
            description="Removes a hotspot user",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Username"
                    }
                },
                "required": ["name"]
            },
        ),
        Tool(
            name="mikrotik_list_hotspot_active",
            description="Lists active hotspot sessions",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
        Tool(
            name="mikrotik_remove_hotspot_active",
            description="Removes an active hotspot session (disconnect user)",
            inputSchema={
                "type": "object",
                "properties": {
                    "user": {
                        "type": "string",
                        "description": "Username to disconnect"
                    }
                },
                "required": ["user"]
            },
        ),
    ]


def get_hotspot_handlers() -> Dict[str, Callable]:
    """Return the handlers for hotspot management tools."""
    return {
        "mikrotik_create_hotspot_server": lambda args: mikrotik_create_hotspot_server(
            args["name"],
            args["interface"],
            args["address_pool"],
            args.get("profile"),
            args.get("disabled")
        ),
        "mikrotik_list_hotspot_servers": lambda args: mikrotik_list_hotspot_servers(),
        "mikrotik_list_hotspot_users": lambda args: mikrotik_list_hotspot_users(),
        "mikrotik_add_hotspot_user": lambda args: mikrotik_add_hotspot_user(
            args["name"],
            args["password"],
            args.get("profile"),
            args.get("limit_uptime"),
            args.get("limit_bytes_total"),
            args.get("comment"),
            args.get("disabled")
        ),
        "mikrotik_remove_hotspot_user": lambda args: mikrotik_remove_hotspot_user(args["name"]),
        "mikrotik_list_hotspot_active": lambda args: mikrotik_list_hotspot_active(),
        "mikrotik_remove_hotspot_active": lambda args: mikrotik_remove_hotspot_active(args["user"]),
    }
