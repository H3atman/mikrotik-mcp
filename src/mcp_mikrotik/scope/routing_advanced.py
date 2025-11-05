"""Advanced routing protocols (BGP, OSPF, RIP) for MikroTik RouterOS."""

from typing import Optional
from ..connector import execute_mikrotik_command
from ..logger import app_logger


# ============================================================================
# BGP Functions
# ============================================================================

def mikrotik_create_bgp_instance(
    name: str,
    as_number: int,
    router_id: Optional[str] = None,
    redistribute_connected: Optional[bool] = None,
    redistribute_static: Optional[bool] = None,
    redistribute_ospf: Optional[bool] = None,
    client_to_client_reflection: Optional[bool] = None,
    comment: Optional[str] = None,
    disabled: Optional[bool] = None
) -> str:
    """
    Creates a BGP instance.
    
    Args:
        name: Instance name
        as_number: AS number
        router_id: Router ID
        redistribute_connected: Redistribute connected routes
        redistribute_static: Redistribute static routes
        redistribute_ospf: Redistribute OSPF routes
        client_to_client_reflection: Enable client-to-client reflection
        comment: Optional comment
        disabled: Disable the instance
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Creating BGP instance: name={name}, as={as_number}")
    
    cmd = f'/routing bgp instance add name="{name}" as={as_number}'
    
    if router_id:
        cmd += f' router-id="{router_id}"'
    if redistribute_connected is not None:
        cmd += f" redistribute-connected={'yes' if redistribute_connected else 'no'}"
    if redistribute_static is not None:
        cmd += f" redistribute-static={'yes' if redistribute_static else 'no'}"
    if redistribute_ospf is not None:
        cmd += f" redistribute-ospf={'yes' if redistribute_ospf else 'no'}"
    if client_to_client_reflection is not None:
        cmd += f" client-to-client-reflection={'yes' if client_to_client_reflection else 'no'}"
    if comment:
        cmd += f' comment="{comment}"'
    if disabled is not None:
        cmd += f" disabled={'yes' if disabled else 'no'}"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to create BGP instance: {result}"
    
    return f"BGP instance '{name}' created successfully"


def mikrotik_list_bgp_instances() -> str:
    """
    Lists BGP instances.
    
    Returns:
        List of BGP instances or error message
    """
    app_logger.info("Listing BGP instances")
    
    cmd = "/routing bgp instance print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list BGP instances: {result}"
    
    return f"BGP Instances:\n\n{result}"


def mikrotik_remove_bgp_instance(name: str) -> str:
    """
    Removes a BGP instance.
    
    Args:
        name: Instance name
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Removing BGP instance: {name}")
    
    cmd = f'/routing bgp instance remove [find name="{name}"]'
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to remove BGP instance: {result}"
    
    return f"BGP instance '{name}' removed successfully"


def mikrotik_add_bgp_peer(
    name: str,
    instance: str,
    remote_address: str,
    remote_as: int,
    ttl: Optional[int] = None,
    multihop: Optional[bool] = None,
    route_reflect: Optional[bool] = None,
    hold_time: Optional[str] = None,
    tcp_md5_key: Optional[str] = None,
    update_source: Optional[str] = None,
    comment: Optional[str] = None,
    disabled: Optional[bool] = None
) -> str:
    """
    Adds a BGP peer.
    
    Args:
        name: Peer name
        instance: BGP instance name
        remote_address: Remote peer IP address
        remote_as: Remote AS number
        ttl: TTL for BGP packets
        multihop: Enable multihop
        route_reflect: Route reflector client
        hold_time: Hold time
        tcp_md5_key: TCP MD5 authentication key
        update_source: Update source address
        comment: Optional comment
        disabled: Disable the peer
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Adding BGP peer: name={name}, remote_address={remote_address}")
    
    cmd = f'/routing bgp peer add name="{name}" instance="{instance}" remote-address="{remote_address}" remote-as={remote_as}'
    
    if ttl is not None:
        cmd += f" ttl={ttl}"
    if multihop is not None:
        cmd += f" multihop={'yes' if multihop else 'no'}"
    if route_reflect is not None:
        cmd += f" route-reflect={'yes' if route_reflect else 'no'}"
    if hold_time:
        cmd += f" hold-time={hold_time}"
    if tcp_md5_key:
        cmd += f' tcp-md5-key="{tcp_md5_key}"'
    if update_source:
        cmd += f' update-source="{update_source}"'
    if comment:
        cmd += f' comment="{comment}"'
    if disabled is not None:
        cmd += f" disabled={'yes' if disabled else 'no'}"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to add BGP peer: {result}"
    
    return f"BGP peer '{name}' added successfully"


def mikrotik_list_bgp_peers() -> str:
    """
    Lists BGP peers.
    
    Returns:
        List of BGP peers or error message
    """
    app_logger.info("Listing BGP peers")
    
    cmd = "/routing bgp peer print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list BGP peers: {result}"
    
    return f"BGP Peers:\n\n{result}"


def mikrotik_remove_bgp_peer(name: str) -> str:
    """
    Removes a BGP peer.
    
    Args:
        name: Peer name
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Removing BGP peer: {name}")
    
    cmd = f'/routing bgp peer remove [find name="{name}"]'
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to remove BGP peer: {result}"
    
    return f"BGP peer '{name}' removed successfully"


def mikrotik_list_bgp_advertisements() -> str:
    """
    Lists BGP advertisements.
    
    Returns:
        List of BGP advertisements or error message
    """
    app_logger.info("Listing BGP advertisements")
    
    cmd = "/routing bgp advertisements print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list BGP advertisements: {result}"
    
    return f"BGP Advertisements:\n\n{result}"


# ============================================================================
# OSPF Functions
# ============================================================================

def mikrotik_create_ospf_instance(
    name: str,
    router_id: Optional[str] = None,
    redistribute_connected: Optional[bool] = None,
    redistribute_static: Optional[bool] = None,
    redistribute_bgp: Optional[bool] = None,
    comment: Optional[str] = None,
    disabled: Optional[bool] = None
) -> str:
    """
    Creates an OSPF instance.
    
    Args:
        name: Instance name
        router_id: Router ID
        redistribute_connected: Redistribute connected routes
        redistribute_static: Redistribute static routes
        redistribute_bgp: Redistribute BGP routes
        comment: Optional comment
        disabled: Disable the instance
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Creating OSPF instance: name={name}")
    
    cmd = f'/routing ospf instance add name="{name}"'
    
    if router_id:
        cmd += f' router-id="{router_id}"'
    if redistribute_connected is not None:
        cmd += f" redistribute-connected={'yes' if redistribute_connected else 'no'}"
    if redistribute_static is not None:
        cmd += f" redistribute-static={'yes' if redistribute_static else 'no'}"
    if redistribute_bgp is not None:
        cmd += f" redistribute-bgp={'yes' if redistribute_bgp else 'no'}"
    if comment:
        cmd += f' comment="{comment}"'
    if disabled is not None:
        cmd += f" disabled={'yes' if disabled else 'no'}"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to create OSPF instance: {result}"
    
    return f"OSPF instance '{name}' created successfully"


def mikrotik_list_ospf_instances() -> str:
    """
    Lists OSPF instances.
    
    Returns:
        List of OSPF instances or error message
    """
    app_logger.info("Listing OSPF instances")
    
    cmd = "/routing ospf instance print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list OSPF instances: {result}"
    
    return f"OSPF Instances:\n\n{result}"


def mikrotik_remove_ospf_instance(name: str) -> str:
    """
    Removes an OSPF instance.
    
    Args:
        name: Instance name
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Removing OSPF instance: {name}")
    
    cmd = f'/routing ospf instance remove [find name="{name}"]'
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to remove OSPF instance: {result}"
    
    return f"OSPF instance '{name}' removed successfully"


def mikrotik_add_ospf_area(
    name: str,
    area_id: str,
    instance: Optional[str] = None,
    type: Optional[str] = None,
    comment: Optional[str] = None,
    disabled: Optional[bool] = None
) -> str:
    """
    Adds an OSPF area.
    
    Args:
        name: Area name
        area_id: Area ID (e.g., "0.0.0.0" for backbone)
        instance: OSPF instance name
        type: Area type (default, stub, nssa)
        comment: Optional comment
        disabled: Disable the area
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Adding OSPF area: name={name}, area_id={area_id}")
    
    cmd = f'/routing ospf area add name="{name}" area-id="{area_id}"'
    
    if instance:
        cmd += f' instance="{instance}"'
    if type:
        cmd += f" type={type}"
    if comment:
        cmd += f' comment="{comment}"'
    if disabled is not None:
        cmd += f" disabled={'yes' if disabled else 'no'}"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to add OSPF area: {result}"
    
    return f"OSPF area '{name}' added successfully"


def mikrotik_list_ospf_areas() -> str:
    """
    Lists OSPF areas.
    
    Returns:
        List of OSPF areas or error message
    """
    app_logger.info("Listing OSPF areas")
    
    cmd = "/routing ospf area print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list OSPF areas: {result}"
    
    return f"OSPF Areas:\n\n{result}"


def mikrotik_add_ospf_network(
    network: str,
    area: str,
    comment: Optional[str] = None,
    disabled: Optional[bool] = None
) -> str:
    """
    Adds an OSPF network.
    
    Args:
        network: Network address (e.g., "192.168.1.0/24")
        area: Area name
        comment: Optional comment
        disabled: Disable the network
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Adding OSPF network: network={network}, area={area}")
    
    cmd = f'/routing ospf network add network="{network}" area="{area}"'
    
    if comment:
        cmd += f' comment="{comment}"'
    if disabled is not None:
        cmd += f" disabled={'yes' if disabled else 'no'}"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to add OSPF network: {result}"
    
    return f"OSPF network '{network}' added successfully"


def mikrotik_list_ospf_networks() -> str:
    """
    Lists OSPF networks.
    
    Returns:
        List of OSPF networks or error message
    """
    app_logger.info("Listing OSPF networks")
    
    cmd = "/routing ospf network print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list OSPF networks: {result}"
    
    return f"OSPF Networks:\n\n{result}"


def mikrotik_list_ospf_neighbors() -> str:
    """
    Lists OSPF neighbors.
    
    Returns:
        List of OSPF neighbors or error message
    """
    app_logger.info("Listing OSPF neighbors")
    
    cmd = "/routing ospf neighbor print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list OSPF neighbors: {result}"
    
    return f"OSPF Neighbors:\n\n{result}"


def mikrotik_add_ospf_interface(
    interface: str,
    network_type: Optional[str] = None,
    priority: Optional[int] = None,
    cost: Optional[int] = None,
    authentication: Optional[str] = None,
    authentication_key: Optional[str] = None,
    comment: Optional[str] = None,
    disabled: Optional[bool] = None
) -> str:
    """
    Adds an OSPF interface configuration.
    
    Args:
        interface: Interface name
        network_type: Network type (broadcast, point-to-point, nbma, etc.)
        priority: Router priority
        cost: Interface cost
        authentication: Authentication type (none, simple, md5)
        authentication_key: Authentication key
        comment: Optional comment
        disabled: Disable the interface
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Adding OSPF interface: interface={interface}")
    
    cmd = f'/routing ospf interface add interface="{interface}"'
    
    if network_type:
        cmd += f" network-type={network_type}"
    if priority is not None:
        cmd += f" priority={priority}"
    if cost is not None:
        cmd += f" cost={cost}"
    if authentication:
        cmd += f" authentication={authentication}"
    if authentication_key:
        cmd += f' authentication-key="{authentication_key}"'
    if comment:
        cmd += f' comment="{comment}"'
    if disabled is not None:
        cmd += f" disabled={'yes' if disabled else 'no'}"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to add OSPF interface: {result}"
    
    return f"OSPF interface '{interface}' added successfully"


def mikrotik_list_ospf_interfaces() -> str:
    """
    Lists OSPF interfaces.
    
    Returns:
        List of OSPF interfaces or error message
    """
    app_logger.info("Listing OSPF interfaces")
    
    cmd = "/routing ospf interface print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list OSPF interfaces: {result}"
    
    return f"OSPF Interfaces:\n\n{result}"


# ============================================================================
# RIP Functions
# ============================================================================

def mikrotik_create_rip_instance(
    name: str,
    redistribute_connected: Optional[bool] = None,
    redistribute_static: Optional[bool] = None,
    redistribute_ospf: Optional[bool] = None,
    redistribute_bgp: Optional[bool] = None,
    comment: Optional[str] = None,
    disabled: Optional[bool] = None
) -> str:
    """
    Creates a RIP instance.
    
    Args:
        name: Instance name
        redistribute_connected: Redistribute connected routes
        redistribute_static: Redistribute static routes
        redistribute_ospf: Redistribute OSPF routes
        redistribute_bgp: Redistribute BGP routes
        comment: Optional comment
        disabled: Disable the instance
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Creating RIP instance: name={name}")
    
    cmd = f'/routing rip instance add name="{name}"'
    
    if redistribute_connected is not None:
        cmd += f" redistribute-connected={'yes' if redistribute_connected else 'no'}"
    if redistribute_static is not None:
        cmd += f" redistribute-static={'yes' if redistribute_static else 'no'}"
    if redistribute_ospf is not None:
        cmd += f" redistribute-ospf={'yes' if redistribute_ospf else 'no'}"
    if redistribute_bgp is not None:
        cmd += f" redistribute-bgp={'yes' if redistribute_bgp else 'no'}"
    if comment:
        cmd += f' comment="{comment}"'
    if disabled is not None:
        cmd += f" disabled={'yes' if disabled else 'no'}"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to create RIP instance: {result}"
    
    return f"RIP instance '{name}' created successfully"


def mikrotik_list_rip_instances() -> str:
    """
    Lists RIP instances.
    
    Returns:
        List of RIP instances or error message
    """
    app_logger.info("Listing RIP instances")
    
    cmd = "/routing rip instance print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list RIP instances: {result}"
    
    return f"RIP Instances:\n\n{result}"


def mikrotik_remove_rip_instance(name: str) -> str:
    """
    Removes a RIP instance.
    
    Args:
        name: Instance name
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Removing RIP instance: {name}")
    
    cmd = f'/routing rip instance remove [find name="{name}"]'
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to remove RIP instance: {result}"
    
    return f"RIP instance '{name}' removed successfully"


def mikrotik_add_rip_network(
    network: str,
    instance: Optional[str] = None,
    comment: Optional[str] = None,
    disabled: Optional[bool] = None
) -> str:
    """
    Adds a RIP network.
    
    Args:
        network: Network address (e.g., "192.168.1.0/24")
        instance: RIP instance name
        comment: Optional comment
        disabled: Disable the network
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Adding RIP network: network={network}")
    
    cmd = f'/routing rip network add network="{network}"'
    
    if instance:
        cmd += f' instance="{instance}"'
    if comment:
        cmd += f' comment="{comment}"'
    if disabled is not None:
        cmd += f" disabled={'yes' if disabled else 'no'}"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to add RIP network: {result}"
    
    return f"RIP network '{network}' added successfully"


def mikrotik_list_rip_networks() -> str:
    """
    Lists RIP networks.
    
    Returns:
        List of RIP networks or error message
    """
    app_logger.info("Listing RIP networks")
    
    cmd = "/routing rip network print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list RIP networks: {result}"
    
    return f"RIP Networks:\n\n{result}"


def mikrotik_add_rip_interface(
    interface: str,
    receive: Optional[str] = None,
    send: Optional[str] = None,
    authentication: Optional[str] = None,
    authentication_key: Optional[str] = None,
    comment: Optional[str] = None,
    disabled: Optional[bool] = None
) -> str:
    """
    Adds a RIP interface configuration.
    
    Args:
        interface: Interface name
        receive: Receive mode (no, v1, v2, v1-v2)
        send: Send mode (no, v1, v2, v1-v2)
        authentication: Authentication type (none, simple, md5)
        authentication_key: Authentication key
        comment: Optional comment
        disabled: Disable the interface
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Adding RIP interface: interface={interface}")
    
    cmd = f'/routing rip interface add interface="{interface}"'
    
    if receive:
        cmd += f" receive={receive}"
    if send:
        cmd += f" send={send}"
    if authentication:
        cmd += f" authentication={authentication}"
    if authentication_key:
        cmd += f' authentication-key="{authentication_key}"'
    if comment:
        cmd += f' comment="{comment}"'
    if disabled is not None:
        cmd += f" disabled={'yes' if disabled else 'no'}"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to add RIP interface: {result}"
    
    return f"RIP interface '{interface}' added successfully"


def mikrotik_list_rip_interfaces() -> str:
    """
    Lists RIP interfaces.
    
    Returns:
        List of RIP interfaces or error message
    """
    app_logger.info("Listing RIP interfaces")
    
    cmd = "/routing rip interface print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list RIP interfaces: {result}"
    
    return f"RIP Interfaces:\n\n{result}"


def mikrotik_list_rip_neighbors() -> str:
    """
    Lists RIP neighbors.
    
    Returns:
        List of RIP neighbors or error message
    """
    app_logger.info("Listing RIP neighbors")
    
    cmd = "/routing rip neighbor print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list RIP neighbors: {result}"
    
    return f"RIP Neighbors:\n\n{result}"
