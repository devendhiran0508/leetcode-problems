/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    const combine=arr1.concat(arr2)
    const merge={};
    combine.forEach((obj)=>{
        const id=obj.id;
        if(!merge[id]){
            merge[id]={...obj};
        } 
        else 
        {
            merge[id]={...merge[id],...obj};
        }
    });
    return Object.values(merge)
};