## 0x13-javascript_objects_scopes_closures


# Alx Higher Level Programming - JavaScript Objects, Scopes, Closures

This repository contains JavaScript scripts and modules covering various topics related to objects, scopes, and closures. Below is a brief overview of each task along with the code and explanations.

## Task 0: Empty class
### File: 0-rectangle.js

```javascript
#!/usr/bin/node

class Rectangle {
  // Empty class definition
}

module.exports = Rectangle;
```

This task introduces the basic structure of a class in JavaScript.

---

## Task 1: Rectangle #0
### File: 1-rectangle.js

```javascript
#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    // Class constructor with width and height attributes
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
```

In this task, we define a class `Rectangle` with a constructor that initializes its width and height attributes.

---

## Task 2: Rectangle #1
### File: 2-rectangle.js

```javascript
#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
```

The class Rectangle is modified to only set width and height if both are positive.

---

## Task 3: Rectangle #2
### File: 3-rectangle.js

```javascript
#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    // Instance method to print rectangle using 'X'
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
```

This task adds an instance method `print()` to the Rectangle class that prints the rectangle using the character 'X'.

---

## Task 4: Rectangle #3
### File: 4-rectangle.js

```javascript
#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate() {
    // Instance method to exchange width and height
    [this.width, this.height] = [this.height, this.width];
  }

  double() {
    // Instance method to double width and height
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
```

Task 4 enhances the Rectangle class by adding methods `rotate()` and `double()`.

---

## Task 5: Square #0
### File: 5-square.js

```javascript
#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    // Calling the constructor of Rectangle using super()
    super(size, size);
  }
}

module.exports = Square;
```

Task 5 introduces a new class Square that inherits from Rectangle, demonstrating the use of the `extends` keyword.

---

## Task 6: Square #1
### File: 6-square.js

```javascript
#!/usr/bin/node

const Square = require('./5-square');

class SquareWithCharPrint extends Square {
  charPrint(c) {
    // Instance method to print square using provided character or 'X'
    for (let i = 0; i < this.height; i++) {
      console.log((c || 'X').repeat(this.width));
    }
  }
}

module.exports = SquareWithCharPrint;
```

Task 6 adds an instance method `charPrint(c)` to the Square class, allowing customization of the printing character.

---

## Task 7: Occurrences
### File: 7-occurrences.js

```javascript
#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  // Function to count occurrences of searchElement in list
  return list.reduce((count, element) => (element === searchElement ? count + 1 : count), 0);
};
```

Task 7 defines a function `nbOccurences` that counts the occurrences of a specified element in a list.

---

## Task 8: Esrever
### File: 8-esrever.js

```javascript
#!/usr/bin/node

exports.esrever = function (list) {
  // Function to reverse a list without using the built-in reverse method
  return list.reduceRight((reversedList, element) => {
    reversedList.push(element);
    return reversedList;
  }, []);
};
```

Task 8 implements a function `esrever` that reverses a list without using the built-in `reverse` method.

---

## Task 9: Log me
### File: 9-logme.js

```javascript
#!/usr/bin/node

let count = 0;

exports.logMe = function (item) {
  // Function to log the number of arguments printed and the current argument value
  console.log(`${count++}: ${item}`);
};
```

Task 9 provides a function `logMe` that prints the number of arguments already printed along with the new argument value.

---

## Task 10: Number conversion
### File: 10-converter.js

```javascript
#!/usr/bin/node

exports.converter = function (base) {
  // Function to convert a number from base 10 to another base
  return function (number) {
    return number.toString(base);
  };
};
```

Task 10 defines a higher-order function `converter` that returns a conversion function for a specified base.

---

## Task 11: Factor index
### File: 100-map.js

```javascript
#!/usr/bin/node

const { list } = require('./100-data');

const newList = list.map((value, index) => value * index);

console.log(list);
console.log(newList);
```

Task 11 uses the `map` function to create a new list where each value is multiplied by its index.

---

## Task 12: Sorted occurrences
### File: 101-sorted.js

```javascript
#!/usr/bin/node

const { dict } = require('./101-data');

const sortedDict = {};

for (const key in dict) {
  const occurrences = dict

[key].toString();
  if (!(occurrences in sortedDict)) {
    sortedDict[occurrences] = [];
  }
  sortedDict[occurrences].push(key);
}

console.log(sortedDict);
```

Task 12 generates a new dictionary with occurrences as keys and lists of user ids as values.

---

## Task 13: Concat files
### File: 102-concat.js

```javascript
#!/usr/bin/node

const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const contentA = fs.readFileSync(fileA, 'utf-8');
const contentB = fs.readFileSync(fileB, 'utf-8');

fs.writeFileSync(fileC, contentA + contentB);
```

Task 13 concatenates the content of two files and writes the result to a third file.

