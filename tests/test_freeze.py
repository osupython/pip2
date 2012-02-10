import mock
import pip2.commands.freeze

class testFreezeAPI():
    
    #can't patch because we need a magiMock object for the generator
    def test_freeze_return_dis_iter(self):
        #magic mock the get_distributions generator
        get_dists = mock.Mock()
        #hook it in
        pip2.commands.freeze.get_distributions = get_dists
    
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
        
        
