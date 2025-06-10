/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    let cache={};
    return function(...args) {
        let temp=String(args);
        if(temp in cache)
        {
            return cache[temp];
        }
        let result=fn(...args);
        cache[temp]=result;
        return result;
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */