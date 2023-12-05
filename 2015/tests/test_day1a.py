#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import adventofcode.day1a
import pytest

from unittest import TestCase

class day1a(TestCase):
    @pytest.fixture(autouse=True)
    def capsys(self, capsys):
        self.capsys = capsys

    def test_example1(self):
        adventofcode.day1a.day1a('(())')
        out, _ = self.capsys.readouterr()
        assert out == '0\n'

    def test_example2(self):
        adventofcode.day1a.day1a('()()')
        out, _ = self.capsys.readouterr()
        assert out == '0\n'

    def test_example3(self):
        adventofcode.day1a.day1a('(((')
        out, _ = self.capsys.readouterr()
        assert out == '3\n'

    def test_example4(self):
        adventofcode.day1a.day1a('(()(()(')
        out, _ = self.capsys.readouterr()
        assert out == '3\n'

    def test_example5(self):
        adventofcode.day1a.day1a('))(((((')
        out, _ = self.capsys.readouterr()
        assert out == '3\n'

    def test_example6(self):
        adventofcode.day1a.day1a('())')
        out, _ = self.capsys.readouterr()
        assert out == '-1\n'

    def test_example7(self):
        adventofcode.day1a.day1a('))(')
        out, _ = self.capsys.readouterr()
        assert out == '-1\n'

    def test_example8(self):
        adventofcode.day1a.day1a(')))')
        out, _ = self.capsys.readouterr()
        assert out == '-3\n'

    def test_example9(self):
        adventofcode.day1a.day1a(')())())')
        out, _ = self.capsys.readouterr()
        assert out == '-3\n'

    def test_final(self):
        adventofcode.day1a.day1a(open('day1.txt', 'r').read())
        out, _ = self.capsys.readouterr()
        assert out == '232\n'
