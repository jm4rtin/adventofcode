#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import adventofcode.day1b
import pytest

from unittest import TestCase

class day1b(TestCase):
    @pytest.fixture(autouse=True)
    def capsys(self, capsys):
        self.capsys = capsys

    def test_example1(self):
        adventofcode.day1b.day1b(')')
        out, _ = self.capsys.readouterr()
        assert out == '1\n'

    def test_example2(self):
        adventofcode.day1b.day1b('()())')
        out, _ = self.capsys.readouterr()
        assert out == '5\n'

    def test_final(self):
        adventofcode.day1b.day1b(open('day1.txt', 'r').read())
        out, _ = self.capsys.readouterr()
        assert out == '1783\n'
