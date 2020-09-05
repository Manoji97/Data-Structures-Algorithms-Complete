/*

AnaGram Challenge is to find whether 2 Input Strings has same letters with same Frequency each.

    Example 1   =>  "aaz",   "zaa"  => True

    Exapmle 2   =>   "anagram",  "aangra"  => False


    Time Complexity for the Provided Solution is O(n)
*/

const ValidAnagram = (str1, str2) => {
  let lookUp = {};
  if (str1.length !== str2.length) return false;
  for (const val of str1) {
    lookUp[val] = ++lookUp[val] || 1;
  }

  for (let i = 0; i < str2.length; i++) {
    const element = str2[i];
    if (!lookUp[element]) {
      // if value of key in lookup dict becomes 0 this will return false
      return false;
    } else {
      lookUp[element] -= 1;
    }
  }
  return true;
};

let a = "level";
let b = "elven";
console.log(ValidAnagram(a, b));
