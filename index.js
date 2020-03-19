function Index() {
}
// node index.js
/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
Index.prototype.convert = function(s, numRows) {
	
	if(numRows == 1 || s.length < numRows) return s;
	var t = [];
	var x = 0;
	var n = 2 * numRows - 2;
	for(var i=0; i<numRows; i++) {
		for(var j=0; j<s.length; j++) {
			var k = i + j * n;
			if(k < s.length) {
				t[x++] = s.charAt(k);
				if(i % (n/2) > 0 && i+j*n < (j+1)*n && k != (j+1)*n-i) {
					k = (j+1)*n-i;
					if(k < s.length) {
						t[x++] = s.charAt(k);
					} else {
						break;
					}
				}
			} else {
				break;
			}
		}
	}
  return t.join('');
};

//index = new Index();
//var msg = ["ABC","PAYPALISHIRING","PAYPALISHIRING","PAYPALISHIRING","abcbabcbb","bbbbb","pwwkew","dvdf","bbtablud","nfpdmpi","dfevdfg","jbpnbwwd","umvejcuuk","tmmzuxt","ohvhjdml","anviaj","yfsrsrpzuya"];
//var row = [2,3,2,4,9,1,3,2,3,3,2,3,2,3,4,2,4];
//var ans = ["ACB","PAHNAPLSIIGYIR","PYAIHRNAPLSIIG","PINALSIGYAHRPI","abcbabcbb","bbbbb","pewkww","ddvf","bbbaldtu","nmfdppi","dedgfvf","jbbnwdpw","uvjukmecu","tumzxmt","omhdlvjh","avanij","ypfrzssuary"];
//for(var i=0; i<msg.length; i++) {
//	console.log(index.convert(msg[i], row[i]));
//}

module.exports = Index;
