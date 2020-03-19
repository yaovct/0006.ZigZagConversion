describe('convert', () => {
	var Index = require('../../index.js');
	var index;
  
  beforeEach(function() {
    index = new Index();
  });

  it("Ex1", function() {
  	var msg = ["ABC","PAYPALISHIRING","PAYPALISHIRING","PAYPALISHIRING","abcbabcbb","bbbbb","pwwkew","dvdf","bbtablud","nfpdmpi","dfevdfg","jbpnbwwd","umvejcuuk","tmmzuxt","ohvhjdml","anviaj","yfsrsrpzuya"];
		var row = [2,3,2,4,9,1,3,2,3,3,2,3,2,3,4,2,4];
		var ans = ["ACB","PAHNAPLSIIGYIR","PYAIHRNAPLSIIG","PINALSIGYAHRPI","abcbabcbb","bbbbb","pewkww","ddvf","bbbaldtu","nmfdppi","dedgfvf","jbbnwdpw","uvjukmecu","tumzxmt","omhdlvjh","avanij","ypfrzssuary"];
		for(var i=0; i<msg.length; i++) {
			expect(index.convert(msg[i], row[i])).toEqual(ans[i]);
		}
  });

});