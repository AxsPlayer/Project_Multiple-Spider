# !/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#
# Copyright (c) 2017 Personal. All Rights Reserved
#
################################################################################
"""
The file is designed to save html to file.

Authors: AxsPlayer
Date: 2017/12/10 12:49:06
"""
import logging
import re
import threading


def save_html_to_file(html_name, html_content, url_depth, **parameter_dictionary):
    """Save html into file.

    Crawl the target html content and save html content to .html file.

    Args:
        html_name: The file name of saved html.
        html_content: The file content of saved html.
        url_depth: The current depth of html address corresponding to seed uri.
        parameter_dictionary: The dictionary which contains
            the necessary parameters in configuration file.

    Returns:
        None.

        Save the satisfying html's content into files.

    Raises:
        IOError: An error occurred when create and open html files.
        OSError: Fail to create output directory.
    """

    # Check the target html's pattern and save the satisfying html content into file.
    pattern = parameter_dictionary['target_url']
    match_result = re.match(pattern, html_name)
    logging.info('\n[%s] The crawled url is %s, threading %s is running.' %
                 (url_depth, html_name, threading.current_thread().name))
    if match_result:
        logging.info('Matches!')
        target_address = parameter_dictionary['output_directory'] + \
            '/' + html_name.replace('/', '_').replace(':', '-') + '.html'
        try:
            with open(target_address, 'wb') as f:
                f.write(html_content)
        except IOError as e:
            logging.warning('\nThe caught error is:%s' % e.strerror)


