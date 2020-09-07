class HashTable {
  constructor(size) {
    this.keyMap = new Array(size);
  }

  hashFunction(key) {
    // Worst Hash Function
    key = key.toLowerCase(); //key is only lower case
    let hash = 0,
      value;
    let wierdPrime = 31;
    let hashLen = Math.min(key.length, 100);
    for (let i = 0; i < hashLen; i++) {
      value = key[i].charCodeAt(0) - 96;
      hash = (hash * wierdPrime + value) % this.keyMap.length;
    }
    return Math.abs(hash);
  }

  get(key) {
    let bucket = this.hashFunction(key);
    if (!this.keyMap[bucket]) return false;
    for (const key_val of this.keyMap[bucket]) {
      if (key_val[0] === key) return key_val;
    }
    return false;
  }

  set(key, val) {
    const toSet = this.get(key);
    if (toSet) {
      toSet[1] = val;
    } else {
      let bucket = this.hashFunction(key);
      if (!this.keyMap[bucket]) this.keyMap[bucket] = [];
      this.keyMap[bucket].push([key, val]);
    }
    return this;
  }

  getKeys() {
    let keys = [];
    for (const key_vals of this.keyMap) {
      if (!key_vals) continue;
      for (const key_val of key_vals) {
        if (!keys.includes(key_val[0])) keys.push(key_val[0]); // Will Return only Unique Keys
      }
    }
    return keys;
  }

  getValues() {
    let values = [];
    for (const key_vals of this.keyMap) {
      if (!key_vals) continue;
      for (const key_val of key_vals) {
        if (!values.includes(key_val[1])) values.push(key_val[1]); // Will Return only Unique Values
      }
    }
    return values;
  }
}

let Dict = new HashTable(13);
