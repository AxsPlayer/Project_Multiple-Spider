# !/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#
# Copyright (c) 2017 Personal. All Rights Reserved
#
################################################################################
"""
The file is designed to parse the configuration.

Authors: Daniel&
Date: 2017/12/10 12:49:06
"""
import ConfigParser
import logging


def parse_config(config_file_name):
    """Parse configuration.

    Parse the configuration file and save the parameters
    to dictionary.

    Args:
        config_file_name: The configuration file name.

    Returns:
        The dictionary containing parameters in configuration file.
        For example:

        {'crawl_interval': 3, 'target_url': '.*.(htm|html)$'}

    Raises:
        IOError: An error occurred when reading the configuration file.
        ConfigParser.MissingSectionHeaderError: An error occurred
            when the section string is not given in configuration file.
    """
    # Create config parser and read the file.
    try:
        config = ConfigParser.ConfigParser()
        config.read(config_file_name)
    except IOError as e:
        logging.error('\nThe caught error is:\n%s' % str(e.strerror))
        return 1
    except ConfigParser.MissingSectionHeaderError as e:
        logging.error('\nThe caught error is:\n%s.' % str(e.message))
        return 1

    # Read the file content and save parameters into dictionary.
    parameter_results = {}
    sections = config.sections()
    for section in sections:
        options = config.options(section)
        for option in options:
            parameter_results[option] = config.get(section, option)

    return parameter_results
