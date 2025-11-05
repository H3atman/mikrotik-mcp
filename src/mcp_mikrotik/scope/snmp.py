"""SNMP management for MikroTik RouterOS."""

from typing import Optional
from ..connector import execute_mikrotik_command
from ..logger import app_logger


def mikrotik_get_snmp_settings() -> str:
    """
    Gets SNMP settings.
    
    Returns:
        SNMP settings or error message
    """
    app_logger.info("Getting SNMP settings")
    
    cmd = "/snmp print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to get SNMP settings: {result}"
    
    return f"SNMP Settings:\n\n{result}"


def mikrotik_set_snmp_settings(
    enabled: Optional[bool] = None,
    contact: Optional[str] = None,
    location: Optional[str] = None,
    engine_id: Optional[str] = None,
    trap_version: Optional[int] = None,
    trap_community: Optional[str] = None,
    trap_generators: Optional[str] = None
) -> str:
    """
    Sets SNMP settings.
    
    Args:
        enabled: Enable SNMP
        contact: Contact information
        location: Location information
        engine_id: SNMP engine ID
        trap_version: SNMP trap version (1, 2, or 3)
        trap_community: Trap community string
        trap_generators: Trap generators (comma-separated)
    
    Returns:
        Success message or error
    """
    app_logger.info("Setting SNMP settings")
    
    cmd = "/snmp set"
    
    if enabled is not None:
        cmd += f" enabled={'yes' if enabled else 'no'}"
    if contact:
        cmd += f' contact="{contact}"'
    if location:
        cmd += f' location="{location}"'
    if engine_id:
        cmd += f' engine-id="{engine_id}"'
    if trap_version is not None:
        cmd += f" trap-version={trap_version}"
    if trap_community:
        cmd += f' trap-community="{trap_community}"'
    if trap_generators:
        cmd += f' trap-generators="{trap_generators}"'
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to set SNMP settings: {result}"
    
    return "SNMP settings configured successfully"


def mikrotik_list_snmp_communities() -> str:
    """
    Lists SNMP communities.
    
    Returns:
        List of SNMP communities or error message
    """
    app_logger.info("Listing SNMP communities")
    
    cmd = "/snmp community print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list SNMP communities: {result}"
    
    return f"SNMP Communities:\n\n{result}"


def mikrotik_add_snmp_community(
    name: str,
    addresses: Optional[str] = None,
    read_access: Optional[bool] = None,
    write_access: Optional[bool] = None,
    authentication_protocol: Optional[str] = None,
    authentication_password: Optional[str] = None,
    encryption_protocol: Optional[str] = None,
    encryption_password: Optional[str] = None,
    comment: Optional[str] = None,
    disabled: Optional[bool] = None
) -> str:
    """
    Adds an SNMP community.
    
    Args:
        name: Community name
        addresses: Allowed addresses (CIDR format)
        read_access: Allow read access
        write_access: Allow write access
        authentication_protocol: Authentication protocol (MD5, SHA1)
        authentication_password: Authentication password
        encryption_protocol: Encryption protocol (DES, AES)
        encryption_password: Encryption password
        comment: Optional comment
        disabled: Disable the community
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Adding SNMP community: name={name}")
    
    cmd = f'/snmp community add name="{name}"'
    
    if addresses:
        cmd += f' addresses="{addresses}"'
    if read_access is not None:
        cmd += f" read-access={'yes' if read_access else 'no'}"
    if write_access is not None:
        cmd += f" write-access={'yes' if write_access else 'no'}"
    if authentication_protocol:
        cmd += f" authentication-protocol={authentication_protocol}"
    if authentication_password:
        cmd += f' authentication-password="{authentication_password}"'
    if encryption_protocol:
        cmd += f" encryption-protocol={encryption_protocol}"
    if encryption_password:
        cmd += f' encryption-password="{encryption_password}"'
    if comment:
        cmd += f' comment="{comment}"'
    if disabled is not None:
        cmd += f" disabled={'yes' if disabled else 'no'}"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to add SNMP community: {result}"
    
    return f"SNMP community '{name}' added successfully"


def mikrotik_remove_snmp_community(name: str) -> str:
    """
    Removes an SNMP community.
    
    Args:
        name: Community name
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Removing SNMP community: {name}")
    
    cmd = f'/snmp community remove [find name="{name}"]'
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to remove SNMP community: {result}"
    
    return f"SNMP community '{name}' removed successfully"
