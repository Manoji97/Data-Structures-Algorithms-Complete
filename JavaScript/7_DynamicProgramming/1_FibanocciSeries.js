// Basic Recursion for Fib Series
//[1, 1, 2, 3 ...]
//Time Complexity => O(2^n)   =>  very bad
const Fib_Basic = (n) => {
  if (n <= 2) return 1;
  return Fib_Basic(n - 1) + Fib_Basic(n - 2);
};

// Fib Function with Memorisation
//Time Complexity => O(n)   =>  Good

const Fib_Memorzation = (n, memo = [0, 1, 1]) => {
  if (memo[n] !== undefined) return memo[n];
  memo[n] = Fib_Memorzation(n - 1, memo) + Fib_Memorzation(n - 2, memo);
  return memo[n];
};

// Fib Function with Tabularization
//Time Complexity => O(n)   =>  Good
//Better than Memorization when comparing Space Complexity

const Fib_Tabularization = (n) => {
  let fibList = [0, 1, 1];
  for (let i = 3; i <= n; i++) {
    fibList[i] = fibList[i - 1] + fibList[i - 2];
  }
  return fibList[n];
};

let val = 40;
console.log(Fib_Memorzation(val));
console.log(Fib_Tabularization(val));
console.log(Fib_Basic(val));
