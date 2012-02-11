import mock
import sys
import pip2.commands.freeze
import pip2.cli_wrapper
import distutils2.database as packaging
from io import StringIO


class testFreezeAPI():
    
    #save the orginal command
    original = packaging.get_distributions   
    
    #creates the magicmock object and patches it to
    #the get_distributions function
    def setup(self):
        #magic mock the get_distributions generator
        get_dists = mock.MagicMock()
        #hook it in
        pip2.commands.freeze.get_distributions = get_dists
        return get_dists
    
    #replace the magicmock object with the original command
    def tear_down(self):
        pip2.commands.freeze.get_distributions = self.original
    
    #can't patch because we need a magiMock object for the generator
    def test_freeze_return_dist_iter(self):
        get_dists = self.setup()
    
        #create the ind. distributions that the gen will return
        dis1 = mock.Mock()
        dis1.name = 'test_package1'
        dis2 = mock.Mock()
        dis2.name = 'test_package2'
        dis3 = mock.Mock()
        dis3.name = 'test_package3'
        
        #get_distributions gen returns a iterator over distributions objects
        get_dists.return_value = [dis1, dis2, dis3]
        
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
        finally:
            #clean up
            self.tear_down()
            
class testFreezeCLI():
    
    originalOut = sys.stdout
    originalCmd = pip2.commands.freeze.freeze
    
    #capture stdout and replace freeze command with mock object
    def setup(self):
        sys.stdout = result = StringIO() 
        freeze = mock.Mock()
        pip2.commands.freeze.freeze = freeze
        return result, freeze
    
    #replace stdout and freeze cmd with orignal values
    def tear_down(self):
        sys.stdout = self.originalOut
        pip2.commands.freeze.freeze = self.originalCmd
    
    def test_freeze_correct_output(self):
        result, freeze = self.setup()
        
        #This is what the freeze API command should return
        freeze.return_value = ['test_package1', 'test_package2', 'test_package3']        
        
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


        
        

        
        
