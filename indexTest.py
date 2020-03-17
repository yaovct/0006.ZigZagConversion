from index import Solution
import unittest

class SolutionTest(unittest.TestCase):

  def test_convert1(self):
    my_test = Solution()
    msg = ["ABC","PAYPALISHIRING","PAYPALISHIRING","PAYPALISHIRING","abcbabcbb","bbbbb","pwwkew","dvdf","bbtablud","nfpdmpi","dfevdfg","jbpnbwwd","umvejcuuk","tmmzuxt","ohvhjdml","anviaj","yfsrsrpzuya"]
    row = [2,3,2,4,9,1,3,2,3,3,2,3,2,3,4,2,4]
    ans = ["ACB","PAHNAPLSIIGYIR","PYAIHRNAPLSIIG","PINALSIGYAHRPI","abcbabcbb","bbbbb","pewkww","ddvf","bbbaldtu","nmfdppi","dedgfvf","jbbnwdpw","uvjukmecu","tumzxmt","omhdlvjh","avanij","ypfrzssuary"]
    for i, m in enumerate(msg):
    	self.assertEqual(ans[i],my_test.convert(m,row[i]))
  
if __name__ == '__main__':
    unittest.main()