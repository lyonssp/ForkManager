import posix,sys,os,pprint

pp = pprint.PrettyPrinter(indent=4)
pp_err = pprint.PrettyPrinter(indent=4,stream=sys.stderr)

class ForkManager():

    ###PUBLIC###
    def onStart(self,func):
        self.onStartFunc = func

    def onFinish(self,func):
        self.onFinishFunc = func

    def start(self):
        if self.__parent_pid__ == os.getpid():
            pid = posix.fork()
        else:
            pid = 0

        self.__this_pid__ = os.getpid()
        if pid: #TODO check existence of start function
            try:
                self.__runOnStartFunc__( self.__this_pid__ )
            except Exception as e:
                pp_err.pprint( e )
        return pid
    
    def finish(self):
        try:
            self.__runOnFinishFunc__( self.__this_pid__ )
        except Exception as e:
            pp_err.pprint( e )
        sys.exit()

    def isParent(self):
        return self.__parent_pid__ == self.__this_pid__
    
    def isChild(self):
        return self.__parent_pid__ != self.__this_pid__
   
    ###PRIVATE### 
    __parent_pid__ = os.getpid()

    def __runOnStartFunc__(self,pid):
        self.onStartFunc(pid)
        
    def __runOnFinishFunc__(self,pid):
        self.onFinishFunc(pid)

