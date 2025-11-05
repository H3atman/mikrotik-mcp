"""Certificate management for MikroTik RouterOS."""

from typing import Optional
from ..connector import execute_mikrotik_command
from ..logger import app_logger


def mikrotik_list_certificates() -> str:
    """
    Lists certificates.
    
    Returns:
        List of certificates or error message
    """
    app_logger.info("Listing certificates")
    
    cmd = "/certificate print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list certificates: {result}"
    
    return f"Certificates:\n\n{result}"


def mikrotik_create_certificate(
    name: str,
    common_name: str,
    key_size: Optional[int] = None,
    days_valid: Optional[int] = None,
    key_usage: Optional[str] = None,
    subject_alt_name: Optional[str] = None,
    country: Optional[str] = None,
    state: Optional[str] = None,
    locality: Optional[str] = None,
    organization: Optional[str] = None,
    unit: Optional[str] = None
) -> str:
    """
    Creates a certificate.
    
    Args:
        name: Certificate name
        common_name: Common name
        key_size: Key size (1024, 2048, 4096)
        days_valid: Days valid
        key_usage: Key usage (digital-signature, key-encipherment, etc.)
        subject_alt_name: Subject alternative name
        country: Country code
        state: State/province
        locality: City/locality
        organization: Organization name
        unit: Organizational unit
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Creating certificate: name={name}, common_name={common_name}")
    
    cmd = f'/certificate add name="{name}" common-name="{common_name}"'
    
    if key_size:
        cmd += f" key-size={key_size}"
    if days_valid:
        cmd += f" days-valid={days_valid}"
    if key_usage:
        cmd += f' key-usage="{key_usage}"'
    if subject_alt_name:
        cmd += f' subject-alt-name="{subject_alt_name}"'
    if country:
        cmd += f' country="{country}"'
    if state:
        cmd += f' state="{state}"'
    if locality:
        cmd += f' locality="{locality}"'
    if organization:
        cmd += f' organization="{organization}"'
    if unit:
        cmd += f' unit="{unit}"'
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to create certificate: {result}"
    
    return f"Certificate '{name}' created successfully"


def mikrotik_sign_certificate(name: str, ca: Optional[str] = None) -> str:
    """
    Signs a certificate.
    
    Args:
        name: Certificate name
        ca: CA certificate name (for signing)
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Signing certificate: {name}")
    
    if ca:
        cmd = f'/certificate sign [find name="{name}"] ca="{ca}"'
    else:
        cmd = f'/certificate sign [find name="{name}"]'
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to sign certificate: {result}"
    
    return f"Certificate '{name}' signed successfully"


def mikrotik_import_certificate(
    file_name: str,
    passphrase: Optional[str] = None,
    name: Optional[str] = None
) -> str:
    """
    Imports a certificate from file.
    
    Args:
        file_name: Certificate file name
        passphrase: Passphrase for encrypted certificate
        name: Certificate name
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Importing certificate from: {file_name}")
    
    cmd = f'/certificate import file-name="{file_name}"'
    
    if passphrase:
        cmd += f' passphrase="{passphrase}"'
    if name:
        cmd += f' name="{name}"'
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to import certificate: {result}"
    
    return f"Certificate imported from '{file_name}' successfully"


def mikrotik_export_certificate(
    name: str,
    file_name: Optional[str] = None,
    export_passphrase: Optional[str] = None,
    type: Optional[str] = None
) -> str:
    """
    Exports a certificate to file.
    
    Args:
        name: Certificate name
        file_name: Export file name
        export_passphrase: Passphrase for encryption
        type: Export type (pem, pkcs12)
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Exporting certificate: {name}")
    
    cmd = f'/certificate export [find name="{name}"]'
    
    if file_name:
        cmd += f' file-name="{file_name}"'
    if export_passphrase:
        cmd += f' export-passphrase="{export_passphrase}"'
    if type:
        cmd += f" type={type}"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to export certificate: {result}"
    
    return f"Certificate '{name}' exported successfully"


def mikrotik_remove_certificate(name: str) -> str:
    """
    Removes a certificate.
    
    Args:
        name: Certificate name
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Removing certificate: {name}")
    
    cmd = f'/certificate remove [find name="{name}"]'
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to remove certificate: {result}"
    
    return f"Certificate '{name}' removed successfully"


def mikrotik_enable_ssl_certificate(service: str, certificate: str) -> str:
    """
    Enables SSL certificate for a service.
    
    Args:
        service: Service name (www-ssl, api-ssl, etc.)
        certificate: Certificate name
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Enabling SSL certificate for service: {service}")
    
    cmd = f'/certificate enable-ssl-certificate [find name="{certificate}"] service={service}'
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to enable SSL certificate: {result}"
    
    return f"SSL certificate '{certificate}' enabled for service '{service}' successfully"
