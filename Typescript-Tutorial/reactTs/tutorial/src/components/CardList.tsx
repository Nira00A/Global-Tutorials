import type { CardPropTypes } from '../types'
import { Card } from './Card'

interface CartListProps {
    items : CardPropTypes[]
}

export default function CardList({items} : CartListProps) {

  return (
    <div>
        CardList
        {items.map((chai) => (
            <Card 
            key={chai.name}
            name={chai.name}
            price={chai.price}
            dimention={chai.dimention}/>
        ))}
    </div>
  )
}
