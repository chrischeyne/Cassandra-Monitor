import sys
sys.path.append("/opt/work/projects/web2py/applications/cass1/controllers/mydata")
import datatime
class MyData():
    def __init__(self):
        self.CASS_JMX = {}
        self.CASS_JMX['Nodetool_Threshold'] = 42
        self.CASS_JMX['JDK_VERSION'] = '1.6.27'
        self.CASS_JMX['CASSANDRA_VERSION'] = 0.86
        self.CASS_JMX['PYTHON_VERSION'] = '2.7.2'
        d = datetime.datetime()
        from gluon.tools import prettydate
        pd = prettydate(d,T)
        print pd 
        self.CASS_JMX['DATE'] = pd

    def mydict(self):
        return self.CASS_JMX
 
if __name__ == '__main__':
    data = MyData()
    myjmx = data.mydict()


    print myjmx

   
