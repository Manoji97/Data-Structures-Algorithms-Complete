const SumRange = (num) => {
  if (num === 0) return 0;
  return num + SumRange(num - 1);
};

const Factorial = (num) => {
  if (num === 1) return 1;
  return num * Factorial(num - 1);
};

const HelperOuterFunction = (arr) => {
  const outArr = [];
  const GetAllODDs = (arr) => {
    if (arr.length === 0) return;
    if (arr[0] % 2 !== 0) outArr.push(arr[0]);
    GetAllODDs(arr.splice(1));
  };
  GetAllODDs(arr);
  return outArr;
};

//Collect all Odd Values without using helper and return the new array

const CollectAllOdd = (arr) => {
  let outArr = [];
  if (arr.length === 0) return outArr;
  if (arr[0] % 2 !== 0) outArr.push(arr[0]);
  outArr = outArr.concat(CollectAllOdd(arr.splice(1)));
  return outArr;
};

console.log(SumRange(10));
console.log(Factorial(3));
console.log(HelperOuterFunction([1, 2, 3, 4, 5, 6, 7]));
console.log(CollectAllOdd([1, 2, 3, 4, 5, 6, 8, 8, 9]));
