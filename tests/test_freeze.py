import mock, sys, inspect
import pip2.commands.freeze
import pip2.cli_wrapper
import packaging.database 
from io import StringIO

@mock.patch.object(packaging.database, 'get_distributions')
class TestFreezeAPI():
    
    def test_basic_freeze(self, mock_gen):
    
        #create the ind. distributions that the gen will return
        dis1 = mock.Mock()
        dis1.name = 'test_package1'
        dis2 = mock.Mock()
        dis2.name = 'test_package2'
        dis3 = mock.Mock()
        dis3.name = 'test_package3'
        
        #get_distributions gen returns a iterator over distributions objects
        mock_gen.return_value = iter([dis1, dis2, dis3])
        
        #freeze returns a dictionary with name as key and misc. info (based on options) in 
        # sub dict.
        expected = {'test_package1':{}, 'test_package2':{}, 'test_package3':{}}
        
        #run the command
        result = pip2.commands.freeze.freeze()

        #compare the two
        try:
            assert result == expected
        #not the same? print out both lists
        except AssertionError:
            print('result  : {0}'.format(result))
            print('expected: {0}'.format(expected))
            raise
        
        
    def test_freeze_version(self, mock_gen):
        
        #create the ind. distributions that the gen will return
        dis1 = mock.Mock()
        dis1.name = 'test_package1'
        dis1.version = 1.0
        dis2 = mock.Mock()
        dis2.name = 'test_package2'
        dis2.version = 2.0
        dis3 = mock.Mock()
        dis3.name = 'test_package3'
        dis3.version = 3.0
        
        #get_distributions gen returns a iterator over distributions objects
        mock_gen.return_value = iter([dis1, dis2, dis3])
        
        expected = {'test_package1':{'version':1.0}, 'test_package2':{'version':2.0}, 'test_package3':{'version':3.0}}
        
        # run the command
        result = pip2.commands.freeze.freeze(version = True)
        
        #compare the two
        try:
            assert result == expected
        #not the same? print out both lists
        except AssertionError:
            print('result  : {0}'.format(result))
            print('expected: {0}'.format(expected))
            raise
        

@mock.patch.object(pip2.commands.freeze, 'freeze')            
class TestFreezeCLI():
    originalOut = sys.stdout
    
    #capture stdout 
    def setup(self):
        sys.stdout = result = StringIO() 
        return result
    
    
    def test_basic_freeze(self, mock_func):
        args = mock.Mock()
        args.version = False
        
        result = self.setup()
        
        #This is what the freeze API command should return
        mock_func.return_value = {'test_package1':{}, 'test_package2':{}, 'test_package3':{}}        
        
        #run the CLI freeze command
        pip2.cli_wrapper.freeze(args)
        
        #This is what the CLI wrapper should return
        expected = "test_package1\ntest_package2\ntest_package3\n"
        
        # compare the outputs
        self.tear_down(result.getvalue(), expected)
            
            
    def test_freeze_version(self, mock_func):
        args = mock.Mock()
        args.version = True
        
        result = self.setup()
        
        mock_func.return_value = {'test_package1':{'version':1.0}, 'test_package2':{'version':2.0}, 'test_package3':{'version':3.0}}
        
        pip2.cli_wrapper.freeze(args)
        
        expected = '{0:<30}1.0\n{1:<30}2.0\n{2:<30}3.0\n'.format('test_package1', 'test_package2', 'test_package3')
        
        self.tear_down(result.getvalue(), expected)
            
            
    def tear_down(self, result, expected):
        # compare the outputs
        try:
            assert result == expected
        # their different? print both
        except AssertionError:
            result = result.replace('\n', '\\n')
            expected = expected.replace('\n', '\\n')
            output = ("\n\nTEST FAILED" +
                      "\nFunction: {0}".format(inspect.stack()[1][3]) +
                      "\nResult  : {0}\n".format(result) +
                      "\nExpected: {0}".format(expected))
            #print to stderr cause stdout hasn't been switched back (better practice anyways)
            print(output, file=sys.stderr)
            raise
        #return it to normal for next test
        finally:
            sys.stdout = self.originalOut


        
        

        
        
