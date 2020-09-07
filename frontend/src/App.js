import React from 'react';
import './App.css';
import { useQuery } from "@apollo/react-hooks"
import gql from "graphql-tag"
import "@elastic/eui/dist/eui_theme_light.css";
import { HeaderBar } from "./components/header_bar.js";
import { Search } from "./components/search.js";
import { CardedDonutChart } from "./components/carded_donutchart.js";

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

    this.setState( () => ({
      searchData: value.value
  }));
  }

  render() {
    return (
      <main className="App">
        <HeaderBar></HeaderBar>
        <Search changeValue={this.changeValue.bind(this)}></Search>

        <CardedDonutChart data={this.searchData}></CardedDonutChart>
        <h1>Items</h1>
      </main>
    )
  }
}

export default App