#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess

from unittest import TestCase

class day4a(TestCase):
    def test_example1(self):
        result = subprocess.check_output( \
            ['tclsh', 'day4/day4a.tcl', 'day4/example_input1.txt'], \
            stderr=subprocess.STDOUT).decode('utf-8')
        assert result == '13\n'

    def test_final(self):
        result = subprocess.check_output( \
            ['tclsh', 'day4/day4a.tcl', 'day4/my_input.txt'], \
            stderr=subprocess.STDOUT).decode('utf-8')
        assert result == '25231\n'
