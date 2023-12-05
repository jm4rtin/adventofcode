#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import adventofcode.day3a
import pytest

from unittest import TestCase

class day3a(TestCase):
    @pytest.fixture(autouse=True)
    def capsys(self, capsys):
        self.capsys = capsys

    def test_example1(self):
        adventofcode.day3a.day3a('>\n')
        out, _ = self.capsys.readouterr()
        assert out == '2\n'

    def test_example2(self):
        adventofcode.day3a.day3a('^>v<\n')
        out, _ = self.capsys.readouterr()
        assert out == '4\n'

    def test_example3(self):
        adventofcode.day3a.day3a('^v^v^v^v^v\n')
        out, _ = self.capsys.readouterr()
        assert out == '2\n'

    def test_final(self):
        adventofcode.day3a.day3a(open('day3.txt', 'r').read())
        out, _ = self.capsys.readouterr()
        assert out == '2081\n'
