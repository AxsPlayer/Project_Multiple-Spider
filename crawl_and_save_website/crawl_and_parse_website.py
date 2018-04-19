# !/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#
# Copyright (c) 2017 Personal. All Rights Reserved
#
################################################################################
"""
The file is designed to crawl the sublinks.

Authors: Daniel&
Date: 2017/12/10 12:49:06
"""
import logging
import time
import urllib2
import urlparse
import socket

import bs4

from crawl_and_save_website import save_html_into_file


def parse_sublink_to_list(a_blocks, html_address):
    """Parse html content and save sublinks into list.

    Search for <href> records in <a> block, convert the sublinks into suitable format,
    and save converted sublinks into list.

    Args:
        a_blocks: The input list of <a> blocks to search for sublinks.
        html_address: The html address of the mother links.

    Returns:
        The list of sublinks. For example: ['baidu.com', 'google.com']
    """
    sublink_list = []
    for each in a_blocks:
        if each.get('href') is None:
            continue
        sublink = each.get('href')
        sublink_lower = sublink.lower()
        # Decide whether url address should be joint or not.
        if sublink_lower.startswith('http'):
            sublink_conversion = sublink
        else:
            sublink_conversion = urlparse.urljoin(html_address, sublink)
        # Prevent from saving duplicate links into list.
        if sublink_conversion in sublink_list:
            continue
        else:
            sublink_list.append(sublink_conversion)
    return sublink_list


def save_sublinks_to_queue(html_address, **parameter_dictionary):
    """Save sublinks in the html into list.

    Use beautiful soup to crawl the <href>sublinks and save sublinks into list.

    Args:
        html_address: The target html address which is used to create joined sublinks.
        parameter_dictionary: The dictionary which contains the
            necessary parameters in configuration file.

    Returns:
        Two Objects, sublink_list, html_content.
        The first part is the list containing sublink addresses.
        The second part is the html content of the input html address.
        For example:

        ['baidu.com', 'google.com'], '<a name='top'></a>'

        If the input html is not found, then the first part of output tuple
        is [], the second part is the type of the error.

    Raises:
        urllib2.HTTPError: An error occurred when html is not found.
        urllib2.URLError: An error occurred when url is not found.
    """
    # Parse website content and save sublink address into list. (cope with the url error)
    try:
        html_response = urllib2.urlopen(html_address, data=None,
                                        timeout=float(parameter_dictionary['crawl_timeout']))
    except urllib2.HTTPError as e:
        logging.warning('\n%s is not found. The reason is %s with %s.' %
                        (html_address, str(e.reason), str(e.code)))
        return [], str(e)
    except (urllib2.URLError, socket.timeout) as e:
        logging.warning('\n%s is not found. The reason is %s.' %
                        (html_address, str(e.reason)))
        return [], str(e)

    # Fetch decoding method of website, and ignore the unusual decoding.
    html_content = html_response.read()
    soup_code = bs4.BeautifulSoup(html_content, "lxml")
    code_method = soup_code.original_encoding  # Fetch website's encode method.
    html_content_conversion = html_content.decode(code_method, 'ignore').encode(code_method)

    # Search for the target <a> block in html content.
    soup = bs4.BeautifulSoup(html_content_conversion, "lxml")
    href_ = soup.find_all(name='a')

    # Parse the <a> blocks and save sublinks into list.
    sublink_list = parse_sublink_to_list(href_, html_address)

    time.sleep(float(parameter_dictionary['crawl_interval']))  # Set the sleep time interval for spider.

    return sublink_list, html_content


def crawl_and_save_html(unique_html_set, lock, unique_html_queue_para, **parameter_dic):
    """Crawl the html content and save html.

    Crawl the html address in unique queue and write the satisfying html's content into file.
    This function and process actors as consumer as well as producer for queue.

    Args:
        unique_html_set: The set to save unique html address.
        lock: The threading lock to change the common variable safely.
        unique_html_queue_para: The queue of html addresses which crawl function
            should get target url from and put sublink into.
        parameter_dic: The dictionary which contains the
            necessary parameters in configuration file.

    Returns: None.
    """
    # Set circulation to crawl websites in queue until all the tasks are done.
    while True:
        # Fetch the message in format of (key, value) from queue as consumer.
        html_address, url_depth = unique_html_queue_para.get(block=True, timeout=None)

        # Parse the html content and crawl the sublinks.
        sublink_list, html_content = save_sublinks_to_queue(html_address, **parameter_dic)

        # Check the url pattern and save the target html content into files.
        save_html_into_file.save_html_to_file(html_address, html_content,
                                              url_depth, **parameter_dic)

        # Fetch every element in list, check if already in set and put unique one into queue.
        if url_depth < int(parameter_dic['max_depth']):  # Set the condition of max spider depth.
            for sublink in sublink_list:
                if sublink not in unique_html_set:
                    # Send message into queue as producer.
                    unique_html_queue_para.put((sublink, int(url_depth)+1))
                    # Acquire the threading lock and change the unique set safely.
                    if lock.acquire():
                        unique_html_set.add(sublink)
                        lock.release()

        # Submit the task done to decrease the task count number.
        unique_html_queue_para.task_done()
