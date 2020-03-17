class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # Observation:
        # First to judge i in L1/L2/L3/...
        # if i in L3, i = sum(L1, L2) + L3(i)
        # For nR = 2, L1 = i/2 + 1, L2 = (i-1)/2 + 1,
        # For nR = 3, L1 = i/4 + 1, L2 = (i-1)/2 + 1, L3 = (i-2)/4 + 1
        # L1: 0, 1*[nR+(nR-2)], 2*[nR+(nR-2)], 3*[nR+(nR-2)]
        # L2: 1, 1*[nR+(nR-2)]-1; 1*[nR+(nR-2)]+1, 2*[nR+(nR-2)]-1; 2*[nR+(nR-2)]+1, 3*[nR+(nR-2)]-1;
        t = []
        if numRows == 1 or len(s) < numRows:
        	return s
        for i in range(0, numRows):
        	for j in range(0, len(s)):
        		k = i + j*(numRows+numRows-2)
        		if k < len(s):
        			t.append(s[k])
        			#print("%d %c" % (k,s[k]))
        			if i % ((numRows+numRows-2)/2) and \
        			 i + j*(numRows+numRows-2) < (j+1)*(numRows+numRows-2) and \
        			 k != (j+1)*(numRows+numRows-2) - i:
        				k = (j+1)*(numRows+numRows-2) - i
        				if k < len(s):
        					t.append(s[k])
        					#print("%d %c" % (k,s[k]))
        				else:
        					break
        		else:
        			break
        return ''.join(t)
        				
#        for i in range(0, numRows):
#        	if i % ((numRows+numRows-2)/2) == 0:
#        		for j in range(0, len(s)/numRows):
#        			k = i + j*(numRows+numRows-2)
#        			if k < len(s):
#        				t.append(s[k])
#        				print("%d %c" % (k,s[k]))
#        	else:
#        		for j in range(0, len(s)/numRows):
#        			if i + j*(numRows+numRows-2) < (j+1)*(numRows+numRows-2):
#        				k = i + j*(numRows+numRows-2)
#        				if k < len(s):
#	        				t.append(s[k])
#	        				print("%d %c" % (k,s[k]))
#	      				if k != (j+1)*(numRows+numRows-2) - i:
#	      					k = (j+1)*(numRows+numRows-2) - i
#	      					if k < len(s):
#	        					t.append(s[k])
#	        					print("%d %c" % (k,s[k]))
#        return ''.join(t)

my_test = Solution()
msg = ["ABC","PAYPALISHIRING","PAYPALISHIRING","PAYPALISHIRING","abcbabcbb","bbbbb","pwwkew","dvdf","bbtablud","nfpdmpi","dfevdfg","jbpnbwwd","umvejcuuk","tmmzuxt","ohvhjdml","anviaj","yfsrsrpzuya"]
row = [2,3,2,4,9,1,3,2,3,3,2,3,2,3,4,2,4]
#  "ACB","PAHNAPLSIIGYIR","PYAIHRNGAPLSIIG","PINALSIGYAHRPI"

for i, m in enumerate(msg):
	print("%s, %d = %s" % (m,row[i],my_test.convert(m,row[i])))
    	