/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    let fntcall=false;
    let res;
    return function(...args){
        if(!fntcall)
        {
            res=fn(...args);
            fntcall=true;
            return res;
        }
        else
        {
            return undefined;
        }
    }
};

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */
