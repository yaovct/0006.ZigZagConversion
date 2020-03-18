// put source in src/Solution.java
// put test in test/SolutionTest.java
package src;
import java.lang.*;
import java.util.*;

public class Solution {
  public String convert(String s, int numRows) {
  	char[] dic = new char[s.length()];
  	if(numRows == 1 || s.length() < numRows) {
  		return s;
  	}
  	int x = 0;
  	int n = 2 * numRows - 2;
  	for(int i=0; i<numRows; i++) {
  		for(int j=0; j<s.length(); j++) {
  			int k = i + j * n;
  			if(k < s.length()) {
  				dic[x++] = s.charAt(k);
  				if((i % (n/2) > 0) && (i+j*n < (j+1)*n) && (k != (j+1)*n-i)) {
  					k = (j+1)*n - i;
  					if(k < s.length()) {
  						dic[x++] = s.charAt(k);
  					} else {
  						break;
  					}
  				}
  			} else {
  				break;
  			}
  		}
  	}
  	return new String(dic);
  }
}
