# Types

Look at the following code, then figure out the type of each `foo`.

```java
// Java
String foo1 = "Hello";

void foo2(int bar){
  System.out.println("Goodbye.");
}

int[] foo3 = new int[] {1,2,3,4,5};
```

The example function calls will help with figuring out the type of each function!

```python
# Python
def foo4(bar):
  return bar[1:]
# foo4([1,2,3]) >>> [2,3]

def foo5(bar):
  return bar + 1
# foo5(3) >>> 4

def foo6(bar):
  print("Hello " + bar)
# foo6("foo") >>> "Hello foo"
```

```js
// Javascript
function foo7(x){
  return function(y){
    return x + y;
  }
}
//foo7(3)(5) >>> 8
//foo7("hello")("world") >>> "helloworld"

const foo8 = x => y => x + y;
//foo8(3)(5) >>> 8
//foo8("hello")("world") >>> "helloworld"

const foo9 = a => b => a(b)
//foo9(x => x + 3)(3) >>> 6

const foo10 = a => b => c => a(b)(c)
//foo10(x => y => x + y)(3)(5) >>> 8
```