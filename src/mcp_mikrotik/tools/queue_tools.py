"""Queue management tools for MikroTik MCP server."""

from typing import Dict, Any, List, Callable
from ..scope.queue import (
    mikrotik_create_simple_queue,
    mikrotik_list_simple_queues,
    mikrotik_remove_simple_queue,
    mikrotik_enable_simple_queue,
    mikrotik_disable_simple_queue,
    mikrotik_create_queue_tree,
    mikrotik_list_queue_tree,
    mikrotik_remove_queue_tree,
    mikrotik_list_queue_types,
    mikrotik_create_queue_type,
    mikrotik_remove_queue_type,
    mikrotik_reset_queue_counters
)
from mcp.types import Tool


def get_queue_tools() -> List[Tool]:
    """Return the list of queue management tools."""
    return [
        Tool(
            name="mikrotik_create_simple_queue",
            description="Creates a simple queue for traffic shaping",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Queue name"},
                    "target": {"type": "string", "description": "Target address/network (e.g., '192.168.1.100/32')"},
                    "max_limit": {"type": "string", "description": "Maximum bandwidth limit (upload/download, e.g., '10M/10M')"},
                    "burst_limit": {"type": "string", "description": "Burst bandwidth limit"},
                    "burst_threshold": {"type": "string", "description": "Burst threshold"},
                    "burst_time": {"type": "string", "description": "Burst time"},
                    "limit_at": {"type": "string", "description": "Guaranteed bandwidth"},
                    "priority": {"type": "integer", "description": "Queue priority (1-8)"},
                    "queue_type": {"type": "string", "description": "Queue type (default, pcq, etc.)"},
                    "parent": {"type": "string", "description": "Parent queue name"},
                    "comment": {"type": "string", "description": "Optional comment"},
                    "disabled": {"type": "boolean", "description": "Disable the queue"}
                },
                "required": ["name", "target", "max_limit"]
            },
        ),
        Tool(
            name="mikrotik_list_simple_queues",
            description="Lists simple queues",
            inputSchema={
                "type": "object",
                "properties": {
                    "name_filter": {"type": "string"},
                    "target_filter": {"type": "string"},
                    "disabled_only": {"type": "boolean"}
                },
                "required": []
            },
        ),
        Tool(
            name="mikrotik_remove_simple_queue",
            description="Removes a simple queue",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Queue name"}
                },
                "required": ["name"]
            },
        ),
        Tool(
            name="mikrotik_enable_simple_queue",
            description="Enables a simple queue",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Queue name"}
                },
                "required": ["name"]
            },
        ),
        Tool(
            name="mikrotik_disable_simple_queue",
            description="Disables a simple queue",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Queue name"}
                },
                "required": ["name"]
            },
        ),
        Tool(
            name="mikrotik_create_queue_tree",
            description="Creates a queue tree entry for advanced QoS",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Queue name"},
                    "parent": {"type": "string", "description": "Parent (interface or queue)"},
                    "max_limit": {"type": "string", "description": "Maximum bandwidth limit"},
                    "burst_limit": {"type": "string"},
                    "burst_threshold": {"type": "string"},
                    "burst_time": {"type": "string"},
                    "limit_at": {"type": "string", "description": "Guaranteed bandwidth"},
                    "priority": {"type": "integer"},
                    "queue_type": {"type": "string"},
                    "packet_mark": {"type": "string", "description": "Packet mark to match"},
                    "comment": {"type": "string"},
                    "disabled": {"type": "boolean"}
                },
                "required": ["name", "parent", "max_limit"]
            },
        ),
        Tool(
            name="mikrotik_list_queue_tree",
            description="Lists queue tree entries",
            inputSchema={
                "type": "object",
                "properties": {
                    "name_filter": {"type": "string"},
                    "parent_filter": {"type": "string"},
                    "disabled_only": {"type": "boolean"}
                },
                "required": []
            },
        ),
        Tool(
            name="mikrotik_remove_queue_tree",
            description="Removes a queue tree entry",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string"}
                },
                "required": ["name"]
            },
        ),
        Tool(
            name="mikrotik_list_queue_types",
            description="Lists available queue types",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
        Tool(
            name="mikrotik_create_queue_type",
            description="Creates a custom queue type (PCQ)",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "kind": {"type": "string", "description": "Queue kind (pcq, pfifo, bfifo, etc.)"},
                    "pcq_rate": {"type": "string"},
                    "pcq_limit": {"type": "string"},
                    "pcq_classifier": {"type": "string"},
                    "pcq_total_limit": {"type": "string"}
                },
                "required": ["name", "kind"]
            },
        ),
        Tool(
            name="mikrotik_remove_queue_type",
            description="Removes a custom queue type",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string"}
                },
                "required": ["name"]
            },
        ),
        Tool(
            name="mikrotik_reset_queue_counters",
            description="Resets queue counters",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
    ]


def get_queue_handlers() -> Dict[str, Callable]:
    """Return the handlers for queue management tools."""
    return {
        "mikrotik_create_simple_queue": lambda args: mikrotik_create_simple_queue(
            args["name"], args["target"], args["max_limit"],
            args.get("burst_limit"), args.get("burst_threshold"), args.get("burst_time"),
            args.get("limit_at"), args.get("priority"), args.get("queue_type"),
            args.get("parent"), args.get("comment"), args.get("disabled")
        ),
        "mikrotik_list_simple_queues": lambda args: mikrotik_list_simple_queues(
            args.get("name_filter"), args.get("target_filter"), args.get("disabled_only")
        ),
        "mikrotik_remove_simple_queue": lambda args: mikrotik_remove_simple_queue(args["name"]),
        "mikrotik_enable_simple_queue": lambda args: mikrotik_enable_simple_queue(args["name"]),
        "mikrotik_disable_simple_queue": lambda args: mikrotik_disable_simple_queue(args["name"]),
        "mikrotik_create_queue_tree": lambda args: mikrotik_create_queue_tree(
            args["name"], args["parent"], args["max_limit"],
            args.get("burst_limit"), args.get("burst_threshold"), args.get("burst_time"),
            args.get("limit_at"), args.get("priority"), args.get("queue_type"),
            args.get("packet_mark"), args.get("comment"), args.get("disabled")
        ),
        "mikrotik_list_queue_tree": lambda args: mikrotik_list_queue_tree(
            args.get("name_filter"), args.get("parent_filter"), args.get("disabled_only")
        ),
        "mikrotik_remove_queue_tree": lambda args: mikrotik_remove_queue_tree(args["name"]),
        "mikrotik_list_queue_types": lambda args: mikrotik_list_queue_types(),
        "mikrotik_create_queue_type": lambda args: mikrotik_create_queue_type(
            args["name"], args["kind"], args.get("pcq_rate"), args.get("pcq_limit"),
            args.get("pcq_classifier"), args.get("pcq_total_limit")
        ),
        "mikrotik_remove_queue_type": lambda args: mikrotik_remove_queue_type(args["name"]),
        "mikrotik_reset_queue_counters": lambda args: mikrotik_reset_queue_counters(),
    }
