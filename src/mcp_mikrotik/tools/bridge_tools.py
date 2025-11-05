"""Bridge interface management tools for MikroTik MCP server."""

from typing import Dict, Any, List, Callable
from ..scope.bridge import (
    mikrotik_create_bridge,
    mikrotik_list_bridges,
    mikrotik_remove_bridge,
    mikrotik_add_bridge_port,
    mikrotik_list_bridge_ports,
    mikrotik_remove_bridge_port,
    mikrotik_add_bridge_vlan,
    mikrotik_list_bridge_vlans,
    mikrotik_get_bridge_host
)
from mcp.types import Tool


def get_bridge_tools() -> List[Tool]:
    """Return the list of bridge management tools."""
    return [
        Tool(
            name="mikrotik_create_bridge",
            description="Creates a bridge interface on MikroTik device",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Bridge interface name"
                    },
                    "mtu": {
                        "type": "integer",
                        "description": "MTU size"
                    },
                    "arp": {
                        "type": "string",
                        "description": "ARP mode"
                    },
                    "arp_timeout": {
                        "type": "string",
                        "description": "ARP timeout"
                    },
                    "ageing_time": {
                        "type": "string",
                        "description": "MAC address ageing time"
                    },
                    "priority": {
                        "type": "integer",
                        "description": "Bridge priority for STP"
                    },
                    "protocol_mode": {
                        "type": "string",
                        "enum": ["none", "rstp", "stp", "mstp"],
                        "description": "Protocol mode"
                    },
                    "vlan_filtering": {
                        "type": "boolean",
                        "description": "Enable VLAN filtering"
                    },
                    "comment": {
                        "type": "string",
                        "description": "Optional comment"
                    },
                    "disabled": {
                        "type": "boolean",
                        "description": "Disable the bridge"
                    }
                },
                "required": ["name"]
            },
        ),
        Tool(
            name="mikrotik_list_bridges",
            description="Lists bridge interfaces on MikroTik device",
            inputSchema={
                "type": "object",
                "properties": {
                    "name_filter": {
                        "type": "string",
                        "description": "Filter by name"
                    },
                    "disabled_only": {
                        "type": "boolean",
                        "description": "Show only disabled bridges"
                    }
                },
                "required": []
            },
        ),
        Tool(
            name="mikrotik_remove_bridge",
            description="Removes a bridge interface from MikroTik device",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Bridge interface name"
                    }
                },
                "required": ["name"]
            },
        ),
        Tool(
            name="mikrotik_add_bridge_port",
            description="Adds an interface to a bridge",
            inputSchema={
                "type": "object",
                "properties": {
                    "bridge": {
                        "type": "string",
                        "description": "Bridge name"
                    },
                    "interface": {
                        "type": "string",
                        "description": "Interface to add"
                    },
                    "pvid": {
                        "type": "integer",
                        "description": "Port VLAN ID"
                    },
                    "priority": {
                        "type": "integer",
                        "description": "Port priority for STP"
                    },
                    "path_cost": {
                        "type": "integer",
                        "description": "Path cost for STP"
                    },
                    "edge": {
                        "type": "boolean",
                        "description": "Edge port (fast transition)"
                    },
                    "point_to_point": {
                        "type": "string",
                        "enum": ["auto", "yes", "no"],
                        "description": "Point-to-point mode"
                    },
                    "horizon": {
                        "type": "integer",
                        "description": "Bridge horizon"
                    },
                    "comment": {
                        "type": "string",
                        "description": "Optional comment"
                    },
                    "disabled": {
                        "type": "boolean",
                        "description": "Disable the port"
                    }
                },
                "required": ["bridge", "interface"]
            },
        ),
        Tool(
            name="mikrotik_list_bridge_ports",
            description="Lists bridge ports",
            inputSchema={
                "type": "object",
                "properties": {
                    "bridge_filter": {
                        "type": "string",
                        "description": "Filter by bridge name"
                    },
                    "interface_filter": {
                        "type": "string",
                        "description": "Filter by interface name"
                    }
                },
                "required": []
            },
        ),
        Tool(
            name="mikrotik_remove_bridge_port",
            description="Removes an interface from a bridge",
            inputSchema={
                "type": "object",
                "properties": {
                    "interface": {
                        "type": "string",
                        "description": "Interface name"
                    }
                },
                "required": ["interface"]
            },
        ),
        Tool(
            name="mikrotik_add_bridge_vlan",
            description="Adds VLAN configuration to a bridge",
            inputSchema={
                "type": "object",
                "properties": {
                    "bridge": {
                        "type": "string",
                        "description": "Bridge name"
                    },
                    "vlan_ids": {
                        "type": "string",
                        "description": "VLAN IDs (e.g., '10' or '10-20')"
                    },
                    "tagged": {
                        "type": "string",
                        "description": "Tagged interfaces (comma-separated)"
                    },
                    "untagged": {
                        "type": "string",
                        "description": "Untagged interfaces (comma-separated)"
                    },
                    "comment": {
                        "type": "string",
                        "description": "Optional comment"
                    },
                    "disabled": {
                        "type": "boolean",
                        "description": "Disable the VLAN"
                    }
                },
                "required": ["bridge", "vlan_ids"]
            },
        ),
        Tool(
            name="mikrotik_list_bridge_vlans",
            description="Lists bridge VLAN configurations",
            inputSchema={
                "type": "object",
                "properties": {
                    "bridge_filter": {
                        "type": "string",
                        "description": "Filter by bridge name"
                    }
                },
                "required": []
            },
        ),
        Tool(
            name="mikrotik_get_bridge_host",
            description="Lists MAC addresses learned by bridges",
            inputSchema={
                "type": "object",
                "properties": {
                    "bridge_filter": {
                        "type": "string",
                        "description": "Filter by bridge name"
                    }
                },
                "required": []
            },
        ),
    ]


def get_bridge_handlers() -> Dict[str, Callable]:
    """Return the handlers for bridge management tools."""
    return {
        "mikrotik_create_bridge": lambda args: mikrotik_create_bridge(
            args["name"],
            args.get("mtu"),
            args.get("arp"),
            args.get("arp_timeout"),
            args.get("ageing_time"),
            args.get("priority"),
            args.get("protocol_mode"),
            args.get("vlan_filtering"),
            args.get("comment"),
            args.get("disabled")
        ),
        "mikrotik_list_bridges": lambda args: mikrotik_list_bridges(
            args.get("name_filter"),
            args.get("disabled_only")
        ),
        "mikrotik_remove_bridge": lambda args: mikrotik_remove_bridge(
            args["name"]
        ),
        "mikrotik_add_bridge_port": lambda args: mikrotik_add_bridge_port(
            args["bridge"],
            args["interface"],
            args.get("pvid"),
            args.get("priority"),
            args.get("path_cost"),
            args.get("edge"),
            args.get("point_to_point"),
            args.get("horizon"),
            args.get("comment"),
            args.get("disabled")
        ),
        "mikrotik_list_bridge_ports": lambda args: mikrotik_list_bridge_ports(
            args.get("bridge_filter"),
            args.get("interface_filter")
        ),
        "mikrotik_remove_bridge_port": lambda args: mikrotik_remove_bridge_port(
            args["interface"]
        ),
        "mikrotik_add_bridge_vlan": lambda args: mikrotik_add_bridge_vlan(
            args["bridge"],
            args["vlan_ids"],
            args.get("tagged"),
            args.get("untagged"),
            args.get("comment"),
            args.get("disabled")
        ),
        "mikrotik_list_bridge_vlans": lambda args: mikrotik_list_bridge_vlans(
            args.get("bridge_filter")
        ),
        "mikrotik_get_bridge_host": lambda args: mikrotik_get_bridge_host(
            args.get("bridge_filter")
        ),
    }
