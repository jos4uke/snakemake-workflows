
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
                print(path, file=sys.stderr)
                return True
        return False

    def loadTestsFromFile(self, snakefile):
        testdir = os.path.join(os.path.dirname(snakefile), "test")
            
        yield TestWorkflow(snakefile, testdir)


class TestWorkflow(TestCase):
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
    print("test")
    nose.main(addplugins=[TestSnakefiles()])
