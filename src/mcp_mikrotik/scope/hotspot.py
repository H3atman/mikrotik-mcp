"""Hotspot (captive portal) management for MikroTik RouterOS."""

from typing import Optional
from ..connector import execute_mikrotik_command
from ..logger import app_logger


def mikrotik_create_hotspot_server(
    name: str,
    interface: str,
    address_pool: str,
    profile: Optional[str] = None,
    disabled: Optional[bool] = None
) -> str:
    """
    Creates a hotspot server.
    
    Args:
        name: Hotspot server name
        interface: Interface to bind to
        address_pool: IP pool name
        profile: Hotspot profile name
        disabled: Disable the server
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Creating hotspot server: name={name}, interface={interface}")
    
    cmd = f'/ip hotspot add name="{name}" interface="{interface}" address-pool="{address_pool}"'
    
    if profile:
        cmd += f' profile="{profile}"'
    if disabled is not None:
        cmd += f" disabled={'yes' if disabled else 'no'}"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to create hotspot server: {result}"
    
    return f"Hotspot server '{name}' created successfully"


def mikrotik_list_hotspot_servers() -> str:
    """
    Lists hotspot servers.
    
    Returns:
        List of hotspot servers or error message
    """
    app_logger.info("Listing hotspot servers")
    
    cmd = "/ip hotspot print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list hotspot servers: {result}"
    
    return f"Hotspot Servers:\n\n{result}"


def mikrotik_list_hotspot_users() -> str:
    """
    Lists hotspot users.
    
    Returns:
        List of hotspot users or error message
    """
    app_logger.info("Listing hotspot users")
    
    cmd = "/ip hotspot user print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list hotspot users: {result}"
    
    return f"Hotspot Users:\n\n{result}"


def mikrotik_add_hotspot_user(
    name: str,
    password: str,
    profile: Optional[str] = None,
    limit_uptime: Optional[str] = None,
    limit_bytes_total: Optional[str] = None,
    comment: Optional[str] = None,
    disabled: Optional[bool] = None
) -> str:
    """
    Adds a hotspot user.
    
    Args:
        name: Username
        password: Password
        profile: User profile
        limit_uptime: Uptime limit
        limit_bytes_total: Total bytes limit
        comment: Optional comment
        disabled: Disable the user
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Adding hotspot user: name={name}")
    
    cmd = f'/ip hotspot user add name="{name}" password="{password}"'
    
    if profile:
        cmd += f' profile="{profile}"'
    if limit_uptime:
        cmd += f' limit-uptime={limit_uptime}'
    if limit_bytes_total:
        cmd += f' limit-bytes-total={limit_bytes_total}'
    if comment:
        cmd += f' comment="{comment}"'
    if disabled is not None:
        cmd += f" disabled={'yes' if disabled else 'no'}"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to add hotspot user: {result}"
    
    return f"Hotspot user '{name}' added successfully"


def mikrotik_remove_hotspot_user(name: str) -> str:
    """
    Removes a hotspot user.
    
    Args:
        name: Username
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Removing hotspot user: {name}")
    
    cmd = f'/ip hotspot user remove [find name="{name}"]'
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to remove hotspot user: {result}"
    
    return f"Hotspot user '{name}' removed successfully"


def mikrotik_list_hotspot_active() -> str:
    """
    Lists active hotspot sessions.
    
    Returns:
        List of active sessions or error message
    """
    app_logger.info("Listing active hotspot sessions")
    
    cmd = "/ip hotspot active print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list active sessions: {result}"
    
    return f"Active Hotspot Sessions:\n\n{result}"


def mikrotik_remove_hotspot_active(user: str) -> str:
    """
    Removes an active hotspot session.
    
    Args:
        user: Username to disconnect
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Removing active hotspot session: {user}")
    
    cmd = f'/ip hotspot active remove [find user="{user}"]'
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to remove active session: {result}"
    
    return f"Active session for user '{user}' removed successfully"
