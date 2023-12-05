#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess

from unittest import TestCase

class day1a(TestCase):
    def test_example2(self):
        result = subprocess.check_output( \
            ['tclsh', 'day1/day1b.tcl', 'day1/example_input2.txt'], \
            stderr=subprocess.STDOUT).decode('utf-8')
        assert result == '281\n'

    def test_final(self):
        result = subprocess.check_output( \
            ['tclsh', 'day1/day1b.tcl', 'day1/my_input.txt'], \
            stderr=subprocess.STDOUT).decode('utf-8')
        assert result == '52834\n'
