import React from 'react';
import './App.css';
import { useQuery } from "@apollo/react-hooks"
import gql from "graphql-tag"
import "@elastic/eui/dist/eui_theme_light.css";
import { HeaderBar } from "./components/component_header.js";
import { Search } from "./components/component_search.js";
import { CardedDonutChart } from "./components/component_donutchart.js";

class App extends React.Component {

  state = {
    searchData : {},
    search_state: {
      id : 0,
      isClearable: true,
      value: "",
      searching: false,
      searchResult: ""
    }
  }

  changeValue(value) {
    console.log(value);
    this.setState( () => ({
      searchData : value
  }));

  this.setState( prevState => ({
    id : (prevState.search_state.id + 1).toString()
  }));
  }

  render() {
    return (
      <main className="App">
        <HeaderBar></HeaderBar>
        <Search changeValue={this.changeValue.bind(this)}></Search>

        <CardedDonutChart graphData={this.state.searchData} key={this.state.search_state.id}></CardedDonutChart>
        <h1>Items</h1>
      </main>
    )
  }
}

export default App