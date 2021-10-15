#from mrjob.job import MRJob
#Create a class called Bacon_count, which inherits, or takes properties, from the MRJob class. We create this class to be called to run the full MapReduce job withMRJob:

#class Bacon_count(MRJob):

#Next, create a mapper()function that will take (self, _, line) as parameters. The mapper() function will assign the input to key-value pairs:
#def mapper(self, _, line):
#The second parameter (here using an underscore (_), explained next) allows methods to be mapped together. 
#Since we are not chaining anything together, we use the Python convention of an underscore to indicate that we won’t use this parameter. The line parameter will be the line of text taken from the raw input file.

#Use the code to Yield functions
from mrjob.job import MRJob
class Bacon_count(MRJob):
   def mapper(self, _, line):
       for word in line.split():
           if word.lower() == "bacon":
               yield "bacon", 1

   def reducer(self, key, values):
       yield key, sum(values)
if __name__ == "__main__":
   Bacon_count.run()

#The mrjob library works by reading in a file passed to it in the terminal.

