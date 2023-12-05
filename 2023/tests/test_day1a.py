#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess

from unittest import TestCase

class day1a(TestCase):
    def test_example1(self):
        result = subprocess.check_output( \
            ['tclsh', 'day1/day1a.tcl', 'day1/example_input1.txt'], \
            stderr=subprocess.STDOUT).decode('utf-8')
        assert result == '142\n'

    def test_final(self):
        result = subprocess.check_output( \
            ['tclsh', 'day1/day1a.tcl', 'day1/my_input.txt'], \
            stderr=subprocess.STDOUT).decode('utf-8')
        assert result == '53334\n'
