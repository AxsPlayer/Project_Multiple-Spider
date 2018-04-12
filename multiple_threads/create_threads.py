# !/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#
# Copyright (c) 2017 Personal. All Rights Reserved
#
################################################################################
"""
The file is designed to create multiple threads.

Authors: Daniel&
Date: 2017/12/10 12:49:06
"""
import logging
import threading


class ConsumerAndProducerThreads(threading.Thread):
    """Multiple threads class for consumer and producer.

    Create the thread class to start consumer as well as producer function.

    Attributes:
        unique_html_set: The set to save unique html address.
        threads_num: The number of threads to run at the same time.
        unique_html_queue: The queue created in the main function to save html address
            from producer and send addresses to consumer for consumption.
        crawl_and_save_html: The main function to crawl the html addresses in the queue
            and save html addresses into files.
        parameter_dictionary: The dictionary which contains all the parameters.
        lock: Threading lock created to change the common variable safely.
    """
    def __init__(self, unique_html_set, threads_num, unique_html_queue,
                 crawl_and_save_html, parameter_dictionary):
        """Init the thread class with all the attributes."""
        threading.Thread.__init__(self)
        self.unique_html_set = unique_html_set
        self.threads_num = threads_num
        self.unique_html_queue = unique_html_queue
        self.crawl_and_save_html = crawl_and_save_html
        self.parameter_dictionary = parameter_dictionary
        self.lock = threading.Lock()

    def start_threads(self):
        """Start multiple threads for crawling function.

        Receive the threads number and start threads through local names.

        Returns:
            None.
        """
        # Create local namespace.
        names = locals()

        # Create threads according to threads num and start threads.
        for i in xrange(0, self.threads_num):
            names['t%s' % i] = threading.Thread(target=self.crawl_and_save_html,
                                                name='crawl_html_%s' % i,
                                                args=(self.unique_html_set, self.lock,
                                                      self.unique_html_queue),
                                                kwargs=self.parameter_dictionary)
            # Set true when the main thread ends, then kill the sub-threads.
            names['t%s' % i].setDaemon(True)
            logging.info('\nStart thread %s' % i)  # Record logs for threads beginning.
            names['t%s' % i].start()
