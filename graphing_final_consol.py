from multiprocessing import Process
from graphWriter2_dir_manage import *
#from baselineMain import *

def main():
    for line in directory():
        try: Process(target = graphWriterIRI())
        except IOError:
            print''
            print'No IRI data available'
            pass
        try: Process(target = graphWriterRut())
        except IOError:
            print''
            print'No RUT data available'
            pass

if __name__ == "__main__":
    main()
    
