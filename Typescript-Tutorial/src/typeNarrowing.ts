function getChai(kind: string | number){
    if(typeof kind === 'string'){
        return `Making ${kind} chai...`
    }
    return `Chai order: ${kind}`
}

//Exhaustive type narrowing

function orderChai(size: 'small' | 'medium' | 'large' | number){
   // if(size) ...
   // ....
}

class NormalChai{
    serve(){
        return 'Serving Normal Chai'
    }
}

class CuttingChai{
    serve(){
        return 'Serving Cutting Chai'
    }
}

function serve(chai: NormalChai | CuttingChai){
    if(chai instanceof NormalChai){
        return 'Normal'
    }
}

type ChaiOrder = {
    type: string
    sugar: number
}

function isChaiOrder(obj:any):obj is ChaiOrder{
    return(
        typeof obj === 'object' &&
        obj !== null &&
        typeof obj.type === 'string' &&
        typeof obj.sugar === 'number'
    )
} 
