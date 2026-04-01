class Chai {
    flavour: string;
    price: number

    constructor(flavor: string , price: number){
        this.flavour = flavor
        this.price = price
    }
}

const masalaChai = new Chai("Ginger" , 20)

masalaChai.flavour = "Masala"

// Access Modifier

class Chai1 {
    public flavor: string = "Masala"

    private secret: string[] = ["Cardmom" , "Kuku"]

    reveal(){
        return this.secret // ok no direct access
    }

    protected shopName: string = "Chai Corder" 
}

const c = new Chai1()

// private 
c.reveal()

class Walet{
    #balance = 100

    getBalance(){
        return this.#balance
    }
}

const w = new Walet()

w.getBalance // no .balance here is private

// readonly 
class Cup{
    readonly capacity: number = 250

    constructor(capacity: number){
        this.capacity = capacity
    }
}

// getter and setter

class ModernChai {
    private _sugar = 2

    get sugar(){
        return this._sugar
    }

    set sugar(value: number){
        if(value > 5) throw new Error("Too sweet")
        
        this._sugar = value
    }
}

const c1 = new ModernChai()

c1.sugar = 3
console.log(c1.sugar)

// static classes

class EKchai {
    static shopName = "Chaicode caffe"

    constructor(public flavour: string){}
}

console.log(EKchai.shopName)

// abstract classes

abstract class Drink{
    abstract make(): void
}

class Mychai extends Drink{
    make(){
        console.log('Hi')
    }
}

// composition

class Heater{
    heat(){}
}

class Winter {
    constructor(private heater: Heater){}

    make(){
        this.heater.heat
    }
}
