#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import adventofcode.day2b
import pytest

from unittest import TestCase

class day2b(TestCase):
    @pytest.fixture(autouse=True)
    def capsys(self, capsys):
        self.capsys = capsys

    def test_example1(self):
        adventofcode.day2b.day2b('2x3x4\n1x1x10\n')
        out, _ = self.capsys.readouterr()
        assert out == '48\n'

    def test_final(self):
        adventofcode.day2b.day2b(open('day2.txt', 'r').read())
        out, _ = self.capsys.readouterr()
        assert out == '3842356\n'
