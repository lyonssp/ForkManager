import sys,os,unittest
sys.path.append('../')

from time import sleep
from ForkManager import ForkManager
from mock import patch , ANY


fm = ForkManager()
def onStartFunc(pid):
    return

def onFinishFunc(pid):
    return

fm.onStart( 
    onStartFunc
)
fm.onFinish(
    onFinishFunc
)

class TestForkManagerModule( unittest.TestCase):
    
    #Test that start() returns the correct process id to parent and child
    def testStartup(self):
        with patch.object( ForkManager , '__runOnStartFunc__' ) as onStart:
            pid = fm.start()

        if not pid:
            with self.assertRaises(SystemExit):
                fm.finish()
        else:
            onStart.assert_called_once_with(ANY)
    
    #Test that finish() ends the child process like it should
    def testFinish(self):
        pid = fm.start()
        if not pid:
            with self.assertRaises(SystemExit):
                fm.finish()
                self.assertTrue(False) #should not get here

    #Test that isParent and isChild work 
    #correctly in both parent and child proc
    def testParentChildChecks(self):
        pid = fm.start()
        if pid:
            self.assertTrue( fm.isParent() )
            self.assertFalse( fm.isChild() )
        else:
            self.assertTrue( fm.isChild() )
            self.assertFalse( fm.isParent() )
            with self.assertRaises(SystemExit):
                fm.finish()

if __name__ == '__main__':
    unittest.main()
