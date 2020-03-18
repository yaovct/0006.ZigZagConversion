import java.lang.*;
import java.util.*;

class Solution {
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

public class index {

	public static void main(String[] args) {
		String[] msg = new String[] {"ABC","PAYPALISHIRING","PAYPALISHIRING","PAYPALISHIRING","abcbabcbb","bbbbb","pwwkew","dvdf","bbtablud","nfpdmpi","dfevdfg","jbpnbwwd","umvejcuuk","tmmzuxt","ohvhjdml","anviaj","yfsrsrpzuya"};
		int[] row = {2,3,2,4,9,1,3,2,3,3,2,3,2,3,4,2,4};

    Solution demo = new Solution();
    for(int i=0; i<msg.length; i++) {
    	System.out.printf("%s, %d = %s\n", msg[i], row[i], demo.convert(msg[i],row[i]));
    }
	}
}