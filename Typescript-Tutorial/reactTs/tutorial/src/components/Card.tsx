import Counter from "./Counter";

interface CardProp {
    name: string;
    price: number;
    isSpecial?: boolean;
    dimention: string
}

export function Card({name , price , isSpecial = false , dimention} : CardProp){
    return(
        <article>
            <h2>
                {name} {isSpecial && <span>Star</span>}
            </h2>
            <h3>{price}</h3> <h3>{dimention}</h3>

            <Counter />
        </article>
    )
}