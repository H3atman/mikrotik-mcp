"""IPv6 management for MikroTik RouterOS."""

from typing import Optional
from ..connector import execute_mikrotik_command
from ..logger import app_logger


def mikrotik_add_ipv6_address(
    address: str,
    interface: str,
    advertise: Optional[bool] = None,
    eui_64: Optional[bool] = None,
    no_dad: Optional[bool] = None,
    comment: Optional[str] = None,
    disabled: Optional[bool] = None
) -> str:
    """
    Adds an IPv6 address to an interface.
    
    Args:
        address: IPv6 address with prefix (e.g., "2001:db8::1/64")
        interface: Interface name
        advertise: Advertise this prefix
        eui_64: Generate EUI-64 address
        no_dad: Disable Duplicate Address Detection
        comment: Optional comment
        disabled: Disable the address
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Adding IPv6 address: address={address}, interface={interface}")
    
    cmd = f'/ipv6 address add address="{address}" interface="{interface}"'
    
    if advertise is not None:
        cmd += f" advertise={'yes' if advertise else 'no'}"
    if eui_64 is not None:
        cmd += f" eui-64={'yes' if eui_64 else 'no'}"
    if no_dad is not None:
        cmd += f" no-dad={'yes' if no_dad else 'no'}"
    if comment:
        cmd += f' comment="{comment}"'
    if disabled is not None:
        cmd += f" disabled={'yes' if disabled else 'no'}"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to add IPv6 address: {result}"
    
    return f"IPv6 address {address} added to {interface} successfully"


def mikrotik_list_ipv6_addresses(
    interface_filter: Optional[str] = None,
    disabled_only: Optional[bool] = None
) -> str:
    """
    Lists IPv6 addresses.
    
    Args:
        interface_filter: Filter by interface
        disabled_only: Show only disabled addresses
    
    Returns:
        List of IPv6 addresses or error message
    """
    app_logger.info("Listing IPv6 addresses")
    
    cmd = "/ipv6 address print"
    
    if interface_filter:
        cmd += f' where interface~"{interface_filter}"'
    elif disabled_only:
        cmd += " where disabled=yes"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list IPv6 addresses: {result}"
    
    return f"IPv6 Addresses:\n\n{result}"


def mikrotik_remove_ipv6_address(address_id: str) -> str:
    """
    Removes an IPv6 address.
    
    Args:
        address_id: Address ID
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Removing IPv6 address: {address_id}")
    
    cmd = f"/ipv6 address remove {address_id}"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to remove IPv6 address: {result}"
    
    return f"IPv6 address {address_id} removed successfully"


def mikrotik_add_ipv6_route(
    dst_address: str,
    gateway: str,
    distance: Optional[int] = None,
    comment: Optional[str] = None,
    disabled: Optional[bool] = None
) -> str:
    """
    Adds an IPv6 route.
    
    Args:
        dst_address: Destination IPv6 address/prefix
        gateway: Gateway IPv6 address or interface
        distance: Administrative distance
        comment: Optional comment
        disabled: Disable the route
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Adding IPv6 route: dst={dst_address}, gateway={gateway}")
    
    cmd = f'/ipv6 route add dst-address="{dst_address}" gateway="{gateway}"'
    
    if distance is not None:
        cmd += f" distance={distance}"
    if comment:
        cmd += f' comment="{comment}"'
    if disabled is not None:
        cmd += f" disabled={'yes' if disabled else 'no'}"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to add IPv6 route: {result}"
    
    return f"IPv6 route to {dst_address} added successfully"


def mikrotik_list_ipv6_routes(
    dst_filter: Optional[str] = None,
    gateway_filter: Optional[str] = None,
    active_only: Optional[bool] = None
) -> str:
    """
    Lists IPv6 routes.
    
    Args:
        dst_filter: Filter by destination
        gateway_filter: Filter by gateway
        active_only: Show only active routes
    
    Returns:
        List of IPv6 routes or error message
    """
    app_logger.info("Listing IPv6 routes")
    
    cmd = "/ipv6 route print"
    
    if dst_filter:
        cmd += f' where dst-address~"{dst_filter}"'
    elif gateway_filter:
        cmd += f' where gateway~"{gateway_filter}"'
    elif active_only:
        cmd += " where active=yes"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list IPv6 routes: {result}"
    
    return f"IPv6 Routes:\n\n{result}"


def mikrotik_remove_ipv6_route(route_id: str) -> str:
    """
    Removes an IPv6 route.
    
    Args:
        route_id: Route ID
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Removing IPv6 route: {route_id}")
    
    cmd = f"/ipv6 route remove {route_id}"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to remove IPv6 route: {result}"
    
    return f"IPv6 route {route_id} removed successfully"


def mikrotik_list_ipv6_neighbors() -> str:
    """
    Lists IPv6 neighbors (Neighbor Discovery).
    
    Returns:
        List of IPv6 neighbors or error message
    """
    app_logger.info("Listing IPv6 neighbors")
    
    cmd = "/ipv6 neighbor print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list IPv6 neighbors: {result}"
    
    return f"IPv6 Neighbors:\n\n{result}"


def mikrotik_get_ipv6_settings() -> str:
    """
    Gets IPv6 settings.
    
    Returns:
        IPv6 settings or error message
    """
    app_logger.info("Getting IPv6 settings")
    
    cmd = "/ipv6 settings print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to get IPv6 settings: {result}"
    
    return f"IPv6 Settings:\n\n{result}"


def mikrotik_set_ipv6_settings(
    accept_redirects: Optional[bool] = None,
    accept_router_advertisements: Optional[bool] = None,
    forward: Optional[bool] = None,
    max_neighbor_entries: Optional[int] = None
) -> str:
    """
    Sets IPv6 settings.
    
    Args:
        accept_redirects: Accept ICMP redirects
        accept_router_advertisements: Accept router advertisements
        forward: Enable IPv6 forwarding
        max_neighbor_entries: Maximum neighbor cache entries
    
    Returns:
        Success message or error
    """
    app_logger.info("Setting IPv6 settings")
    
    cmd = "/ipv6 settings set"
    
    if accept_redirects is not None:
        cmd += f" accept-redirects={'yes' if accept_redirects else 'no'}"
    if accept_router_advertisements is not None:
        cmd += f" accept-router-advertisements={'yes' if accept_router_advertisements else 'no'}"
    if forward is not None:
        cmd += f" forward={'yes' if forward else 'no'}"
    if max_neighbor_entries is not None:
        cmd += f" max-neighbor-entries={max_neighbor_entries}"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to set IPv6 settings: {result}"
    
    return "IPv6 settings configured successfully"
