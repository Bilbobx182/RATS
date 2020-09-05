import React from 'react';
import './App.css';
import { useQuery } from "@apollo/react-hooks"
import gql from "graphql-tag"
import "@elastic/eui/dist/eui_theme_light.css";
import { EuiButton, EuiFlexGroup, EuiFlexItem } from "@elastic/eui";
import { EuiFieldSearch, EuiSwitch } from '@elastic/eui';

const CiaranNavbar = ()  => {
    return (
      <EuiFlexGroup gutterSize="s" alignItems="stretch">
      <EuiFlexItem grow={false}>
        <EuiButton onClick={() => window.alert("Button clicked")}>
          Primary
        </EuiButton>
      </EuiFlexItem>
    
      <EuiFlexItem grow={false}>
        <EuiButton fill onClick={() => window.alert("Button clicked")}>
          Filled
        </EuiButton>
      </EuiFlexItem>
    </EuiFlexGroup>
    )
}


const Header = () => {
     return (
        <header className='header_banner'>
            <h1>Rats Job finder</h1>
            <CiaranNavbar></CiaranNavbar>
        </header>
    );
    };
  

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

const Search = () => {
  const [isClearable, setIsClearable] = React.useState(true);
  const [value, setValue] = React.useState('');

  const onChange = e => {
    setValue(e.target.value);
  };

  return (
    /* DisplayToggles wrapper for Docs only */

      <EuiFieldSearch
        placeholder="Search this"
        value={value}
        onChange={e => onChange(e)}
        isClearable={isClearable}
        aria-label="Use aria labels when no actual label is in use"
      />
  );
};


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
     <Header></Header>
     <Search></Search>
      <h1>Items</h1>
      {data.allLocations.edges.map(
        item => (
        <Location key={item.node.id} item={item.node} />))}
    </main>
  )
}

export default App