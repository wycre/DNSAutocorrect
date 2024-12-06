"""
Celery tasks for dynamicdns.
"""

from celery import shared_task

@shared_task
def run_dns_engine():
    """
    Performs the checks on all DNS records based on timing.
    :return:
    """
    pass
