/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    return new Promise((resolve,reject)=>{
        if(functions.length===0)
        {
            resolve([]);
            return;
        }
        const res=new Array(functions.length).fill(null);
        let resolveCount=0;
        functions.forEach(async(i,j)=>{
            try{
                const subres=await i();
                res[j]=subres;
                resolveCount++;
                if(resolveCount===functions.length){
                    resolve(res);
                }
            } catch(err){
                reject(err);
            }
        })
    })
    
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */