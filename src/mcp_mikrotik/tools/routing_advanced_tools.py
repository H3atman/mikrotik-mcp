"""Advanced routing protocol tools for MikroTik MCP server."""

from typing import Dict, Any, List, Callable
from ..scope.routing_advanced import (
    # BGP functions
    mikrotik_create_bgp_instance,
    mikrotik_list_bgp_instances,
    mikrotik_remove_bgp_instance,
    mikrotik_add_bgp_peer,
    mikrotik_list_bgp_peers,
    mikrotik_remove_bgp_peer,
    mikrotik_list_bgp_advertisements,
    # OSPF functions
    mikrotik_create_ospf_instance,
    mikrotik_list_ospf_instances,
    mikrotik_remove_ospf_instance,
    mikrotik_add_ospf_area,
    mikrotik_list_ospf_areas,
    mikrotik_add_ospf_network,
    mikrotik_list_ospf_networks,
    mikrotik_list_ospf_neighbors,
    mikrotik_add_ospf_interface,
    mikrotik_list_ospf_interfaces,
    # RIP functions
    mikrotik_create_rip_instance,
    mikrotik_list_rip_instances,
    mikrotik_remove_rip_instance,
    mikrotik_add_rip_network,
    mikrotik_list_rip_networks,
    mikrotik_add_rip_interface,
    mikrotik_list_rip_interfaces,
    mikrotik_list_rip_neighbors
)
from mcp.types import Tool


def get_routing_advanced_tools() -> List[Tool]:
    """Return the list of advanced routing protocol tools."""
    return [
        # BGP Tools
        Tool(
            name="mikrotik_create_bgp_instance",
            description="Creates a BGP instance",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Instance name"},
                    "as_number": {"type": "integer", "description": "AS number"},
                    "router_id": {"type": "string", "description": "Router ID"},
                    "redistribute_connected": {"type": "boolean", "description": "Redistribute connected routes"},
                    "redistribute_static": {"type": "boolean", "description": "Redistribute static routes"},
                    "redistribute_ospf": {"type": "boolean", "description": "Redistribute OSPF routes"},
                    "client_to_client_reflection": {"type": "boolean", "description": "Enable client-to-client reflection"},
                    "comment": {"type": "string", "description": "Optional comment"},
                    "disabled": {"type": "boolean", "description": "Disable the instance"}
                },
                "required": ["name", "as_number"]
            },
        ),
        Tool(
            name="mikrotik_list_bgp_instances",
            description="Lists BGP instances",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
        Tool(
            name="mikrotik_remove_bgp_instance",
            description="Removes a BGP instance",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Instance name"}
                },
                "required": ["name"]
            },
        ),
        Tool(
            name="mikrotik_add_bgp_peer",
            description="Adds a BGP peer",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Peer name"},
                    "instance": {"type": "string", "description": "BGP instance name"},
                    "remote_address": {"type": "string", "description": "Remote peer IP address"},
                    "remote_as": {"type": "integer", "description": "Remote AS number"},
                    "ttl": {"type": "integer", "description": "TTL for BGP packets"},
                    "multihop": {"type": "boolean", "description": "Enable multihop"},
                    "route_reflect": {"type": "boolean", "description": "Route reflector client"},
                    "hold_time": {"type": "string", "description": "Hold time"},
                    "tcp_md5_key": {"type": "string", "description": "TCP MD5 authentication key"},
                    "update_source": {"type": "string", "description": "Update source address"},
                    "comment": {"type": "string", "description": "Optional comment"},
                    "disabled": {"type": "boolean", "description": "Disable the peer"}
                },
                "required": ["name", "instance", "remote_address", "remote_as"]
            },
        ),
        Tool(
            name="mikrotik_list_bgp_peers",
            description="Lists BGP peers",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
        Tool(
            name="mikrotik_remove_bgp_peer",
            description="Removes a BGP peer",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Peer name"}
                },
                "required": ["name"]
            },
        ),
        Tool(
            name="mikrotik_list_bgp_advertisements",
            description="Lists BGP advertisements",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
        # OSPF Tools
        Tool(
            name="mikrotik_create_ospf_instance",
            description="Creates an OSPF instance",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Instance name"},
                    "router_id": {"type": "string", "description": "Router ID"},
                    "redistribute_connected": {"type": "boolean", "description": "Redistribute connected routes"},
                    "redistribute_static": {"type": "boolean", "description": "Redistribute static routes"},
                    "redistribute_bgp": {"type": "boolean", "description": "Redistribute BGP routes"},
                    "comment": {"type": "string", "description": "Optional comment"},
                    "disabled": {"type": "boolean", "description": "Disable the instance"}
                },
                "required": ["name"]
            },
        ),
        Tool(
            name="mikrotik_list_ospf_instances",
            description="Lists OSPF instances",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
        Tool(
            name="mikrotik_remove_ospf_instance",
            description="Removes an OSPF instance",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Instance name"}
                },
                "required": ["name"]
            },
        ),
        Tool(
            name="mikrotik_add_ospf_area",
            description="Adds an OSPF area",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Area name"},
                    "area_id": {"type": "string", "description": "Area ID (e.g., '0.0.0.0' for backbone)"},
                    "instance": {"type": "string", "description": "OSPF instance name"},
                    "type": {"type": "string", "enum": ["default", "stub", "nssa"], "description": "Area type"},
                    "comment": {"type": "string", "description": "Optional comment"},
                    "disabled": {"type": "boolean", "description": "Disable the area"}
                },
                "required": ["name", "area_id"]
            },
        ),
        Tool(
            name="mikrotik_list_ospf_areas",
            description="Lists OSPF areas",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
        Tool(
            name="mikrotik_add_ospf_network",
            description="Adds an OSPF network",
            inputSchema={
                "type": "object",
                "properties": {
                    "network": {"type": "string", "description": "Network address (e.g., '192.168.1.0/24')"},
                    "area": {"type": "string", "description": "Area name"},
                    "comment": {"type": "string", "description": "Optional comment"},
                    "disabled": {"type": "boolean", "description": "Disable the network"}
                },
                "required": ["network", "area"]
            },
        ),
        Tool(
            name="mikrotik_list_ospf_networks",
            description="Lists OSPF networks",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
        Tool(
            name="mikrotik_list_ospf_neighbors",
            description="Lists OSPF neighbors",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
        Tool(
            name="mikrotik_add_ospf_interface",
            description="Adds an OSPF interface configuration",
            inputSchema={
                "type": "object",
                "properties": {
                    "interface": {"type": "string", "description": "Interface name"},
                    "network_type": {"type": "string", "description": "Network type (broadcast, point-to-point, nbma, etc.)"},
                    "priority": {"type": "integer", "description": "Router priority"},
                    "cost": {"type": "integer", "description": "Interface cost"},
                    "authentication": {"type": "string", "enum": ["none", "simple", "md5"], "description": "Authentication type"},
                    "authentication_key": {"type": "string", "description": "Authentication key"},
                    "comment": {"type": "string", "description": "Optional comment"},
                    "disabled": {"type": "boolean", "description": "Disable the interface"}
                },
                "required": ["interface"]
            },
        ),
        Tool(
            name="mikrotik_list_ospf_interfaces",
            description="Lists OSPF interfaces",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
        # RIP Tools
        Tool(
            name="mikrotik_create_rip_instance",
            description="Creates a RIP instance",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Instance name"},
                    "redistribute_connected": {"type": "boolean", "description": "Redistribute connected routes"},
                    "redistribute_static": {"type": "boolean", "description": "Redistribute static routes"},
                    "redistribute_ospf": {"type": "boolean", "description": "Redistribute OSPF routes"},
                    "redistribute_bgp": {"type": "boolean", "description": "Redistribute BGP routes"},
                    "comment": {"type": "string", "description": "Optional comment"},
                    "disabled": {"type": "boolean", "description": "Disable the instance"}
                },
                "required": ["name"]
            },
        ),
        Tool(
            name="mikrotik_list_rip_instances",
            description="Lists RIP instances",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
        Tool(
            name="mikrotik_remove_rip_instance",
            description="Removes a RIP instance",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Instance name"}
                },
                "required": ["name"]
            },
        ),
        Tool(
            name="mikrotik_add_rip_network",
            description="Adds a RIP network",
            inputSchema={
                "type": "object",
                "properties": {
                    "network": {"type": "string", "description": "Network address (e.g., '192.168.1.0/24')"},
                    "instance": {"type": "string", "description": "RIP instance name"},
                    "comment": {"type": "string", "description": "Optional comment"},
                    "disabled": {"type": "boolean", "description": "Disable the network"}
                },
                "required": ["network"]
            },
        ),
        Tool(
            name="mikrotik_list_rip_networks",
            description="Lists RIP networks",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
        Tool(
            name="mikrotik_add_rip_interface",
            description="Adds a RIP interface configuration",
            inputSchema={
                "type": "object",
                "properties": {
                    "interface": {"type": "string", "description": "Interface name"},
                    "receive": {"type": "string", "enum": ["no", "v1", "v2", "v1-v2"], "description": "Receive mode"},
                    "send": {"type": "string", "enum": ["no", "v1", "v2", "v1-v2"], "description": "Send mode"},
                    "authentication": {"type": "string", "enum": ["none", "simple", "md5"], "description": "Authentication type"},
                    "authentication_key": {"type": "string", "description": "Authentication key"},
                    "comment": {"type": "string", "description": "Optional comment"},
                    "disabled": {"type": "boolean", "description": "Disable the interface"}
                },
                "required": ["interface"]
            },
        ),
        Tool(
            name="mikrotik_list_rip_interfaces",
            description="Lists RIP interfaces",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
        Tool(
            name="mikrotik_list_rip_neighbors",
            description="Lists RIP neighbors",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
    ]


def get_routing_advanced_handlers() -> Dict[str, Callable]:
    """Return the handlers for advanced routing protocol tools."""
    return {
        # BGP handlers
        "mikrotik_create_bgp_instance": lambda args: mikrotik_create_bgp_instance(
            args["name"], args["as_number"], args.get("router_id"),
            args.get("redistribute_connected"), args.get("redistribute_static"),
            args.get("redistribute_ospf"), args.get("client_to_client_reflection"),
            args.get("comment"), args.get("disabled")
        ),
        "mikrotik_list_bgp_instances": lambda args: mikrotik_list_bgp_instances(),
        "mikrotik_remove_bgp_instance": lambda args: mikrotik_remove_bgp_instance(args["name"]),
        "mikrotik_add_bgp_peer": lambda args: mikrotik_add_bgp_peer(
            args["name"], args["instance"], args["remote_address"], args["remote_as"],
            args.get("ttl"), args.get("multihop"), args.get("route_reflect"),
            args.get("hold_time"), args.get("tcp_md5_key"), args.get("update_source"),
            args.get("comment"), args.get("disabled")
        ),
        "mikrotik_list_bgp_peers": lambda args: mikrotik_list_bgp_peers(),
        "mikrotik_remove_bgp_peer": lambda args: mikrotik_remove_bgp_peer(args["name"]),
        "mikrotik_list_bgp_advertisements": lambda args: mikrotik_list_bgp_advertisements(),
        
        # OSPF handlers
        "mikrotik_create_ospf_instance": lambda args: mikrotik_create_ospf_instance(
            args["name"], args.get("router_id"), args.get("redistribute_connected"),
            args.get("redistribute_static"), args.get("redistribute_bgp"),
            args.get("comment"), args.get("disabled")
        ),
        "mikrotik_list_ospf_instances": lambda args: mikrotik_list_ospf_instances(),
        "mikrotik_remove_ospf_instance": lambda args: mikrotik_remove_ospf_instance(args["name"]),
        "mikrotik_add_ospf_area": lambda args: mikrotik_add_ospf_area(
            args["name"], args["area_id"], args.get("instance"), args.get("type"),
            args.get("comment"), args.get("disabled")
        ),
        "mikrotik_list_ospf_areas": lambda args: mikrotik_list_ospf_areas(),
        "mikrotik_add_ospf_network": lambda args: mikrotik_add_ospf_network(
            args["network"], args["area"], args.get("comment"), args.get("disabled")
        ),
        "mikrotik_list_ospf_networks": lambda args: mikrotik_list_ospf_networks(),
        "mikrotik_list_ospf_neighbors": lambda args: mikrotik_list_ospf_neighbors(),
        "mikrotik_add_ospf_interface": lambda args: mikrotik_add_ospf_interface(
            args["interface"], args.get("network_type"), args.get("priority"),
            args.get("cost"), args.get("authentication"), args.get("authentication_key"),
            args.get("comment"), args.get("disabled")
        ),
        "mikrotik_list_ospf_interfaces": lambda args: mikrotik_list_ospf_interfaces(),
        
        # RIP handlers
        "mikrotik_create_rip_instance": lambda args: mikrotik_create_rip_instance(
            args["name"], args.get("redistribute_connected"), args.get("redistribute_static"),
            args.get("redistribute_ospf"), args.get("redistribute_bgp"),
            args.get("comment"), args.get("disabled")
        ),
        "mikrotik_list_rip_instances": lambda args: mikrotik_list_rip_instances(),
        "mikrotik_remove_rip_instance": lambda args: mikrotik_remove_rip_instance(args["name"]),
        "mikrotik_add_rip_network": lambda args: mikrotik_add_rip_network(
            args["network"], args.get("instance"), args.get("comment"), args.get("disabled")
        ),
        "mikrotik_list_rip_networks": lambda args: mikrotik_list_rip_networks(),
        "mikrotik_add_rip_interface": lambda args: mikrotik_add_rip_interface(
            args["interface"], args.get("receive"), args.get("send"),
            args.get("authentication"), args.get("authentication_key"),
            args.get("comment"), args.get("disabled")
        ),
        "mikrotik_list_rip_interfaces": lambda args: mikrotik_list_rip_interfaces(),
        "mikrotik_list_rip_neighbors": lambda args: mikrotik_list_rip_neighbors(),
    }
