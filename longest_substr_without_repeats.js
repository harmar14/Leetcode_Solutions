/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    if (s.length == 0) return 0;
    if (s.trim().length == 0) return 1;
    let chars = new Map();
    let res = 0;
    let tmp = 0;
    let i = 0;
    while (i != s.length) {
        if (!chars.has(s[i])) {
            chars.set(s[i], i);
            tmp++;
            i++;
        } else {
            if (tmp > res) res = tmp;
            tmp = 0;
            i = chars.get(s[i]) + 1;
            chars = new Map();
        }
    }
    if (tmp > res) res = tmp;
    return res;
};
