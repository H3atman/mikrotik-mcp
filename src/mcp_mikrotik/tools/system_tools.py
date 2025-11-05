"""System management tools for MikroTik MCP server."""

from typing import Dict, Any, List, Callable
from ..scope.system import (
    mikrotik_get_system_resource,
    mikrotik_get_system_health,
    mikrotik_get_system_identity,
    mikrotik_set_system_identity,
    mikrotik_get_system_clock,
    mikrotik_set_system_clock,
    mikrotik_get_ntp_client,
    mikrotik_set_ntp_client,
    mikrotik_system_reboot,
    mikrotik_system_shutdown,
    mikrotik_list_packages,
    mikrotik_enable_package,
    mikrotik_disable_package,
    mikrotik_list_scheduler,
    mikrotik_add_scheduler,
    mikrotik_remove_scheduler,
    mikrotik_list_scripts,
    mikrotik_add_script,
    mikrotik_run_script,
    mikrotik_remove_script,
    mikrotik_get_system_routerboard,
    mikrotik_get_system_license,
    mikrotik_get_system_history
)
from mcp.types import Tool


def get_system_tools() -> List[Tool]:
    """Return the list of system management tools."""
    return [
        Tool(
            name="mikrotik_get_system_resource",
            description="Gets system resource information (CPU, memory, disk, uptime)",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
        Tool(
            name="mikrotik_get_system_health",
            description="Gets system health information (temperature, voltage, etc.)",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
        Tool(
            name="mikrotik_get_system_identity",
            description="Gets the system identity (router name)",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
        Tool(
            name="mikrotik_set_system_identity",
            description="Sets the system identity (router name)",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "New router name"
                    }
                },
                "required": ["name"]
            },
        ),
        Tool(
            name="mikrotik_get_system_clock",
            description="Gets system clock settings and current time",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
        Tool(
            name="mikrotik_set_system_clock",
            description="Sets system clock configuration",
            inputSchema={
                "type": "object",
                "properties": {
                    "time_zone_name": {
                        "type": "string",
                        "description": "Time zone name (e.g., 'America/New_York')"
                    },
                    "time_zone_autodetect": {
                        "type": "boolean",
                        "description": "Enable automatic time zone detection"
                    }
                },
                "required": []
            },
        ),
        Tool(
            name="mikrotik_get_ntp_client",
            description="Gets NTP client configuration",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
        Tool(
            name="mikrotik_set_ntp_client",
            description="Configures NTP client settings",
            inputSchema={
                "type": "object",
                "properties": {
                    "enabled": {
                        "type": "boolean",
                        "description": "Enable/disable NTP client"
                    },
                    "servers": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of NTP server addresses"
                    },
                    "mode": {
                        "type": "string",
                        "enum": ["unicast", "broadcast"],
                        "description": "NTP mode"
                    }
                },
                "required": []
            },
        ),
        Tool(
            name="mikrotik_system_reboot",
            description="Reboots the MikroTik device (use with caution)",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
        Tool(
            name="mikrotik_system_shutdown",
            description="Shuts down the MikroTik device (use with caution)",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
        Tool(
            name="mikrotik_list_packages",
            description="Lists installed system packages",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
        Tool(
            name="mikrotik_enable_package",
            description="Enables a system package (requires reboot)",
            inputSchema={
                "type": "object",
                "properties": {
                    "package_name": {
                        "type": "string",
                        "description": "Name of the package to enable"
                    }
                },
                "required": ["package_name"]
            },
        ),
        Tool(
            name="mikrotik_disable_package",
            description="Disables a system package (requires reboot)",
            inputSchema={
                "type": "object",
                "properties": {
                    "package_name": {
                        "type": "string",
                        "description": "Name of the package to disable"
                    }
                },
                "required": ["package_name"]
            },
        ),
        Tool(
            name="mikrotik_list_scheduler",
            description="Lists scheduled tasks",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
        Tool(
            name="mikrotik_add_scheduler",
            description="Adds a scheduled task",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Task name"
                    },
                    "on_event": {
                        "type": "string",
                        "description": "Script or command to execute"
                    },
                    "start_date": {
                        "type": "string",
                        "description": "Start date (format: mmm/dd/yyyy)"
                    },
                    "start_time": {
                        "type": "string",
                        "description": "Start time (format: HH:MM:SS)"
                    },
                    "interval": {
                        "type": "string",
                        "description": "Execution interval (e.g., '1d', '1h', '30m')"
                    },
                    "policy": {
                        "type": "string",
                        "description": "Execution policy (e.g., 'read,write,policy,test')"
                    },
                    "comment": {
                        "type": "string",
                        "description": "Optional comment"
                    },
                    "disabled": {
                        "type": "boolean",
                        "description": "Disable the task"
                    }
                },
                "required": ["name", "on_event"]
            },
        ),
        Tool(
            name="mikrotik_remove_scheduler",
            description="Removes a scheduled task",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Task name"
                    }
                },
                "required": ["name"]
            },
        ),
        Tool(
            name="mikrotik_list_scripts",
            description="Lists system scripts",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
        Tool(
            name="mikrotik_add_script",
            description="Adds a system script",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Script name"
                    },
                    "source": {
                        "type": "string",
                        "description": "Script source code"
                    },
                    "policy": {
                        "type": "string",
                        "description": "Execution policy (e.g., 'read,write,policy,test')"
                    },
                    "comment": {
                        "type": "string",
                        "description": "Optional comment"
                    },
                    "dont_require_permissions": {
                        "type": "boolean",
                        "description": "Don't require permissions"
                    }
                },
                "required": ["name", "source"]
            },
        ),
        Tool(
            name="mikrotik_run_script",
            description="Runs a system script",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Script name"
                    }
                },
                "required": ["name"]
            },
        ),
        Tool(
            name="mikrotik_remove_script",
            description="Removes a system script",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Script name"
                    }
                },
                "required": ["name"]
            },
        ),
        Tool(
            name="mikrotik_get_system_routerboard",
            description="Gets RouterBOARD hardware information",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
        Tool(
            name="mikrotik_get_system_license",
            description="Gets system license information",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
        Tool(
            name="mikrotik_get_system_history",
            description="Gets system command history",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
    ]


def get_system_handlers() -> Dict[str, Callable]:
    """Return the handlers for system management tools."""
    return {
        "mikrotik_get_system_resource": lambda args: mikrotik_get_system_resource(),
        "mikrotik_get_system_health": lambda args: mikrotik_get_system_health(),
        "mikrotik_get_system_identity": lambda args: mikrotik_get_system_identity(),
        "mikrotik_set_system_identity": lambda args: mikrotik_set_system_identity(
            args["name"]
        ),
        "mikrotik_get_system_clock": lambda args: mikrotik_get_system_clock(),
        "mikrotik_set_system_clock": lambda args: mikrotik_set_system_clock(
            args.get("time_zone_name"),
            args.get("time_zone_autodetect")
        ),
        "mikrotik_get_ntp_client": lambda args: mikrotik_get_ntp_client(),
        "mikrotik_set_ntp_client": lambda args: mikrotik_set_ntp_client(
            args.get("enabled"),
            args.get("servers"),
            args.get("mode")
        ),
        "mikrotik_system_reboot": lambda args: mikrotik_system_reboot(),
        "mikrotik_system_shutdown": lambda args: mikrotik_system_shutdown(),
        "mikrotik_list_packages": lambda args: mikrotik_list_packages(),
        "mikrotik_enable_package": lambda args: mikrotik_enable_package(
            args["package_name"]
        ),
        "mikrotik_disable_package": lambda args: mikrotik_disable_package(
            args["package_name"]
        ),
        "mikrotik_list_scheduler": lambda args: mikrotik_list_scheduler(),
        "mikrotik_add_scheduler": lambda args: mikrotik_add_scheduler(
            args["name"],
            args["on_event"],
            args.get("start_date"),
            args.get("start_time"),
            args.get("interval"),
            args.get("policy"),
            args.get("comment"),
            args.get("disabled")
        ),
        "mikrotik_remove_scheduler": lambda args: mikrotik_remove_scheduler(
            args["name"]
        ),
        "mikrotik_list_scripts": lambda args: mikrotik_list_scripts(),
        "mikrotik_add_script": lambda args: mikrotik_add_script(
            args["name"],
            args["source"],
            args.get("policy"),
            args.get("comment"),
            args.get("dont_require_permissions")
        ),
        "mikrotik_run_script": lambda args: mikrotik_run_script(
            args["name"]
        ),
        "mikrotik_remove_script": lambda args: mikrotik_remove_script(
            args["name"]
        ),
        "mikrotik_get_system_routerboard": lambda args: mikrotik_get_system_routerboard(),
        "mikrotik_get_system_license": lambda args: mikrotik_get_system_license(),
        "mikrotik_get_system_history": lambda args: mikrotik_get_system_history(),
    }
