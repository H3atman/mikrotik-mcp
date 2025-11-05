"""System management operations for MikroTik RouterOS."""

from typing import Optional, List
from ..connector import execute_mikrotik_command
from ..logger import app_logger


def mikrotik_get_system_resource() -> str:
    """
    Gets system resource information (CPU, memory, disk, uptime).
    
    Returns:
        System resource information or error message
    """
    app_logger.info("Getting system resource information")
    
    cmd = "/system resource print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to get system resources: {result}"
    
    return f"System Resources:\n\n{result}"


def mikrotik_get_system_health() -> str:
    """
    Gets system health information (temperature, voltage, etc.).
    
    Returns:
        System health information or error message
    """
    app_logger.info("Getting system health information")
    
    cmd = "/system health print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to get system health: {result}"
    
    return f"System Health:\n\n{result}"


def mikrotik_get_system_identity() -> str:
    """
    Gets the system identity (router name).
    
    Returns:
        System identity or error message
    """
    app_logger.info("Getting system identity")
    
    cmd = "/system identity print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to get system identity: {result}"
    
    return f"System Identity:\n\n{result}"


def mikrotik_set_system_identity(name: str) -> str:
    """
    Sets the system identity (router name).
    
    Args:
        name: New router name
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Setting system identity: name={name}")
    
    cmd = f'/system identity set name="{name}"'
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to set system identity: {result}"
    
    return f"System identity set to '{name}' successfully"


def mikrotik_get_system_clock() -> str:
    """
    Gets system clock settings and current time.
    
    Returns:
        System clock information or error message
    """
    app_logger.info("Getting system clock")
    
    cmd = "/system clock print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to get system clock: {result}"
    
    return f"System Clock:\n\n{result}"


def mikrotik_set_system_clock(
    time_zone_name: Optional[str] = None,
    time_zone_autodetect: Optional[bool] = None
) -> str:
    """
    Sets system clock configuration.
    
    Args:
        time_zone_name: Time zone name (e.g., "America/New_York")
        time_zone_autodetect: Enable automatic time zone detection
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Setting system clock: timezone={time_zone_name}")
    
    cmd = "/system clock set"
    
    if time_zone_name:
        cmd += f' time-zone-name="{time_zone_name}"'
    if time_zone_autodetect is not None:
        cmd += f" time-zone-autodetect={'yes' if time_zone_autodetect else 'no'}"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to set system clock: {result}"
    
    return "System clock configured successfully"


def mikrotik_get_ntp_client() -> str:
    """
    Gets NTP client configuration.
    
    Returns:
        NTP client settings or error message
    """
    app_logger.info("Getting NTP client configuration")
    
    cmd = "/system ntp client print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to get NTP client: {result}"
    
    return f"NTP Client Configuration:\n\n{result}"


def mikrotik_set_ntp_client(
    enabled: Optional[bool] = None,
    servers: Optional[List[str]] = None,
    mode: Optional[str] = None
) -> str:
    """
    Configures NTP client settings.
    
    Args:
        enabled: Enable/disable NTP client
        servers: List of NTP server addresses
        mode: NTP mode ("unicast" or "broadcast")
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Setting NTP client: enabled={enabled}, servers={servers}")
    
    cmd = "/system ntp client set"
    
    if enabled is not None:
        cmd += f" enabled={'yes' if enabled else 'no'}"
    if servers:
        servers_str = ",".join(servers)
        cmd += f' servers="{servers_str}"'
    if mode:
        cmd += f" mode={mode}"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to set NTP client: {result}"
    
    return "NTP client configured successfully"


def mikrotik_system_reboot() -> str:
    """
    Reboots the MikroTik device.
    
    Returns:
        Success message or error
    """
    app_logger.info("Initiating system reboot")
    
    cmd = "/system reboot"
    result = execute_mikrotik_command(cmd)
    
    return "System reboot initiated"


def mikrotik_system_shutdown() -> str:
    """
    Shuts down the MikroTik device.
    
    Returns:
        Success message or error
    """
    app_logger.info("Initiating system shutdown")
    
    cmd = "/system shutdown"
    result = execute_mikrotik_command(cmd)
    
    return "System shutdown initiated"


def mikrotik_list_packages() -> str:
    """
    Lists installed system packages.
    
    Returns:
        List of packages or error message
    """
    app_logger.info("Listing system packages")
    
    cmd = "/system package print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list packages: {result}"
    
    return f"Installed Packages:\n\n{result}"


def mikrotik_enable_package(package_name: str) -> str:
    """
    Enables a system package.
    
    Args:
        package_name: Name of the package to enable
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Enabling package: {package_name}")
    
    cmd = f'/system package enable [find name="{package_name}"]'
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to enable package: {result}"
    
    return f"Package '{package_name}' enabled successfully (reboot required)"


def mikrotik_disable_package(package_name: str) -> str:
    """
    Disables a system package.
    
    Args:
        package_name: Name of the package to disable
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Disabling package: {package_name}")
    
    cmd = f'/system package disable [find name="{package_name}"]'
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to disable package: {result}"
    
    return f"Package '{package_name}' disabled successfully (reboot required)"


def mikrotik_list_scheduler() -> str:
    """
    Lists scheduled tasks.
    
    Returns:
        List of scheduled tasks or error message
    """
    app_logger.info("Listing scheduled tasks")
    
    cmd = "/system scheduler print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list scheduler: {result}"
    
    return f"Scheduled Tasks:\n\n{result}"


def mikrotik_add_scheduler(
    name: str,
    on_event: str,
    start_date: Optional[str] = None,
    start_time: Optional[str] = None,
    interval: Optional[str] = None,
    policy: Optional[str] = None,
    comment: Optional[str] = None,
    disabled: Optional[bool] = None
) -> str:
    """
    Adds a scheduled task.
    
    Args:
        name: Task name
        on_event: Script or command to execute
        start_date: Start date (format: mmm/dd/yyyy)
        start_time: Start time (format: HH:MM:SS)
        interval: Execution interval (e.g., "1d", "1h", "30m")
        policy: Execution policy (e.g., "read,write,policy,test")
        comment: Optional comment
        disabled: Disable the task
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Adding scheduler task: name={name}")
    
    cmd = f'/system scheduler add name="{name}" on-event="{on_event}"'
    
    if start_date:
        cmd += f' start-date="{start_date}"'
    if start_time:
        cmd += f' start-time="{start_time}"'
    if interval:
        cmd += f' interval={interval}'
    if policy:
        cmd += f' policy={policy}'
    if comment:
        cmd += f' comment="{comment}"'
    if disabled is not None:
        cmd += f" disabled={'yes' if disabled else 'no'}"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to add scheduler task: {result}"
    
    return f"Scheduler task '{name}' added successfully"


def mikrotik_remove_scheduler(name: str) -> str:
    """
    Removes a scheduled task.
    
    Args:
        name: Task name
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Removing scheduler task: {name}")
    
    cmd = f'/system scheduler remove [find name="{name}"]'
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to remove scheduler task: {result}"
    
    return f"Scheduler task '{name}' removed successfully"


def mikrotik_list_scripts() -> str:
    """
    Lists system scripts.
    
    Returns:
        List of scripts or error message
    """
    app_logger.info("Listing system scripts")
    
    cmd = "/system script print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list scripts: {result}"
    
    return f"System Scripts:\n\n{result}"


def mikrotik_add_script(
    name: str,
    source: str,
    policy: Optional[str] = None,
    comment: Optional[str] = None,
    dont_require_permissions: Optional[bool] = None
) -> str:
    """
    Adds a system script.
    
    Args:
        name: Script name
        source: Script source code
        policy: Execution policy (e.g., "read,write,policy,test")
        comment: Optional comment
        dont_require_permissions: Don't require permissions
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Adding script: name={name}")
    
    # Escape special characters in source
    source_escaped = source.replace('"', '\\"').replace('\n', '\\n')
    
    cmd = f'/system script add name="{name}" source="{source_escaped}"'
    
    if policy:
        cmd += f' policy={policy}'
    if comment:
        cmd += f' comment="{comment}"'
    if dont_require_permissions is not None:
        cmd += f" dont-require-permissions={'yes' if dont_require_permissions else 'no'}"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to add script: {result}"
    
    return f"Script '{name}' added successfully"


def mikrotik_run_script(name: str) -> str:
    """
    Runs a system script.
    
    Args:
        name: Script name
    
    Returns:
        Script output or error message
    """
    app_logger.info(f"Running script: {name}")
    
    cmd = f'/system script run [find name="{name}"]'
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to run script: {result}"
    
    return f"Script '{name}' executed:\n\n{result}"


def mikrotik_remove_script(name: str) -> str:
    """
    Removes a system script.
    
    Args:
        name: Script name
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Removing script: {name}")
    
    cmd = f'/system script remove [find name="{name}"]'
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to remove script: {result}"
    
    return f"Script '{name}' removed successfully"


def mikrotik_get_system_routerboard() -> str:
    """
    Gets RouterBOARD hardware information.
    
    Returns:
        RouterBOARD information or error message
    """
    app_logger.info("Getting RouterBOARD information")
    
    cmd = "/system routerboard print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to get RouterBOARD info: {result}"
    
    return f"RouterBOARD Information:\n\n{result}"


def mikrotik_get_system_license() -> str:
    """
    Gets system license information.
    
    Returns:
        License information or error message
    """
    app_logger.info("Getting system license")
    
    cmd = "/system license print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to get license info: {result}"
    
    return f"System License:\n\n{result}"


def mikrotik_get_system_history() -> str:
    """
    Gets system command history.
    
    Returns:
        Command history or error message
    """
    app_logger.info("Getting system history")
    
    cmd = "/system history print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to get history: {result}"
    
    return f"System History:\n\n{result}"
