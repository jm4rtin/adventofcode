#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess

from unittest import TestCase

class day2a(TestCase):
    def test_example2(self):
        result = subprocess.check_output( \
            ['tclsh', 'day2/day2b.tcl', 'day2/example_input1.txt'], \
            stderr=subprocess.STDOUT).decode('utf-8')
        assert result == '2286\n'

    def test_final(self):
        result = subprocess.check_output( \
            ['tclsh', 'day2/day2b.tcl', 'day2/my_input.txt'], \
            stderr=subprocess.STDOUT).decode('utf-8')
        assert result == '70265\n'
