#!/bin/python
# coding: utf-8
import unittest
import imp
import os

ses = imp.load_source("ses", "ses")

testscript = """
import os

def ham():
    return os"""

failurescript = """
I am a failure"""

class TestBetterExec(unittest.TestCase):

    def test_betterexecokay(self):
        script = ses.betterexec(testscript)
        self.assertEqual(hasattr(script, "ham"), True)
        # This tests to see if we can use modules inside the testscript.
        # The reason for this test, is that normal exec will not work 
        # with this.
        self.assertEqual(script.ham(), os)

    def test_betterexecexceptions(self):
        # Betterexec should just propagonate exceptions up, without
        # catching them.
        self.assertRaises(SyntaxError, ses.betterexec, failurescript)

