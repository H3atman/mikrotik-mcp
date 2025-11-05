"""PPPoE management tools for MikroTik MCP server."""

from typing import Dict, Any, List, Callable
from ..scope.pppoe import (
    mikrotik_create_pppoe_server,
    mikrotik_list_pppoe_servers,
    mikrotik_remove_pppoe_server,
    mikrotik_add_ppp_secret,
    mikrotik_list_ppp_secrets,
    mikrotik_remove_ppp_secret,
    mikrotik_list_ppp_active,
    mikrotik_disconnect_ppp_active,
    mikrotik_create_ppp_profile,
    mikrotik_list_ppp_profiles,
    mikrotik_remove_ppp_profile,
    mikrotik_create_pppoe_client,
    mikrotik_list_pppoe_clients,
    mikrotik_remove_pppoe_client
)
from mcp.types import Tool


def get_pppoe_tools() -> List[Tool]:
    """Return the list of PPPoE management tools."""
    return [
        Tool(
            name="mikrotik_create_pppoe_server",
            description="Creates a PPPoE server",
            inputSchema={
                "type": "object",
                "properties": {
                    "service_name": {"type": "string", "description": "Service name"},
                    "interface": {"type": "string", "description": "Interface to bind to"},
                    "default_profile": {"type": "string", "description": "Default PPP profile"},
                    "authentication": {"type": "string", "description": "Authentication methods (pap, chap, mschap1, mschap2)"},
                    "keepalive_timeout": {"type": "integer", "description": "Keepalive timeout in seconds"},
                    "max_mtu": {"type": "integer", "description": "Maximum MTU"},
                    "max_mru": {"type": "integer", "description": "Maximum MRU"},
                    "one_session_per_host": {"type": "boolean", "description": "Allow only one session per host"},
                    "disabled": {"type": "boolean", "description": "Disable the server"}
                },
                "required": ["service_name", "interface"]
            },
        ),
        Tool(
            name="mikrotik_list_pppoe_servers",
            description="Lists PPPoE servers",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
        Tool(
            name="mikrotik_remove_pppoe_server",
            description="Removes a PPPoE server",
            inputSchema={
                "type": "object",
                "properties": {
                    "service_name": {"type": "string", "description": "Service name"}
                },
                "required": ["service_name"]
            },
        ),
        Tool(
            name="mikrotik_add_ppp_secret",
            description="Adds a PPP secret (user credentials)",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Username"},
                    "password": {"type": "string", "description": "Password"},
                    "service": {"type": "string", "description": "Service type (any, pppoe, pptp, l2tp, sstp)"},
                    "profile": {"type": "string", "description": "PPP profile"},
                    "local_address": {"type": "string", "description": "Local IP address"},
                    "remote_address": {"type": "string", "description": "Remote IP address"},
                    "routes": {"type": "string", "description": "Static routes for this user"},
                    "limit_bytes_in": {"type": "string", "description": "Incoming traffic limit"},
                    "limit_bytes_out": {"type": "string", "description": "Outgoing traffic limit"},
                    "comment": {"type": "string", "description": "Optional comment"},
                    "disabled": {"type": "boolean", "description": "Disable the secret"}
                },
                "required": ["name", "password"]
            },
        ),
        Tool(
            name="mikrotik_list_ppp_secrets",
            description="Lists PPP secrets",
            inputSchema={
                "type": "object",
                "properties": {
                    "service_filter": {"type": "string", "description": "Filter by service type"},
                    "disabled_only": {"type": "boolean", "description": "Show only disabled secrets"}
                },
                "required": []
            },
        ),
        Tool(
            name="mikrotik_remove_ppp_secret",
            description="Removes a PPP secret",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Username"}
                },
                "required": ["name"]
            },
        ),
        Tool(
            name="mikrotik_list_ppp_active",
            description="Lists active PPP connections",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
        Tool(
            name="mikrotik_disconnect_ppp_active",
            description="Disconnects an active PPP connection",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Username to disconnect"}
                },
                "required": ["name"]
            },
        ),
        Tool(
            name="mikrotik_create_ppp_profile",
            description="Creates a PPP profile",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Profile name"},
                    "local_address": {"type": "string", "description": "Local IP address or pool"},
                    "remote_address": {"type": "string", "description": "Remote IP address or pool"},
                    "dns_server": {"type": "string", "description": "DNS server addresses"},
                    "wins_server": {"type": "string", "description": "WINS server addresses"},
                    "use_compression": {"type": "boolean", "description": "Use compression"},
                    "use_encryption": {"type": "boolean", "description": "Use encryption"},
                    "only_one": {"type": "boolean", "description": "Allow only one session per user"},
                    "rate_limit": {"type": "string", "description": "Rate limit (e.g., '10M/10M')"},
                    "comment": {"type": "string", "description": "Optional comment"}
                },
                "required": ["name"]
            },
        ),
        Tool(
            name="mikrotik_list_ppp_profiles",
            description="Lists PPP profiles",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
        Tool(
            name="mikrotik_remove_ppp_profile",
            description="Removes a PPP profile",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Profile name"}
                },
                "required": ["name"]
            },
        ),
        Tool(
            name="mikrotik_create_pppoe_client",
            description="Creates a PPPoE client interface",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Interface name"},
                    "interface": {"type": "string", "description": "Physical interface to use"},
                    "user": {"type": "string", "description": "Username"},
                    "password": {"type": "string", "description": "Password"},
                    "service_name": {"type": "string", "description": "Service name to connect to"},
                    "add_default_route": {"type": "boolean", "description": "Add default route"},
                    "use_peer_dns": {"type": "boolean", "description": "Use DNS from peer"},
                    "profile": {"type": "string", "description": "PPP profile"},
                    "comment": {"type": "string", "description": "Optional comment"},
                    "disabled": {"type": "boolean", "description": "Disable the client"}
                },
                "required": ["name", "interface", "user", "password"]
            },
        ),
        Tool(
            name="mikrotik_list_pppoe_clients",
            description="Lists PPPoE client interfaces",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
        Tool(
            name="mikrotik_remove_pppoe_client",
            description="Removes a PPPoE client interface",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Interface name"}
                },
                "required": ["name"]
            },
        ),
    ]


def get_pppoe_handlers() -> Dict[str, Callable]:
    """Return the handlers for PPPoE management tools."""
    return {
        "mikrotik_create_pppoe_server": lambda args: mikrotik_create_pppoe_server(
            args["service_name"], args["interface"], args.get("default_profile"),
            args.get("authentication"), args.get("keepalive_timeout"), args.get("max_mtu"),
            args.get("max_mru"), args.get("one_session_per_host"), args.get("disabled")
        ),
        "mikrotik_list_pppoe_servers": lambda args: mikrotik_list_pppoe_servers(),
        "mikrotik_remove_pppoe_server": lambda args: mikrotik_remove_pppoe_server(args["service_name"]),
        "mikrotik_add_ppp_secret": lambda args: mikrotik_add_ppp_secret(
            args["name"], args["password"], args.get("service"), args.get("profile"),
            args.get("local_address"), args.get("remote_address"), args.get("routes"),
            args.get("limit_bytes_in"), args.get("limit_bytes_out"), args.get("comment"),
            args.get("disabled")
        ),
        "mikrotik_list_ppp_secrets": lambda args: mikrotik_list_ppp_secrets(
            args.get("service_filter"), args.get("disabled_only")
        ),
        "mikrotik_remove_ppp_secret": lambda args: mikrotik_remove_ppp_secret(args["name"]),
        "mikrotik_list_ppp_active": lambda args: mikrotik_list_ppp_active(),
        "mikrotik_disconnect_ppp_active": lambda args: mikrotik_disconnect_ppp_active(args["name"]),
        "mikrotik_create_ppp_profile": lambda args: mikrotik_create_ppp_profile(
            args["name"], args.get("local_address"), args.get("remote_address"),
            args.get("dns_server"), args.get("wins_server"), args.get("use_compression"),
            args.get("use_encryption"), args.get("only_one"), args.get("rate_limit"),
            args.get("comment")
        ),
        "mikrotik_list_ppp_profiles": lambda args: mikrotik_list_ppp_profiles(),
        "mikrotik_remove_ppp_profile": lambda args: mikrotik_remove_ppp_profile(args["name"]),
        "mikrotik_create_pppoe_client": lambda args: mikrotik_create_pppoe_client(
            args["name"], args["interface"], args["user"], args["password"],
            args.get("service_name"), args.get("add_default_route"), args.get("use_peer_dns"),
            args.get("profile"), args.get("comment"), args.get("disabled")
        ),
        "mikrotik_list_pppoe_clients": lambda args: mikrotik_list_pppoe_clients(),
        "mikrotik_remove_pppoe_client": lambda args: mikrotik_remove_pppoe_client(args["name"]),
    }
