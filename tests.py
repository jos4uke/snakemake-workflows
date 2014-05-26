#!/usr/bin/env python3
# vim: syntax=python tabstop=4 expandtab
# coding: utf-8


"""
Executes test cases for all workflows that contain a "test" directory.
"""


__author__ = "Johannes Köster (http://johanneskoester.bitbucket.org)"
__license__ = "MIT"


import nose
import sys, os
from nose.plugins import Plugin
from unittest import TestCase
from snakemake import snakemake


class TestSnakefiles(Plugin):
    enabled=True
    
    def configure(self, options, conf):
        pass

    def wantDirectory(self, path):
        return True

    def wantFile(self, path):
        head, tail = os.path.split(path)
        if tail == "Snakefile":
            if os.path.exists(os.path.join(head, "test")):
                return True
        return False

    def loadTestsFromFile(self, snakefile):
        testdir = os.path.join(os.path.dirname(snakefile), "test")
            
        yield WorkflowTest(snakefile, testdir)


class WorkflowTest(TestCase):
    def __init__(self, snakefile, testdir):
        self.snakefile = snakefile
        self.testdir = testdir
        self._testMethodName = os.path.basename(os.path.dirname(snakefile))

    def run(self, result):
        result.startTest(self)
        if snakemake(self.snakefile, dryrun=True, workdir=self.testdir):
            result.addSuccess(self)
        else:
            result.addFailure(self, "")
        result.stopTest(self)


if __name__ == "__main__":
    nose.main(addplugins=[TestSnakefiles()])
