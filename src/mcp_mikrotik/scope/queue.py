"""Queue management for MikroTik RouterOS."""

from typing import Optional
from ..connector import execute_mikrotik_command
from ..logger import app_logger


def mikrotik_create_simple_queue(
    name: str,
    target: str,
    max_limit: str,
    burst_limit: Optional[str] = None,
    burst_threshold: Optional[str] = None,
    burst_time: Optional[str] = None,
    limit_at: Optional[str] = None,
    priority: Optional[int] = None,
    queue_type: Optional[str] = None,
    parent: Optional[str] = None,
    comment: Optional[str] = None,
    disabled: Optional[bool] = None
) -> str:
    """
    Creates a simple queue for traffic shaping.
    
    Args:
        name: Queue name
        target: Target address/network (e.g., "192.168.1.100/32")
        max_limit: Maximum bandwidth limit (upload/download, e.g., "10M/10M")
        burst_limit: Burst bandwidth limit
        burst_threshold: Burst threshold
        burst_time: Burst time
        limit_at: Guaranteed bandwidth
        priority: Queue priority (1-8)
        queue_type: Queue type (default, pcq, etc.)
        parent: Parent queue name
        comment: Optional comment
        disabled: Disable the queue
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Creating simple queue: name={name}, target={target}")
    
    cmd = f'/queue simple add name="{name}" target="{target}" max-limit={max_limit}'
    
    if burst_limit:
        cmd += f" burst-limit={burst_limit}"
    if burst_threshold:
        cmd += f" burst-threshold={burst_threshold}"
    if burst_time:
        cmd += f" burst-time={burst_time}"
    if limit_at:
        cmd += f" limit-at={limit_at}"
    if priority is not None:
        cmd += f" priority={priority}"
    if queue_type:
        cmd += f" queue={queue_type}"
    if parent:
        cmd += f' parent="{parent}"'
    if comment:
        cmd += f' comment="{comment}"'
    if disabled is not None:
        cmd += f" disabled={'yes' if disabled else 'no'}"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to create simple queue: {result}"
    
    return f"Simple queue '{name}' created successfully"


def mikrotik_list_simple_queues(
    name_filter: Optional[str] = None,
    target_filter: Optional[str] = None,
    disabled_only: Optional[bool] = None
) -> str:
    """
    Lists simple queues.
    
    Args:
        name_filter: Filter by name
        target_filter: Filter by target
        disabled_only: Show only disabled queues
    
    Returns:
        List of simple queues or error message
    """
    app_logger.info("Listing simple queues")
    
    cmd = "/queue simple print"
    
    if name_filter:
        cmd += f' where name~"{name_filter}"'
    elif target_filter:
        cmd += f' where target~"{target_filter}"'
    elif disabled_only:
        cmd += " where disabled=yes"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list simple queues: {result}"
    
    return f"Simple Queues:\n\n{result}"


def mikrotik_remove_simple_queue(name: str) -> str:
    """
    Removes a simple queue.
    
    Args:
        name: Queue name
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Removing simple queue: {name}")
    
    cmd = f'/queue simple remove [find name="{name}"]'
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to remove simple queue: {result}"
    
    return f"Simple queue '{name}' removed successfully"


def mikrotik_enable_simple_queue(name: str) -> str:
    """
    Enables a simple queue.
    
    Args:
        name: Queue name
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Enabling simple queue: {name}")
    
    cmd = f'/queue simple enable [find name="{name}"]'
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to enable simple queue: {result}"
    
    return f"Simple queue '{name}' enabled successfully"


def mikrotik_disable_simple_queue(name: str) -> str:
    """
    Disables a simple queue.
    
    Args:
        name: Queue name
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Disabling simple queue: {name}")
    
    cmd = f'/queue simple disable [find name="{name}"]'
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to disable simple queue: {result}"
    
    return f"Simple queue '{name}' disabled successfully"


def mikrotik_create_queue_tree(
    name: str,
    parent: str,
    max_limit: str,
    burst_limit: Optional[str] = None,
    burst_threshold: Optional[str] = None,
    burst_time: Optional[str] = None,
    limit_at: Optional[str] = None,
    priority: Optional[int] = None,
    queue_type: Optional[str] = None,
    packet_mark: Optional[str] = None,
    comment: Optional[str] = None,
    disabled: Optional[bool] = None
) -> str:
    """
    Creates a queue tree entry for advanced QoS.
    
    Args:
        name: Queue name
        parent: Parent (interface or queue)
        max_limit: Maximum bandwidth limit
        burst_limit: Burst bandwidth limit
        burst_threshold: Burst threshold
        burst_time: Burst time
        limit_at: Guaranteed bandwidth
        priority: Queue priority (1-8)
        queue_type: Queue type (default, pcq, etc.)
        packet_mark: Packet mark to match
        comment: Optional comment
        disabled: Disable the queue
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Creating queue tree: name={name}, parent={parent}")
    
    cmd = f'/queue tree add name="{name}" parent="{parent}" max-limit={max_limit}'
    
    if burst_limit:
        cmd += f" burst-limit={burst_limit}"
    if burst_threshold:
        cmd += f" burst-threshold={burst_threshold}"
    if burst_time:
        cmd += f" burst-time={burst_time}"
    if limit_at:
        cmd += f" limit-at={limit_at}"
    if priority is not None:
        cmd += f" priority={priority}"
    if queue_type:
        cmd += f" queue={queue_type}"
    if packet_mark:
        cmd += f' packet-mark="{packet_mark}"'
    if comment:
        cmd += f' comment="{comment}"'
    if disabled is not None:
        cmd += f" disabled={'yes' if disabled else 'no'}"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to create queue tree: {result}"
    
    return f"Queue tree '{name}' created successfully"


def mikrotik_list_queue_tree(
    name_filter: Optional[str] = None,
    parent_filter: Optional[str] = None,
    disabled_only: Optional[bool] = None
) -> str:
    """
    Lists queue tree entries.
    
    Args:
        name_filter: Filter by name
        parent_filter: Filter by parent
        disabled_only: Show only disabled queues
    
    Returns:
        List of queue tree entries or error message
    """
    app_logger.info("Listing queue tree")
    
    cmd = "/queue tree print"
    
    if name_filter:
        cmd += f' where name~"{name_filter}"'
    elif parent_filter:
        cmd += f' where parent~"{parent_filter}"'
    elif disabled_only:
        cmd += " where disabled=yes"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list queue tree: {result}"
    
    return f"Queue Tree:\n\n{result}"


def mikrotik_remove_queue_tree(name: str) -> str:
    """
    Removes a queue tree entry.
    
    Args:
        name: Queue name
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Removing queue tree: {name}")
    
    cmd = f'/queue tree remove [find name="{name}"]'
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to remove queue tree: {result}"
    
    return f"Queue tree '{name}' removed successfully"


def mikrotik_list_queue_types() -> str:
    """
    Lists available queue types.
    
    Returns:
        List of queue types or error message
    """
    app_logger.info("Listing queue types")
    
    cmd = "/queue type print"
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to list queue types: {result}"
    
    return f"Queue Types:\n\n{result}"


def mikrotik_create_queue_type(
    name: str,
    kind: str,
    pcq_rate: Optional[str] = None,
    pcq_limit: Optional[str] = None,
    pcq_classifier: Optional[str] = None,
    pcq_total_limit: Optional[str] = None
) -> str:
    """
    Creates a custom queue type (PCQ).
    
    Args:
        name: Queue type name
        kind: Queue kind (pcq, pfifo, bfifo, etc.)
        pcq_rate: PCQ rate limit
        pcq_limit: PCQ queue size limit
        pcq_classifier: PCQ classifier (src-address, dst-address, etc.)
        pcq_total_limit: PCQ total limit
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Creating queue type: name={name}, kind={kind}")
    
    cmd = f'/queue type add name="{name}" kind={kind}'
    
    if pcq_rate:
        cmd += f" pcq-rate={pcq_rate}"
    if pcq_limit:
        cmd += f" pcq-limit={pcq_limit}"
    if pcq_classifier:
        cmd += f" pcq-classifier={pcq_classifier}"
    if pcq_total_limit:
        cmd += f" pcq-total-limit={pcq_total_limit}"
    
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to create queue type: {result}"
    
    return f"Queue type '{name}' created successfully"


def mikrotik_remove_queue_type(name: str) -> str:
    """
    Removes a custom queue type.
    
    Args:
        name: Queue type name
    
    Returns:
        Success message or error
    """
    app_logger.info(f"Removing queue type: {name}")
    
    cmd = f'/queue type remove [find name="{name}"]'
    result = execute_mikrotik_command(cmd)
    
    if "failure:" in result.lower() or "error" in result.lower():
        return f"Failed to remove queue type: {result}"
    
    return f"Queue type '{name}' removed successfully"


def mikrotik_reset_queue_counters() -> str:
    """
    Resets queue counters.
    
    Returns:
        Success message or error
    """
    app_logger.info("Resetting queue counters")
    
    cmd = "/queue simple reset-counters"
    result = execute_mikrotik_command(cmd)
    
    return "Queue counters reset successfully"
