import mock
import sys
import pip2.commands.freeze
import pip2.cli_wrapper
import distutils2.database 
from io import StringIO


@mock.patch.object(distutils2.database, 'get_distributions')
class TestFreezeAPI():
    
    def test_freeze_return_dist_iter(self, mock_gen):
    
        #create the ind. distributions that the gen will return
        dis1 = mock.Mock()
        dis1.name = 'test_package1'
        dis2 = mock.Mock()
        dis2.name = 'test_package2'
        dis3 = mock.Mock()
        dis3.name = 'test_package3'
        
        #get_distributions gen returns a iterator over distributions objects
        mock_gen.return_value = iter([dis1, dis2, dis3])
        
        #freeze type casts the iterator to a list before returning it
        expected = ['test_package1', 'test_package2', 'test_package3']
        
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

@mock.patch.object(pip2.commands.freeze, 'freeze')            
class TestFreezeCLI():
    
    originalOut = sys.stdout
    
    #capture stdout 
    def setup(self):
        sys.stdout = result = StringIO() 
        return result
    
    #replace stdout 
    def tear_down(self):
        sys.stdout = self.originalOut
    
    def test_freeze_correct_output(self, mock_func):
        result = self.setup()
        
        #This is what the freeze API command should return
        mock_func.return_value = ['test_package1', 'test_package2', 'test_package3']        
        
        #run the CLI freeze command
        pip2.cli_wrapper.freeze(None)
        
        #This is what the CLI wrapper should return
        expected = "test_package1\ntest_package2\ntest_package3\n"
        
        # compare the outputs
        try:
            assert result.getvalue() == expected
        # their different? print both
        except AssertionError:
            #print to stderr cause stdout hasn't been switched back (better practice anyways)
            print('result  : {0}'.format(result.getvalue()), file=sys.stderr)
            print('expected: {0}'.format(expected), file=sys.stderr)
            raise
        #return it to normal for next test
        finally:
            self.tear_down()


        
        

        
        
