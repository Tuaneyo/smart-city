
export const CalculationServie = {
  mean,
  median,
  mode,
}

function mean(arr) {
  let total = 0;
  for (let i = 0; i < arr.length; i++) {
    total += arr[i];
  }
  return Math.floor(total / arr.length, 0);
};

function median(arr) {
  const { length } = arr;
  
  arr.sort((a, b) => a - b);
  
  if (length % 2 === 0) {
    return (arr[length / 2 - 1] + arr[length / 2]) / 2;
  }
  
  return Math.floor(arr[(length - 1) / 2], 0);
};

function mode(arr) {
  const mode = {};
  let max = 0, count = 0;

  for(let i = 0; i < arr.length; i++) {
    const item = arr[i];
    
    if(mode[item]) {
      mode[item]++;
    } else {
      mode[item] = 1;
    }
    
    if(count < mode[item]) {
      max = item;
      count = mode[item];
    }
  }
  
  return Math.floor(max, 0);
}