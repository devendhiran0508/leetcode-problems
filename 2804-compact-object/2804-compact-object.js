/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    const stack=[[obj, Array.isArray(obj)?[]:{}]];
    let new1=stack[0][1];
    while (stack.length>0)
    {
        const [currobj,newobj]=stack.pop();
        for(const key in currobj)
        {
            const value=currobj[key];
            if(!value) continue;
            if(typeof value!=='object')
            {
                Array.isArray(newobj)?newobj.push(value):newobj[key]=value;
                continue;
            }
            const newSubobj=Array.isArray(value)?[]:{};
            Array.isArray(newobj)?newobj.push(newSubobj):newobj[key]=newSubobj;
            stack.push([value,newSubobj]);
        }
    }
    return new1
};