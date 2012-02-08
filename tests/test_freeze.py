import mock
import pip2.commands.freeze

class testFreezeAPI():
    
    #should be a magicmock object that is passed in
    @mock.patch.object(pip2.commands.freeze, 'get_distributions')
    def test_freeze_return_dis_iter(self, mock_iter):
        #mock object for generator function that yields all installed dists.
        assert isinstance(mock_iter, mock.MagicMock)
        get_distributions = mock_iter.iter.return_value
        #mock object for the distribution list 
        #used to populate the generator
        dis1 = mock()
        dis1.name = 'test_package1'
        dis2 = mock()
        dis2.name = 'test_package2'
        dis3 = mock()
        dis3.name = 'test_package3'
    
        distributions = [dis1, dis2, dis3]
        iterator = iter(distributions)
        get_distributions.__iter__.return_value = iterator
        
        expected = ['test_package1', 'test_package2', 'test_package3']
        
        result = pip2.commands.freeze.freeze()
        
        assert result == expected
        
        
