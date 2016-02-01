#naics.py
from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import cPickle as pickle
from process import Process


class Naics2text(Process):
    # Class to Deconstruct AICS Description PDF to its subsequent parts
    def __init__(self):
        self.fname = None
        self.location = None
        print "Trying to import PDF"
        if self.fname == '':
            raise IOError("You need to enter a vaild PDF file!,\n"
                          "ex pdf = Naics2text()")
        self.location = 'pickle/{0}.p'.format(self.fname)

    def convert(self, fname='', pages=None):
        print "Trying to import PDF"
        if self.fname == '':
            raise IOError("You need to enter a vaild PDF file!,\n"
                          "ex pdf.convert('example.pdf')")
        self.location = 'pickle/{0}.p'.format(self.fname)
        print "We are processing your PDF >>>>>>>>>>>>"
        if not pages:
            pagenums = set()
        else:
            pagenums = set(pages)

        output = StringIO()
        manager = PDFResourceManager()
        converter = TextConverter(manager, output, laparams=LAParams())
        interpreter = PDFPageInterpreter(manager, converter)

        infile = file(self.fname, 'rb')
        for page in PDFPage.get_pages(infile, pagenums):
            interpreter.process_page(page)
        infile.close()
        converter.close()
        text = output.getvalue()
        output.close
        msg = 'Pickled File Location is "{0}"'.format(self.location)
        pickle.dump(text, open(self.location, 'wb'))
        return msg
