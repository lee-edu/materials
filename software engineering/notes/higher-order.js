const reducer = (acc, item) => 
	acc + (item.price * item.quantity);
 
const totalPrice = cart => cart.reduce(reducer, 100);

Array.prototype.reduce = (reducerFn, initialValue) => {

}

Array.prototype.filter = (filterFn) => {};
Array.prototype.map = (mapFn) => {};

// Same thing but w/ for loop
function _totalPrice(cart){
	let acc = 0;
	for (const item of cart){
		acc = reducer(acc,item);
	}
	return acc;
}