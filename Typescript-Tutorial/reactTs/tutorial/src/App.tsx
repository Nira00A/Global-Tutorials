import { useState } from 'react'
import './App.css'
import { Card } from './components/Card'

import type { CardPropTypes } from './types'
import CardList from './components/CardList'

const menu: CardPropTypes[] = [
  { name: 'Masala' , price: 30 , dimention: 'small'},
  { name: 'Adrak' , price: 50 , dimention: 'small'},
  
]

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <CardList items={menu}/>
      </div>
    </>
  )
}

export default App
