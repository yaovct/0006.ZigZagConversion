#include<stdio.h>
#include<stdlib.h>

#define MAX_STRING_SIZE 2048

char * convert(char * s, int numRows){

	int len = 0;
	char *p = s;
	while(*p++) len++;

	if(numRows == 1 || len < numRows) return s;
	char *t = (char *)malloc((len+1)*sizeof(char));
	p = t;
	int n = 2 * numRows - 2;
	
	for(int i=0; i<numRows; i++){
		for(int j=0; j<len; j++) {
			int k = i + j * n;
			if(k < len) {
				*p++ = s[k];
				if(i % (n/2) > 0 && i+j*n < (j+1)*n &&  k != (j+1)*n-i) {
					k = (j+1)*n-i;
					if(k < len) {
						*p++ = s[k];
					} else {
						break;
					}
				}
			} else {
				break;
			}
		}
	}
	*p = '\0';
  return t;
}

int main(int argc, char *argv[]) {

  char* msg[] = {"ABC","PAYPALISHIRING","PAYPALISHIRING","PAYPALISHIRING","abcbabcbb","bbbbb","pwwkew","dvdf","bbtablud","nfpdmpi","dfevdfg","jbpnbwwd","umvejcuuk","tmmzuxt","ohvhjdml","anviaj","yfsrsrpzuya"};
	int row[] = {2,3,2,4,9,1,3,2,3,3,2,3,2,3,4,2,4};
	char* ans[] = {"ACB","PAHNAPLSIIGYIR","PYAIHRNAPLSIIG","PINALSIGYAHRPI","abcbabcbb","bbbbb","pewkww","ddvf","bbbaldtu","nmfdppi","dedgfvf","jbbnwdpw","uvjukmecu","tumzxmt","omhdlvjh","avanij","ypfrzssuary"};
	for(int i=0; i<sizeof(msg)/sizeof(msg[0]); i++) {
		printf("%s => %s\n", convert(msg[i], row[i]), ans[i]);
	}
}