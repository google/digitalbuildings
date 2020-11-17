/**
* Swap endianness of 32bit numbers.
* @param {number} val 32 bit number to be swapped.
* @return {number} 32bit number in swapped endianness.
*/
function swap32(val) {
  return ((val & 0xFF) << 24) |
           ((val & 0xFF00) << 8) |
           ((val >> 8) & 0xFF00) |
           ((val >> 24) & 0xFF);
}

export {swap32};
