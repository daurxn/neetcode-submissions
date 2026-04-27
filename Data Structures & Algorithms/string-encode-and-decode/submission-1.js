class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        return strs.reduce((res, str) => res + `${str.length}#${str}`, '');
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        const res = []
        for (let i = 0; i < str.length; i++) {
            let j = i
            while (str[j] !== '#') j++

            const len = Number(str.substring(i, j))
            const substr = str.substring(j + 1, j + len + 1)
            res.push(substr)
            i = j + len
        }
        return res
    }
}
