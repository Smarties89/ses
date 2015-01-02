#!/usr/bin/python
# coding: utf-8
import unittest
import imp

ses = imp.load_source("ses", "ses")

# Loading testscript as text, to see later matches.
with open("repo/testscript", "r") as f:
    testscript = f.read()

class TesthttpdownloadFunction(unittest.TestCase):
    """ this test requires runrepo.bash is running. """

    def test_fileexists(self):
        snippet = ses.httpdownload("http://localhost:6005/testscript")
        self.assertEqual(snippet, testscript)

    def test_filenotexist(self):
        snippet = ses.httpdownload("http://localhost:6005/notexisting")
        self.assertEqual(snippet, None)
