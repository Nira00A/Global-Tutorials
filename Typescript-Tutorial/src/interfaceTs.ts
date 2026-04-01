type chaiOrder = {
    type: string ;
    sugar: number ;
    strong : boolean
}

function makeChai(order: chaiOrder){
    console.log(order)
}

function saveChai(order: chaiOrder){
    console.log(order)
}

type Tea = {
    water: number,
    milk: number
}

class MasalaChai implements Tea {
    water = 100;
    milk = 50;
}

interface TeaRep {
    water: number,
    milk: number
}

interface cupSize {
    size: 'small' | 'large'
}

class chai implements cupSize {
    size: "small" | "large" = 'small'
}

interface response{ok: true | false}

type TeaType = "masala" | "ginger" | "lemon"

function orderChai(t: TeaType){
    console.log(t)
}

type BaseChai = {tealeaves: number}
type extra = {masala: number}

type MasalaChai1 = BaseChai & extra

const cup: MasalaChai1 = {
    tealeaves: 2,
    masala: 1
}

type User = {
    username: string 
    bio?: string
}

const u1: User = { username: 'Arin' }
const u2: User = { username: 'Horin' , bio: 'horin.ai'}

// read only 
type config = {
    readonly appName: string
    version: Number
}

const cfg : config = {
    appName: 'Todotog',
    version: 1
}

// cfg.appName = "kuku" (error) - Just one time assign of the value in read only

