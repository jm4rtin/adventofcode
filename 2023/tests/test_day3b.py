#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess

from unittest import TestCase

class day3a(TestCase):
    def test_example2(self):
        result = subprocess.check_output( \
            ['tclsh', 'day3/day3b.tcl', 'day3/example_input1.txt'], \
            stderr=subprocess.STDOUT).decode('utf-8')
        assert result == '467835\n'

    def test_final(self):
        result = subprocess.check_output( \
            ['tclsh', 'day3/day3b.tcl', 'day3/my_input.txt'], \
            stderr=subprocess.STDOUT).decode('utf-8')
        assert result == '84399773\n'
