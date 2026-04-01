function makeChai(type: string , cups: number){
    console.log(`Mkaing ${type} cups of ${cups}`)
}

makeChai('Masala' , 2)

function takeChai(cond: boolean) : string {
    return `${cond} takes cups of chai`
}

function makeOrder(order: string) {
    if (!order) return null
    return order
}

function logChai(): void {
    console.log("Chai is ready") // no return so void type
}

function createChai(order: {
    type: string,
    sugar: number,
    size: "small" | "large"
}) : number {
    return 12
}