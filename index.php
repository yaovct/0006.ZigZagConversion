<?php

class Solution {

    /**
     * @param String $s
     * @param Integer $numRows
     * @return String
     */
    function convert($s, $numRows) {
  	$t = Array();
  	if($numRows == 1 || strlen($s) < $numRows) return $s;
  	$x = 0;
  	$n = 2 * $numRows - 2;
  	for($i=0; $i<$numRows; $i++) {
  		for($j=0; $j<strlen($s); $j++) {
  			$k = $i + $j * $n;
  			if($k < strlen($s)) {
  				$t[$x++] = $s[$k];
  				if($i % ($n/2) > 0 && $i+$j*$n < ($j+1)*$n && $k != ($j+1)*$n-$i) {
  					$k = ($j+1)*$n - $i;
  					if($k < strlen($s)) {
  						$t[$x++] = $s[$k];
  					} else {
  						break;
  					}
  				}
  			} else {
  				break;
  			}
  		}
  	}
  	return join($t);
  }
}
//$msg = array("ABC","PAYPALISHIRING","PAYPALISHIRING","PAYPALISHIRING","abcbabcbb","bbbbb","pwwkew","dvdf","bbtablud","nfpdmpi","dfevdfg","jbpnbwwd","umvejcuuk","tmmzuxt","ohvhjdml","anviaj","yfsrsrpzuya");
//$row = array(2,3,2,4,9,1,3,2,3,3,2,3,2,3,4,2,4);
//$testSolution = new Solution();
//for($i=0; $i<count($msg); $i++) {
//	printf("%s %d => %s\n",$msg[$i], $row[$i], $testSolution->convert($msg[$i], $row[$i]));
//}
?>