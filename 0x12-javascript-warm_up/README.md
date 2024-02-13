# 0x12. JavaScript - Warm up


---

# JavaScript Warm-up

This repository contains a set of JavaScript scripts designed to help you get familiar with basic JavaScript concepts. Each script serves a specific purpose, and the explanations are provided in simple terms for easy understanding.

## Task 0: First constant, first print

- **Objective**: Print the string "JavaScript is amazing" using a constant variable.
- **Script**: [0-javascript_is_amazing.js](0-javascript_is_amazing.js)

```javascript
#!/usr/bin/node

const myVar = "JavaScript is amazing";
console.log(myVar);
```

## Task 1: 3 languages

- **Objective**: Print three lines with different programming languages.
- **Script**: [1-multi_languages.js](1-multi_languages.js)

```javascript
#!/usr/bin/node

console.log("C is fun");
console.log("Python is cool");
console.log("JavaScript is amazing");
```

## Task 2: Arguments

- **Objective**: Print a message based on the number of arguments passed.
- **Script**: [2-arguments.js](2-arguments.js)

```javascript
#!/usr/bin/node

const argsCount = process.argv.length;
if (argsCount === 2) {
  console.log("No argument");
} else if (argsCount === 3) {
  console.log("Argument found");
} else {
  console.log("Arguments found");
}
```

## Task 3: Value of my argument

- **Objective**: Print the first argument passed to the script.
- **Script**: [3-value_argument.js](3-value_argument.js)

```javascript
#!/usr/bin/node

const firstArg = process.argv[2];
if (firstArg === undefined) {
  console.log("No argument");
} else {
  console.log(firstArg);
}
```

## Task 4: Create a sentence

- **Objective**: Print two arguments in the format " is ".
- **Script**: [4-concat.js](4-concat.js)

```javascript
#!/usr/bin/node

const arg1 = process.argv[2];
const arg2 = process.argv[3];

console.log(`${arg1} is ${arg2}`);
```

## Task 5: An Integer

- **Objective**: Print "My number: " followed by the first argument converted to an integer.
- **Script**: [5-to_integer.js](5-to_integer.js)

```javascript
#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log("Not a number");
} else {
  console.log(`My number: ${num}`);
}
```

## Task 6: Loop to languages

- **Objective**: Print three lines using an array of strings and a loop.
- **Script**: [6-multi_languages_loop.js](6-multi_languages_loop.js)

```javascript
#!/usr/bin/node

const languages = ["C is fun", "Python is cool", "JavaScript is amazing"];

for (const language of languages) {
  console.log(language);
}
```

## Task 7: I love C

- **Objective**: Print "C is fun" a specific number of times.
- **Script**: [7-multi_c.js](7-multi_c.js)

```javascript
#!/usr/bin/node

const occurrences = parseInt(process.argv[2]);

if (isNaN(occurrences) || occurrences <= 0) {
  console.log("Missing number of occurrences");
} else {
  for (let i = 0; i < occurrences; i++) {
    console.log("C is fun");
  }
}
```

## Task 8: Square

- **Objective**: Print a square using the character 'X'.
- **Script**: [8-square.js](8-square.js)

```javascript
#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (isNaN(size) || size <= 0) {
  console.log("Missing size");
} else {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
```

## Task 9: Add

- **Objective**: Print the addition of two integers.
- **Script**: [9-add.js](9-add.js)

```javascript
#!/usr/bin/node

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

if (isNaN(a) || isNaN(b)) {
  console.log("NaN");
} else {
  console.log(a + b);
}
```

## Task 10: Factorial

- **Objective**: Compute and print a factorial using recursion.
- **Script**: [10-factorial.js](10-factorial.js)

```javascript
#!/usr/bin/node

function factorial(n) {
  if (isNaN(n) || n < 0) {
    return 1;
  } else if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const num = parseInt(process.argv[2]);
console.log(factorial(num));
```

## Task 11: Second biggest!

- **Objective**: Find and print the second biggest integer in the list of arguments.
- **Script**: [11-second_biggest.js](11-second_biggest.js)

```javascript
#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  const sortedArgs = args.sort((a, b) => a - b);
  console.log(sortedArgs[sortedArgs.length - 2]);
}
```

## Task 12: Object

- **Objective**: Replace the value 12 with 89 in an

 object.
- **Script**: [12-object.js](12-object.js)

```javascript
#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12
};

console.log(myObject);

myObject.value = 89;

console.log(myObject);
```

## Task 13: Add file

- **Objective**: Write a function that returns the addition of two integers.
- **Script**: [13-add.js](13-add.js)

```javascript
#!/usr/bin/node

exports.add = function (a, b) {
  return a + b;
};
```

## Task 14: Const or not const

- **Objective**: Modify the value of myVar to 333.
- **Script**: [100-let_me_const.js](100-let_me_const.js)

```javascript
#!/usr/bin/node

myVar = 333;
```

## Task 15: Call me Moby

- **Objective**: Execute a function x times.
- **Script**: [101-call_me_moby.js](101-call_me_moby.js)

```javascript
#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
```

## Task 16: Add me maybe

- **Objective**: Increment and call a function.
- **Script**: [102-add_me_maybe.js](102-add_me_maybe.js)

```javascript
#!/usr/bin/node

exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
```

## Task 17: Increment object

- **Objective**: Add a new function to an object that increments its integer value.
- **Script**: [103-object_fct.js](103-object_fct.js)

```javascript
#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12
};

console.log(myObject);

myObject.incr = function () {
  this.value++;
};

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
```

---

