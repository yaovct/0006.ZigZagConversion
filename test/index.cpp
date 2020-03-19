#include "index.h"

string Solution::convert(string s, int numRows) {
	if(numRows == 1 || s.size() < numRows){
		return s;
	}
	string t;
	int x = 0;
	int n = 2 * numRows - 2;
	for(int i=0; i<numRows; i++){
		for(int j=0; j<s.size(); j++) {
			int k = i + j * n;
			if(k < s.size()) {
				t += s[k];
				if(i % (n/2) > 0 && i+j*n < (j+1)*n &&  k != (j+1)*n-i) {
					k = (j+1)*n-i;
					if(k < s.size()) {
						t += s[k];
					} else {
						break;
					}
				}
			} else {
				break;
			}
		}
	}
  return t;
}

//int main(int argc, char *argv[]) {
//
//  Solution myClass;
//  
//	string msg[17] = {"ABC","PAYPALISHIRING","PAYPALISHIRING","PAYPALISHIRING","abcbabcbb","bbbbb","pwwkew","dvdf","bbtablud","nfpdmpi","dfevdfg","jbpnbwwd","umvejcuuk","tmmzuxt","ohvhjdml","anviaj","yfsrsrpzuya"};
//	int row[17] = {2,3,2,4,9,1,3,2,3,3,2,3,2,3,4,2,4};
//	string ans[17] = {"ACB","PAHNAPLSIIGYIR","PYAIHRNAPLSIIG","PINALSIGYAHRPI","abcbabcbb","bbbbb","pewkww","ddvf","bbbaldtu","nmfdppi","dedgfvf","jbbnwdpw","uvjukmecu","tumzxmt","omhdlvjh","avanij","ypfrzssuary"};
//	for(int i=0; i<sizeof(msg)/sizeof(msg[0]); i++) {
//		cout << myClass.convert(msg[i], row[i]) << " => " << ans[i] << endl;
//	}
//}