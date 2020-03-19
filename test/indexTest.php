<?php
// cd ../; phpunit -c phpunit.xml
require_once('index.php');

class SolutionTest extends \PHPUnit_Framework_TestCase
{
  function testconvert1()
  {
    $f = new Solution;
    $msg = array("ABC","PAYPALISHIRING","PAYPALISHIRING","PAYPALISHIRING","abcbabcbb","bbbbb","pwwkew","dvdf","bbtablud","nfpdmpi","dfevdfg","jbpnbwwd","umvejcuuk","tmmzuxt","ohvhjdml","anviaj","yfsrsrpzuya");
    $row = array(2,3,2,4,9,1,3,2,3,3,2,3,2,3,4,2,4);
    $ans = array("ACB","PAHNAPLSIIGYIR","PYAIHRNAPLSIIG","PINALSIGYAHRPI","abcbabcbb","bbbbb","pewkww","ddvf","bbbaldtu","nmfdppi","dedgfvf","jbbnwdpw","uvjukmecu","tumzxmt","omhdlvjh","avanij","ypfrzssuary");
    
    for($i=0; $i<count($msg); $i++) {
    	$this->assertEquals($ans[$i], $f->convert($msg[$i], $row[$i]));
    }
  }
}
?>