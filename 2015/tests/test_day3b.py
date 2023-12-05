#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import adventofcode.day3b
import pytest

from unittest import TestCase

class day3b(TestCase):
    @pytest.fixture(autouse=True)
    def capsys(self, capsys):
        self.capsys = capsys

    def test_example1(self):
        adventofcode.day3b.day3b('^v\n')
        out, _ = self.capsys.readouterr()
        assert out == '3\n'

    def test_example2(self):
        adventofcode.day3b.day3b('^>v<\n')
        out, _ = self.capsys.readouterr()
        assert out == '3\n'

    def test_example3(self):
        adventofcode.day3b.day3b('^v^v^v^v^v\n')
        out, _ = self.capsys.readouterr()
        assert out == '11\n'

    def test_final(self):
        adventofcode.day3b.day3b(open('day3.txt', 'r').read())
        out, _ = self.capsys.readouterr()
        assert out == '2341\n'
