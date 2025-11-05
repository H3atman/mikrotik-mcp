"""IPsec VPN management for MikroTik RouterOS."""

from typing import Optional
from ..connector import execute_mikrotik_command
from ..logger import app_logger


def mikrotik_create_ipsec_peer(
    name: str,
    address: str,
    auth_method: Optional[str] = None,
    secret: Optional[str] = None,
    exchange_mode: Optional[str] = None,
    send_initial_contact: Optional[bool] = None,
    comment: Optional[str] = None,
    disabled: Optional[bool] = None
) -> str:
    """
    Creates an IPsec peer.
    
    Args:
        name: Peer name
        address: Peer IP address
        auth_method: Authentication method (pre-shared-key, rsa-signature, etc.)
        secret: Pre-shared key
        exchange_mode: Exchange mode (main, aggressive, ike2)
        send_initial_contact: Send initial contact
        comment: Optional comment
        disabled: Disable the peer
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Creating IPsec peer: name={name}, address={address}")
    
    cmd = f'/ip ipsec peer add name="{name}" address="{address}"'
    
    if auth_method:
        cmd += f" auth-method={auth_method}"
    if secret:
        cmd += f' secret="{secret}"'
    if exchange_mode:
        cmd += f" exchange-mode={exchange_mode}"
    if send_initial_contact is not None:
        cmd += f" send-initial-contact={'yes' if send_initial_contact else 'no'}"
    if comment:
        cmd += f' comment="{comment}"'
    if disabled is not None:
        cmd += f" disabled={'yes' if disabled else 'no'}"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to create IPsec peer: {result}"
    
    return f"IPsec peer '{name}' created successfully"


def mikrotik_list_ipsec_peers() -> str:
    """
    Lists IPsec peers.
    
    Returns:
        List of IPsec peers or error message
    """
    app_logger.info("Listing IPsec peers")
    
    cmd = "/ip ipsec peer print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list IPsec peers: {result}"
    
    return f"IPsec Peers:\n\n{result}"


def mikrotik_remove_ipsec_peer(name: str) -> str:
    """
    Removes an IPsec peer.
    
    Args:
        name: Peer name
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Removing IPsec peer: {name}")
    
    cmd = f'/ip ipsec peer remove [find name="{name}"]'
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to remove IPsec peer: {result}"
    
    return f"IPsec peer '{name}' removed successfully"


def mikrotik_create_ipsec_proposal(
    name: str,
    auth_algorithms: Optional[str] = None,
    enc_algorithms: Optional[str] = None,
    lifetime: Optional[str] = None,
    pfs_group: Optional[str] = None,
    comment: Optional[str] = None,
    disabled: Optional[bool] = None
) -> str:
    """
    Creates an IPsec proposal.
    
    Args:
        name: Proposal name
        auth_algorithms: Authentication algorithms (sha1, sha256, etc.)
        enc_algorithms: Encryption algorithms (aes-128-cbc, aes-256-cbc, etc.)
        lifetime: Lifetime
        pfs_group: PFS group
        comment: Optional comment
        disabled: Disable the proposal
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Creating IPsec proposal: name={name}")
    
    cmd = f'/ip ipsec proposal add name="{name}"'
    
    if auth_algorithms:
        cmd += f" auth-algorithms={auth_algorithms}"
    if enc_algorithms:
        cmd += f" enc-algorithms={enc_algorithms}"
    if lifetime:
        cmd += f" lifetime={lifetime}"
    if pfs_group:
        cmd += f" pfs-group={pfs_group}"
    if comment:
        cmd += f' comment="{comment}"'
    if disabled is not None:
        cmd += f" disabled={'yes' if disabled else 'no'}"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to create IPsec proposal: {result}"
    
    return f"IPsec proposal '{name}' created successfully"


def mikrotik_list_ipsec_proposals() -> str:
    """
    Lists IPsec proposals.
    
    Returns:
        List of IPsec proposals or error message
    """
    app_logger.info("Listing IPsec proposals")
    
    cmd = "/ip ipsec proposal print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list IPsec proposals: {result}"
    
    return f"IPsec Proposals:\n\n{result}"


def mikrotik_list_ipsec_installed_sa() -> str:
    """
    Lists installed IPsec Security Associations.
    
    Returns:
        List of installed SAs or error message
    """
    app_logger.info("Listing IPsec installed SAs")
    
    cmd = "/ip ipsec installed-sa print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list IPsec installed SAs: {result}"
    
    return f"IPsec Installed SAs:\n\n{result}"


def mikrotik_create_ipsec_policy(
    src_address: str,
    dst_address: str,
    action: Optional[str] = None,
    proposal: Optional[str] = None,
    tunnel: Optional[bool] = None,
    comment: Optional[str] = None,
    disabled: Optional[bool] = None
) -> str:
    """
    Creates an IPsec policy.
    
    Args:
        src_address: Source address
        dst_address: Destination address
        action: Action (encrypt, discard, none)
        proposal: Proposal name
        tunnel: Tunnel mode
        comment: Optional comment
        disabled: Disable the policy
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Creating IPsec policy: src={src_address}, dst={dst_address}")
    
    cmd = f'/ip ipsec policy add src-address="{src_address}" dst-address="{dst_address}"'
    
    if action:
        cmd += f" action={action}"
    if proposal:
        cmd += f' proposal="{proposal}"'
    if tunnel is not None:
        cmd += f" tunnel={'yes' if tunnel else 'no'}"
    if comment:
        cmd += f' comment="{comment}"'
    if disabled is not None:
        cmd += f" disabled={'yes' if disabled else 'no'}"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to create IPsec policy: {result}"
    
    return "IPsec policy created successfully"


def mikrotik_list_ipsec_policies() -> str:
    """
    Lists IPsec policies.
    
    Returns:
        List of IPsec policies or error message
    """
    app_logger.info("Listing IPsec policies")
    
    cmd = "/ip ipsec policy print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list IPsec policies: {result}"
    
    return f"IPsec Policies:\n\n{result}"
