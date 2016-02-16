import posix,sys,os

class ForkManager():
    def onStart(self,func):
        self.onStartFunc = func

    def __runOnStartFunc__(self,pid):
        self.onStartFunc(pid)
        
    def onFinish(self,func):
        self.onFinishFunc = func

    def __runOnFinishFunc__(self,pid):
        self.onFinishFunc(pid)

    def start(self):
        pid = posix.fork()
        if pid: #TODO check existence of start function
            try:
                self.this_pid = os.getpid()
                self.__runOnStartFunc__( self.this_pid )
            except Exception:
                pass 
        return pid
    
    def finish(self):
        pid = os.getpid()
        try:
            self.onFinishFunc(pid)
        except Exception:
            pass
        sys.exit()
