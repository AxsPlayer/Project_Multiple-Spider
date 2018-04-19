# !/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#
# Copyright (c) 2017 Personal. All Rights Reserved
#
################################################################################
"""
The file is designed for unit test.

Authors: Daniel&
Date: 2017/12/10 12:49:06
"""
import logging
import os
import unittest

from config import output_log
from config import read_config
from crawl_and_save_website import crawl_and_parse_website
from crawl_and_save_website import save_html_into_file


class TestSpider(unittest.TestCase):
    """Test the functions in mini spider.

    Test the separate modules's function imported in mini_spider.py.

    Attributes:
        config_file_name: The file address to read the configuration file.
        log_file = The log file address to save the log info.
    """
    def __init__(self, *args, **kwargs):
        """Init the test class with all the attributes."""
        super(TestSpider, self).__init__(*args, **kwargs)
        self.config_file_name = '../config/spider.conf'
        self.log_file = './log/test'

    def test_read_config(self):
        """Test the module 'read_config.py'.

        Returns: Boolean.
        """
        # Import the logger.
        output_log.init_log(self.log_file)
        # Import parameter_dictionary.
        parameter_dictionary = read_config.parse_config(self.config_file_name)

        # Test results.
        self.assertTrue('thread_count' in parameter_dictionary.keys())

    def test_save_html_into_file(self):
        """Test the module 'save_html_into_file.py'.

        Returns: Boolean.
        """
        # Import the logger.
        output_log.init_log(self.log_file)
        # Import parameter_dictionary.
        parameter_dictionary = read_config.parse_config(self.config_file_name)

        # Execute the function.
        save_html_into_file.save_html_to_file('test_file.html', 'This is the test content.',
                                              '1', **parameter_dictionary)
        target_address = parameter_dictionary['output_directory'] + '/' + \
            'test_file.html'.replace('/', '_').replace(':', '-')

        # Test results.
        self.assertTrue(os.path.exists(target_address))

    def test_output_log(self):
        """Test the module 'output_log.py'.

        Returns: Boolean.
        """
        # Import the logger.
        output_log.init_log(self.log_file)

        # Execute the function.
        log_address = '%s.log' % self.log_file
        logging.info('Here is the INFO information.')

        # Test results.
        self.assertTrue(os.path.exists(log_address))

    def test_crawl_and_parse_website(self):
        """Test the module 'crawl_and_parse_website.py'.

        Returns: Boolean.
        """
        # Import the logger.
        output_log.init_log(self.log_file)
        # Import parameter_dictionary.
        parameter_dictionary = read_config.parse_config(self.config_file_name)

        # Execute the function.
        html_address = 'https://www.cnblogs.com/buptzym/p/6933868.html'
        sublink_list, html_content = crawl_and_parse_website.\
            save_sublinks_to_queue(html_address, **parameter_dictionary)

        # Test results.
        self.assertTrue(len(sublink_list) != 0)
        self.assertTrue(html_content != 'e.code')
        self.assertTrue(html_content != '')


if __name__ == "__main__":
    # Use 'python -m unittest mini_spider_test' in console for unit test.
    unittest.main()
