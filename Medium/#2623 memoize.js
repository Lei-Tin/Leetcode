/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {

    let cache = {};

    return function(...args) {
        let key = JSON.stringify(args);

        if (key in cache) {
            return cache[key];
        }

        let res = fn(...args);
        cache[key] = res;

        return res;
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
