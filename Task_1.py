import logging as lg
lg.basicConfig(filename= 'task1.log', level=lg.INFO, format= '%(levelname)s %(asctime)s %(name)s %(message)s')
lg.info('creating a class')
class strg:
    lg.info('creating instructor and pointer to pass a data')
    def __init__(self,s):
        self.s = s
    lg.info('out of instructor')

    lg.info('creating a function')
    def extract_data(self):
        """this function is used to extract data"""
        lg.info('entering in a function')
        try:
            a = self.s[int(input()):int(input()):int(input())]
            lg.info('we getting a data %s', a)
            return a
        except Exception as e:
            lg.exception(e)
            lg.info('out of the function')
            lg.warning('make sure you have to pass a data as string')

    lg.info('entering for creation of reverse operation of string')
    def rev_str(self):
        """This function is used to get out of string in reverse direction"""
        lg.info('initialize of function')
        try:
            a = self.s[::-1]
            lg.info('out return %s', a)
            return a
        except Exception as e:
            lg.info(e)
            lg.warning('parsing a data only string format')

    lg.info('creating a function to get uppercase and split of it')
    def splt_upr(self):
        """this function in return get a capital format of individual word"""
        lg.info('enter to create a funciton')
        try:
            a = self.s.upper()
            b = a.split()
            lg.info('result in upper format and split of it %s', b)
            return b
        except Exception as e:
            lg.info(e)

    lg.info('entering to create lower function')
    def low(self):
        """this function is used to get lowercase of string"""
        lg.info('entering in function')
        try:
            a = self.s.lower()
            lg.info('result of lower case %s', a)
        except Exception as e:
            lg.exception(e)

    lg.info('entering to create capitalize funciton')
    def cap(self):
        """This funciton is used to make capitalize of string"""
        lg.info('entering in function')
        try:
            a = self.s.capitalize()
            lg.info('result of cap %s', a)
            return a
        except Exception as e:
            lg.info(e)

    lg.info('entering to create a function of expand tab')
    def extab(self):
        """This function is used to create expand tab"""
        lg.info('entering in function')
        try:
            a = self.s.expandtabs()
            lg.info('result of expand tab %s', a)
            return a
        except Exception as e:
            lg.exception(e)

    lg.info('entering to create a function of strip')
    def strp(self):
        """this helps to remove whitespaces"""
        lg.info('entering in function')
        try:
            a = self.s.strip()
            lg.info('result is here %s', a)
            return a
        except Exception as e:
            lg.exception(e)

    lg.info('enterign to create a function to remover lestside whitespaces')
    def lstrp(self):
        """removed left side whitespaces"""
        lg.info('entering in function')
        try:
            a = self.s.lstrip()
            lg.info('result of lstrp %s', a)
            return  a
        except Exception as e:
            lg.info(e)

    lg.info('entering to create a function to remove rightside space')
    def rstrp(self):
        """removed right side spaces"""
        lg.info('enterign in rstrp function')
        try:
            a = self.s.rstrip()
            lg.info('result of rstrp %s', a)
            return a
        except Exception as e:
            lg.info(e)

    lg.info('entering to create a function to replace a character in string with another character')
    def remv(self):
        """this remove a character with another one
        start  = character to remove
        end = replacement character"""
        lg.info('entering in a function')
        try:
            a = self.s.replace(input(),input())
            lg.info('result of remv %s', a)
            return a
        except Exception as e:
            lg.exception(e)

    lg.info('entering to create a center like function')
    def ctr(self):
        """this function return a string of length width"""
        lg.info(' entering in ctr function')
        try:
            a = self.s.center(int(input()), input())
            lg.info('result of ctr %s', a)
            return a
        except Exception as e:
            lg.info(e)
a = strg("this is My First Python programming class and i am learNING python string and its function")
b = strg('Ineuron\tis\tthe\tbest\tplatform\tto\tlearn\tdata\tscience.')
c = strg('    Ineuron     ')
d = strg('Ineuron')
