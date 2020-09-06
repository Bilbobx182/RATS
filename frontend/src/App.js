import React from 'react';
import './App.css';
import { useQuery } from "@apollo/react-hooks"
import gql from "graphql-tag"
import "@elastic/eui/dist/eui_theme_light.css";
import { HeaderBar } from "./components/header_bar.js";
import { Search } from "./components/search.js";

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

const Location = ({ item: { city } }) => (
  <div className="Location">
    <h1 className="Location--name">{city}</h1>
  </div>
)


{/* 
TODO Configure colour themes
*/}


class App extends React.Component {

  state = {
    search_state: {
      searchData: "",
      isClearable: true,
      value: "",
      searching: false,
      searchResult: ""
    }
  }

  changeValue(value) {
    console.log("APP HELLO WORLD");
    console.log({ value });
  }

  updateSearchDataState = searchData => this.setState({ searchData })

  render() {
    return (
      <main className="App">
        <HeaderBar></HeaderBar>
        <Search changeValue={this.changeValue}></Search>
        <h1>Items</h1>
      </main>
    )
  }
}

export default App