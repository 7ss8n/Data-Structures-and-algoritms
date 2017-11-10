#Implementation of the StudentFile Reader ADT using a text file as the 
#input source in which each field is stored on a separate line.

class StudentFileReader:
    #Create a new student reader instance.
    def __init__(self,inputSrc):
        self.__inputSrc=inputSrc
        self.__inputFile=None
    
    #Open a connection to the input file.
    def open(self):
        self.__inputFile=open(self._inputSrc,"r")
        
    #Close a connection to the input file.
    def close(self):
        self._inputFile.close()
        self._inputFile=None
    #Extract all studetn records and store them in a list.
    def fetchAll(self):
        theRecords=list()
        student=self.fetchRecord()
        while student!=None:
            theRecords.append(student)
            student=self.fetchRecord()
            while student!=None:
                theRecords.append(student)
                student=self.fetchRecord()
            return theRecords
            
            #Extract the next student record from the file.
            def fetchRecord(self):
                #Read the first line of the recor.
                line=self._inputFile.readline()
                if line=='':
                    return None
                #if there is another record, create a storage object and fill it.
                student=StudentRecord()
                student.idNum=int(line)
                student.firstName=self._inputFile.readline().rstrip()
                student.lastName = self. _ inputFile.readline().rstrip()
                student.classCode = int( self. _ inputFile.readline() )
                student.gpa = float( self. _ inputFile.readline() )
                return student
        

# Storage class used for an individual student record.
class StudentRecord:
    def __init__(self):
        self.idNum=0
        self.firstName=None
        self.lastName=None
        self.classCode=0
        self.gpa=0.0
        