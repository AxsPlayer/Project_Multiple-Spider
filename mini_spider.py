# !/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#
# Copyright (c) 2017 Personal. All Rights Reserved
#
################################################################################
"""
Python code to crawl websites given configuration.

Authors: Daniel&
Date: 2017/12/10 12:49:06
"""
import argparse
import ConfigParser
import logging
import os
import sys
import time

from config import output_log
from config import read_config
from config import save_seed_html
from crawl_and_save_website import crawl_and_parse_website
from multiple_threads import create_threads


def main():
    """The main process to crawl the target websites."""
    # Set the code and input configuration.
    parser = argparse.ArgumentParser(description='This is a mini web spider.')
    parser.add_argument('-v', action='version', version='Mini spider 0.1')
    parser.add_argument('-c', required=True, help='The configuration of the website uri.')

    # Print help manual for system input.
    if len(sys.argv) == 0:
        parser.print_help()
        return 1

    # Create logger for debugging.
    output_log.init_log('./log/crawl_html')

    # Read and save configurations into dictionary.
    args = parser.parse_args()
    config_file_name = args.c
    # Catch the raised error from parse_config function.
    parameter_dictionary = read_config.parse_config(config_file_name)
    if parameter_dictionary == 1:
        logging.error('\nThe error occurs in read_config.py module.')
        return 1

    # Create queue and import seed html address into queue.
    try:
        url_list_file = parameter_dictionary['url_list_file']
    except KeyError as e:
        logging.error('\nThe caught error is:\nKeyError in parameter_dictionary '
                      'with %s.' % str(e.args))
        return 1
    unique_html_queue, unique_html_set = save_seed_html.save_seed_to_list(url_list_file)

    # Create output directory if not exist.
    try:
        if not os.path.exists(parameter_dictionary['output_directory']):
            os.mkdir(parameter_dictionary['output_directory'])
    except OSError as e:
        logging.error('\nThe caught error is:\nThe directory '
                      '%s is not existed.' % str(e.filename))
        return 1

    # Set and start multiple threads for crawling websites.
    threads_num = int(parameter_dictionary['thread_count'])
    start_time = time.time()
    logging.info('Start time is %s.' % start_time)
    spider_threads = create_threads.\
        ConsumerAndProducerThreads(unique_html_set, threads_num, unique_html_queue,
                                   crawl_and_parse_website.crawl_and_save_html,
                                   parameter_dictionary)
    spider_threads.start_threads()

    # Join the multiple threads until all the threads finish the task in queue,
    # meaning when the task count equals to zero.
    logging.info('\nThreads join.')
    unique_html_queue.join()

    # Record the running time.
    time_interval = time.time() - start_time
    logging.info('\nTime interval is %s seconds.' % time_interval)


if __name__ == "__main__":
    '''The main process to crawl the target websites.'''
    main()


