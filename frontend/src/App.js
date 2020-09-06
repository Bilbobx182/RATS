import React from 'react';
import './App.css';
import { useQuery } from "@apollo/react-hooks"
import gql from "graphql-tag"
import "@elastic/eui/dist/eui_theme_light.css";
import { EuiButton, EuiFlexGroup, EuiFlexItem } from "@elastic/eui";
import { EuiFieldSearch, EuiSwitch } from '@elastic/eui';
import {HeaderBar} from  "./components/header_bar.js";
import {Search} from  "./components/search.js";

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


{/* 
TODO Configure colour themes
*/}


function App() {
  // const { loading, error, data } = useQuery(GET_USERS)

  // if (error) return <h1>Something went wrong!</h1>
  // if (loading) return <h1>Loading...</h1>

  return (
    <main className="App">
     <HeaderBar></HeaderBar>
     <Search></Search>
      <h1>Items</h1>
      {/* {data.allLocations.edges.map(
        item => (
        <Location key={item.node.id} item={item.node} />))} */}
    </main>
  )
}

export default App