"""PPPoE server and client management for MikroTik RouterOS."""

from typing import Optional
from ..connector import execute_mikrotik_command
from ..logger import app_logger


def mikrotik_create_pppoe_server(
    service_name: str,
    interface: str,
    default_profile: Optional[str] = None,
    authentication: Optional[str] = None,
    keepalive_timeout: Optional[int] = None,
    max_mtu: Optional[int] = None,
    max_mru: Optional[int] = None,
    one_session_per_host: Optional[bool] = None,
    disabled: Optional[bool] = None
) -> str:
    """
    Creates a PPPoE server.
    
    Args:
        service_name: Service name
        interface: Interface to bind to
        default_profile: Default PPP profile
        authentication: Authentication methods (pap, chap, mschap1, mschap2)
        keepalive_timeout: Keepalive timeout in seconds
        max_mtu: Maximum MTU
        max_mru: Maximum MRU
        one_session_per_host: Allow only one session per host
        disabled: Disable the server
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Creating PPPoE server: service_name={service_name}, interface={interface}")
    
    cmd = f'/interface pppoe-server server add service-name="{service_name}" interface="{interface}"'
    
    if default_profile:
        cmd += f' default-profile="{default_profile}"'
    if authentication:
        cmd += f' authentication={authentication}'
    if keepalive_timeout is not None:
        cmd += f" keepalive-timeout={keepalive_timeout}"
    if max_mtu is not None:
        cmd += f" max-mtu={max_mtu}"
    if max_mru is not None:
        cmd += f" max-mru={max_mru}"
    if one_session_per_host is not None:
        cmd += f" one-session-per-host={'yes' if one_session_per_host else 'no'}"
    if disabled is not None:
        cmd += f" disabled={'yes' if disabled else 'no'}"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to create PPPoE server: {result}"
    
    return f"PPPoE server '{service_name}' created successfully"


def mikrotik_list_pppoe_servers() -> str:
    """
    Lists PPPoE servers.
    
    Returns:
        List of PPPoE servers or error message
    """
    app_logger.info("Listing PPPoE servers")
    
    cmd = "/interface pppoe-server server print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list PPPoE servers: {result}"
    
    return f"PPPoE Servers:\n\n{result}"


def mikrotik_remove_pppoe_server(service_name: str) -> str:
    """
    Removes a PPPoE server.
    
    Args:
        service_name: Service name
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Removing PPPoE server: {service_name}")
    
    cmd = f'/interface pppoe-server server remove [find service-name="{service_name}"]'
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to remove PPPoE server: {result}"
    
    return f"PPPoE server '{service_name}' removed successfully"


def mikrotik_add_ppp_secret(
    name: str,
    password: str,
    service: Optional[str] = None,
    profile: Optional[str] = None,
    local_address: Optional[str] = None,
    remote_address: Optional[str] = None,
    routes: Optional[str] = None,
    limit_bytes_in: Optional[str] = None,
    limit_bytes_out: Optional[str] = None,
    comment: Optional[str] = None,
    disabled: Optional[bool] = None
) -> str:
    """
    Adds a PPP secret (user credentials).
    
    Args:
        name: Username
        password: Password
        service: Service type (any, pppoe, pptp, l2tp, sstp)
        profile: PPP profile
        local_address: Local IP address
        remote_address: Remote IP address
        routes: Static routes for this user
        limit_bytes_in: Incoming traffic limit
        limit_bytes_out: Outgoing traffic limit
        comment: Optional comment
        disabled: Disable the secret
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Adding PPP secret: name={name}")
    
    cmd = f'/ppp secret add name="{name}" password="{password}"'
    
    if service:
        cmd += f" service={service}"
    if profile:
        cmd += f' profile="{profile}"'
    if local_address:
        cmd += f' local-address="{local_address}"'
    if remote_address:
        cmd += f' remote-address="{remote_address}"'
    if routes:
        cmd += f' routes="{routes}"'
    if limit_bytes_in:
        cmd += f' limit-bytes-in={limit_bytes_in}'
    if limit_bytes_out:
        cmd += f' limit-bytes-out={limit_bytes_out}'
    if comment:
        cmd += f' comment="{comment}"'
    if disabled is not None:
        cmd += f" disabled={'yes' if disabled else 'no'}"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to add PPP secret: {result}"
    
    return f"PPP secret '{name}' added successfully"


def mikrotik_list_ppp_secrets(
    service_filter: Optional[str] = None,
    disabled_only: Optional[bool] = None
) -> str:
    """
    Lists PPP secrets.
    
    Args:
        service_filter: Filter by service type
        disabled_only: Show only disabled secrets
    
    Returns:
        List of PPP secrets or error message
    """
    app_logger.info("Listing PPP secrets")
    
    cmd = "/ppp secret print"
    
    if service_filter:
        cmd += f' where service={service_filter}'
    elif disabled_only:
        cmd += " where disabled=yes"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list PPP secrets: {result}"
    
    return f"PPP Secrets:\n\n{result}"


def mikrotik_remove_ppp_secret(name: str) -> str:
    """
    Removes a PPP secret.
    
    Args:
        name: Username
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Removing PPP secret: {name}")
    
    cmd = f'/ppp secret remove [find name="{name}"]'
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to remove PPP secret: {result}"
    
    return f"PPP secret '{name}' removed successfully"


def mikrotik_list_ppp_active() -> str:
    """
    Lists active PPP connections.
    
    Returns:
        List of active PPP connections or error message
    """
    app_logger.info("Listing active PPP connections")
    
    cmd = "/ppp active print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list active PPP connections: {result}"
    
    return f"Active PPP Connections:\n\n{result}"


def mikrotik_disconnect_ppp_active(name: str) -> str:
    """
    Disconnects an active PPP connection.
    
    Args:
        name: Username to disconnect
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Disconnecting PPP user: {name}")
    
    cmd = f'/ppp active remove [find name="{name}"]'
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to disconnect PPP user: {result}"
    
    return f"PPP user '{name}' disconnected successfully"


def mikrotik_create_ppp_profile(
    name: str,
    local_address: Optional[str] = None,
    remote_address: Optional[str] = None,
    dns_server: Optional[str] = None,
    wins_server: Optional[str] = None,
    use_compression: Optional[bool] = None,
    use_encryption: Optional[bool] = None,
    only_one: Optional[bool] = None,
    rate_limit: Optional[str] = None,
    comment: Optional[str] = None
) -> str:
    """
    Creates a PPP profile.
    
    Args:
        name: Profile name
        local_address: Local IP address or pool
        remote_address: Remote IP address or pool
        dns_server: DNS server addresses
        wins_server: WINS server addresses
        use_compression: Use compression
        use_encryption: Use encryption
        only_one: Allow only one session per user
        rate_limit: Rate limit (e.g., "10M/10M")
        comment: Optional comment
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Creating PPP profile: name={name}")
    
    cmd = f'/ppp profile add name="{name}"'
    
    if local_address:
        cmd += f' local-address="{local_address}"'
    if remote_address:
        cmd += f' remote-address="{remote_address}"'
    if dns_server:
        cmd += f' dns-server="{dns_server}"'
    if wins_server:
        cmd += f' wins-server="{wins_server}"'
    if use_compression is not None:
        cmd += f" use-compression={'yes' if use_compression else 'no'}"
    if use_encryption is not None:
        cmd += f" use-encryption={'yes' if use_encryption else 'no'}"
    if only_one is not None:
        cmd += f" only-one={'yes' if only_one else 'no'}"
    if rate_limit:
        cmd += f' rate-limit="{rate_limit}"'
    if comment:
        cmd += f' comment="{comment}"'
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to create PPP profile: {result}"
    
    return f"PPP profile '{name}' created successfully"


def mikrotik_list_ppp_profiles() -> str:
    """
    Lists PPP profiles.
    
    Returns:
        List of PPP profiles or error message
    """
    app_logger.info("Listing PPP profiles")
    
    cmd = "/ppp profile print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list PPP profiles: {result}"
    
    return f"PPP Profiles:\n\n{result}"


def mikrotik_remove_ppp_profile(name: str) -> str:
    """
    Removes a PPP profile.
    
    Args:
        name: Profile name
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Removing PPP profile: {name}")
    
    cmd = f'/ppp profile remove [find name="{name}"]'
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to remove PPP profile: {result}"
    
    return f"PPP profile '{name}' removed successfully"


def mikrotik_create_pppoe_client(
    name: str,
    interface: str,
    user: str,
    password: str,
    service_name: Optional[str] = None,
    add_default_route: Optional[bool] = None,
    use_peer_dns: Optional[bool] = None,
    profile: Optional[str] = None,
    comment: Optional[str] = None,
    disabled: Optional[bool] = None
) -> str:
    """
    Creates a PPPoE client interface.
    
    Args:
        name: Interface name
        interface: Physical interface to use
        user: Username
        password: Password
        service_name: Service name to connect to
        add_default_route: Add default route
        use_peer_dns: Use DNS from peer
        profile: PPP profile
        comment: Optional comment
        disabled: Disable the client
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Creating PPPoE client: name={name}, interface={interface}")
    
    cmd = f'/interface pppoe-client add name="{name}" interface="{interface}" user="{user}" password="{password}"'
    
    if service_name:
        cmd += f' service-name="{service_name}"'
    if add_default_route is not None:
        cmd += f" add-default-route={'yes' if add_default_route else 'no'}"
    if use_peer_dns is not None:
        cmd += f" use-peer-dns={'yes' if use_peer_dns else 'no'}"
    if profile:
        cmd += f' profile="{profile}"'
    if comment:
        cmd += f' comment="{comment}"'
    if disabled is not None:
        cmd += f" disabled={'yes' if disabled else 'no'}"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to create PPPoE client: {result}"
    
    return f"PPPoE client '{name}' created successfully"


def mikrotik_list_pppoe_clients() -> str:
    """
    Lists PPPoE client interfaces.
    
    Returns:
        List of PPPoE clients or error message
    """
    app_logger.info("Listing PPPoE clients")
    
    cmd = "/interface pppoe-client print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list PPPoE clients: {result}"
    
    return f"PPPoE Clients:\n\n{result}"


def mikrotik_remove_pppoe_client(name: str) -> str:
    """
    Removes a PPPoE client interface.
    
    Args:
        name: Interface name
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Removing PPPoE client: {name}")
    
    cmd = f'/interface pppoe-client remove [find name="{name}"]'
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to remove PPPoE client: {result}"
    
    return f"PPPoE client '{name}' removed successfully"
