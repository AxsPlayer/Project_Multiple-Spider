# !/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#
# Copyright (c) 2017 Personal. All Rights Reserved
#
################################################################################
"""
The file is designed to crawl the sublinks into set as well as queue.

Authors: AxsPlayer
Date: 2017/12/10 12:49:06
"""
import logging
import Queue
import sys


def save_seed_to_list(url_list_file):
    """Save seed uri address.

    Save the seed html address into unique set as well as queue.

    Args:
        url_list_file: The file address which contains seed uri.

    Returns:
        Two Objects, (unique_html_queue, unique_html_set).
        The first part of tuple is queue which contains the seed html address using (key, value).
        The second part is unique set in which contains the list of unique html address.
        For example:

        ['baidu.com', 'google.com'], set('baidu.com', 'google.com')

    Raises:
        IOError: An error occurred when open seed uri file.
    """
    # Import seed html address from url file.
    seed_html_list = []
    try:
        with open(url_list_file, 'r') as f:
            for line in f:
                line = line.strip()
                seed_html_list.append(line)
    except IOError as e:
        logging.warning('\nThe caught error is:%s' % e.strerror)
        sys.exit(0)
    unique_html_set = set(seed_html_list)  # Convert list into unique set.

    # Create queue and import seed html address into queue.
    unique_html_queue = Queue.Queue()
    for seed_url in unique_html_set:
        unique_html_queue.put((seed_url, 0))  # Save the html in format of (key, value).
    logging.info('Initial seed html address are imported in queue.')  # Print initial unique html list.

    return unique_html_queue, unique_html_set
