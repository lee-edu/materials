// Promises
const fn1 = () => {
  let result;
   db.get(query, [params], (error, result) => {
     result = 1;
   });
   console.log("hello");
   return result;
}
// ...
const fn2 = () => {
  return new Promise(
    (resolve, reject) => {
      db.get(query, [params], (error, result) => {
        if (error){
          reject(error);
        }
        resolve(result);
      });
    }
  );
}

const main = async () => {
  try {
    const a = await fn1();
    const b = await fn2();
    return a + b;
  } catch (error){
    console.error(error);
  }
}
