"""Bridge interface management for MikroTik RouterOS."""

from typing import Optional
from ..connector import execute_mikrotik_command
from ..logger import app_logger


def mikrotik_create_bridge(
    name: str,
    mtu: Optional[int] = None,
    arp: Optional[str] = None,
    arp_timeout: Optional[str] = None,
    ageing_time: Optional[str] = None,
    priority: Optional[int] = None,
    protocol_mode: Optional[str] = None,
    vlan_filtering: Optional[bool] = None,
    comment: Optional[str] = None,
    disabled: Optional[bool] = None
) -> str:
    """
    Creates a bridge interface on MikroTik device.
    
    Args:
        name: Bridge interface name
        mtu: MTU size
        arp: ARP mode
        arp_timeout: ARP timeout
        ageing_time: MAC address ageing time
        priority: Bridge priority for STP
        protocol_mode: Protocol mode (none, rstp, stp, mstp)
        vlan_filtering: Enable VLAN filtering
        comment: Optional comment
        disabled: Disable the bridge
    
    Returns:
        Command output or error message
    """
    app_logger.info(f"Creating bridge: name={name}")
    
    cmd = f'/interface bridge add name="{name}"'
    
    if mtu:
        cmd += f" mtu={mtu}"
    if arp:
        cmd += f" arp={arp}"
    if arp_timeout:
        cmd += f" arp-timeout={arp_timeout}"
    if ageing_time:
        cmd += f" ageing-time={ageing_time}"
    if priority is not None:
        cmd += f" priority={priority}"
    if protocol_mode:
        cmd += f" protocol-mode={protocol_mode}"
    if vlan_filtering is not None:
        cmd += f" vlan-filtering={'yes' if vlan_filtering else 'no'}"
    if comment:
        cmd += f' comment="{comment}"'
    if disabled is not None:
        cmd += f" disabled={'yes' if disabled else 'no'}"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to create bridge: {result}"
    
    return f"Bridge '{name}' created successfully"


def mikrotik_list_bridges(
    name_filter: Optional[str] = None,
    disabled_only: Optional[bool] = None
) -> str:
    """
    Lists bridge interfaces on MikroTik device.
    
    Args:
        name_filter: Filter by name
        disabled_only: Show only disabled bridges
    
    Returns:
        List of bridges or error message
    """
    app_logger.info("Listing bridges")
    
    cmd = "/interface bridge print"
    
    if name_filter:
        cmd += f' where name~"{name_filter}"'
    elif disabled_only:
        cmd += " where disabled=yes"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list bridges: {result}"
    
    return f"Bridge Interfaces:\n\n{result}"


def mikrotik_remove_bridge(name: str) -> str:
    """
    Removes a bridge interface from MikroTik device.
    
    Args:
        name: Bridge interface name
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Removing bridge: {name}")
    
    cmd = f'/interface bridge remove [find name="{name}"]'
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to remove bridge: {result}"
    
    return f"Bridge '{name}' removed successfully"


def mikrotik_add_bridge_port(
    bridge: str,
    interface: str,
    pvid: Optional[int] = None,
    priority: Optional[int] = None,
    path_cost: Optional[int] = None,
    edge: Optional[bool] = None,
    point_to_point: Optional[str] = None,
    horizon: Optional[int] = None,
    comment: Optional[str] = None,
    disabled: Optional[bool] = None
) -> str:
    """
    Adds an interface to a bridge.
    
    Args:
        bridge: Bridge name
        interface: Interface to add
        pvid: Port VLAN ID
        priority: Port priority for STP
        path_cost: Path cost for STP
        edge: Edge port (fast transition)
        point_to_point: Point-to-point mode (auto, yes, no)
        horizon: Bridge horizon
        comment: Optional comment
        disabled: Disable the port
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Adding bridge port: bridge={bridge}, interface={interface}")
    
    cmd = f'/interface bridge port add bridge="{bridge}" interface="{interface}"'
    
    if pvid is not None:
        cmd += f" pvid={pvid}"
    if priority is not None:
        cmd += f" priority={priority}"
    if path_cost is not None:
        cmd += f" path-cost={path_cost}"
    if edge is not None:
        cmd += f" edge={'yes' if edge else 'no'}"
    if point_to_point:
        cmd += f" point-to-point={point_to_point}"
    if horizon is not None:
        cmd += f" horizon={horizon}"
    if comment:
        cmd += f' comment="{comment}"'
    if disabled is not None:
        cmd += f" disabled={'yes' if disabled else 'no'}"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to add bridge port: {result}"
    
    return f"Interface '{interface}' added to bridge '{bridge}' successfully"


def mikrotik_list_bridge_ports(
    bridge_filter: Optional[str] = None,
    interface_filter: Optional[str] = None
) -> str:
    """
    Lists bridge ports.
    
    Args:
        bridge_filter: Filter by bridge name
        interface_filter: Filter by interface name
    
    Returns:
        List of bridge ports or error message
    """
    app_logger.info("Listing bridge ports")
    
    cmd = "/interface bridge port print"
    
    if bridge_filter:
        cmd += f' where bridge~"{bridge_filter}"'
    elif interface_filter:
        cmd += f' where interface~"{interface_filter}"'
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list bridge ports: {result}"
    
    return f"Bridge Ports:\n\n{result}"


def mikrotik_remove_bridge_port(interface: str) -> str:
    """
    Removes an interface from a bridge.
    
    Args:
        interface: Interface name
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Removing bridge port: {interface}")
    
    cmd = f'/interface bridge port remove [find interface="{interface}"]'
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to remove bridge port: {result}"
    
    return f"Interface '{interface}' removed from bridge successfully"


def mikrotik_add_bridge_vlan(
    bridge: str,
    vlan_ids: str,
    tagged: Optional[str] = None,
    untagged: Optional[str] = None,
    comment: Optional[str] = None,
    disabled: Optional[bool] = None
) -> str:
    """
    Adds VLAN configuration to a bridge.
    
    Args:
        bridge: Bridge name
        vlan_ids: VLAN IDs (e.g., "10" or "10-20")
        tagged: Tagged interfaces (comma-separated)
        untagged: Untagged interfaces (comma-separated)
        comment: Optional comment
        disabled: Disable the VLAN
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Adding bridge VLAN: bridge={bridge}, vlan_ids={vlan_ids}")
    
    cmd = f'/interface bridge vlan add bridge="{bridge}" vlan-ids={vlan_ids}'
    
    if tagged:
        cmd += f' tagged="{tagged}"'
    if untagged:
        cmd += f' untagged="{untagged}"'
    if comment:
        cmd += f' comment="{comment}"'
    if disabled is not None:
        cmd += f" disabled={'yes' if disabled else 'no'}"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to add bridge VLAN: {result}"
    
    return f"Bridge VLAN {vlan_ids} added successfully"


def mikrotik_list_bridge_vlans(bridge_filter: Optional[str] = None) -> str:
    """
    Lists bridge VLAN configurations.
    
    Args:
        bridge_filter: Filter by bridge name
    
    Returns:
        List of bridge VLANs or error message
    """
    app_logger.info("Listing bridge VLANs")
    
    cmd = "/interface bridge vlan print"
    
    if bridge_filter:
        cmd += f' where bridge~"{bridge_filter}"'
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list bridge VLANs: {result}"
    
    return f"Bridge VLANs:\n\n{result}"


def mikrotik_get_bridge_host(bridge_filter: Optional[str] = None) -> str:
    """
    Lists MAC addresses learned by bridges.
    
    Args:
        bridge_filter: Filter by bridge name
    
    Returns:
        List of bridge hosts or error message
    """
    app_logger.info("Listing bridge hosts")
    
    cmd = "/interface bridge host print"
    
    if bridge_filter:
        cmd += f' where bridge~"{bridge_filter}"'
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list bridge hosts: {result}"
    
    return f"Bridge Hosts (MAC Table):\n\n{result}"
