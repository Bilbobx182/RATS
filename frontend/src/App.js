import React from 'react';
import logo from './logo.svg';
import './App.css';
import { useQuery } from "@apollo/react-hooks"
import gql from "graphql-tag"

const GET_USERS = gql`
{
  allLocations {
  edges {
    node {
      id,city
    }
  }
}
}
`

const Location = ({item : {city}}) => (
  <div className="Location">
      <h1 className="Location--name">{city}</h1>
  </div>
)


function App() {
  const { loading, error, data } = useQuery(GET_USERS)

  if (error) return <h1>Something went wrong!</h1>
  if (loading) return <h1>Loading...</h1>

  return (
    <main className="App">
      <h1>Items</h1>
      {data.allLocations.edges.map(
        item => (
        <Location key={item.node.id} item={item.node} />))}
    </main>
  )
}

export default App