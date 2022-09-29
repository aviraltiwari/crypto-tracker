import { useEffect, useState } from 'react'
import './App.css'

function App() {
  const [cryptoCurrency, setCryptoCurrency] = useState({})
  useEffect(() => {
    try {
      setInterval(() => {
        fetch('http://127.0.0.1:8000/').then(response => response.json()).then(json => setCryptoCurrency(json))
      }, 3000)
    } catch {
      console.log("Something Went Wrong")
    }
  }, [])
  return (
    <div className="App">
      <h1>Top 10 CryptoCurrency</h1>
      <h2>Tracker</h2>
      {
        Object.keys(cryptoCurrency).length === 0 ? 'Please Wait' :
          <table>
            <tr>
              <th>Name</th>
              <th>Price</th>
              <th>1 Hour %</th>
              <th>24 Hour %</th>
              <th>7 day %</th>
              <th>Market Cap</th>
              <th>Volume</th>
              <th>Supply</th>
            </tr>
            {cryptoCurrency.map((item, index) =>
              <tr key={index}>
                <td>{item.name}</td>
                <td>{item.price}</td>
                <td>{item.change_percentage_1h}</td>
                <td>{item.change_percentage_2h}</td>
                <td>{item.change_percentage_7d}</td>
                <td>{item.market_cap}</td>
                <td>{item.volume}</td>
                <td>{item.supply}</td>
              </tr>)}
          </table>
      }
    </div>
  );
}

export default App;
