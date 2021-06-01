 class Queue{
   #b
   show
   item
put(a){
   
    if (Array.isArray(a)){
     return this.#b = a
    }
    else if (typeof a === 'string'){
       return this.#b  = a.split('')
    }
    else {
     return this.#b = a.toString().split('')
    }

}
get(){ 
return this.item = this.#b.shift()
}
showarray()
{
   console.log( this.show = this.#b)
}


}
module.exports = Queue



