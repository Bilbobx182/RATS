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
      searchResult: "",
      colours: ['#ab47bc','#42a5f5','#26c6da','#66bb6a','#ffca28','#ff7043'],
      coloursAccent: ['#ce93d8','#90caf9','#80deea','#a5d6a7','#fff59d','#ffab91']
    }
  }


  changeValue(value) {
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
        <CardedDonutChart 
          graphData={this.state.searchData}
           key={this.state.search_state.id}>
         </CardedDonutChart>
      </main>
    )
  }
}

export default App