import "@elastic/eui/dist/eui_theme_light.css";
import { EuiButton, EuiFlexGroup, EuiFlexItem } from "@elastic/eui";
import { EuiFieldSearch, EuiSwitch } from '@elastic/eui';
import React from 'react';

export class Search extends React.Component  {


    state = {
        isClearable : true,
        value : "",
        searching: false
    }

    _performRequest() {
        console.log("PERFORMING REQUEST");

        (async () => {
            const rawResponse = await fetch('http://localhost:5000/dummy_words', {
              method: 'POST',
              headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
              },
              body: JSON.stringify({title: "JOB TITLE HERE"})
            });
            const content = await rawResponse.json();
          
            console.log(content);
          })();

        // const apiUrl = 'http://localhost:5000/dummy_words';
        // fetch(apiUrl)
        //   .then((response) => response.json())
        //   .then((data) => console.log('This is your data', data));

        //   this.setState( () => { return {
        //     searching: false
        // }});
        

    }

    onChange= (e) => {
        console.log(e.target.value);
        this.setState(prevState => { return {
            value: e.target.value
        }
      });
      }

      _handleKeyDown =  (e) => {
    
        if (e.key === 'Enter') {
          console.log('HELLO WORLD ENTER');

          this.setState(prevState => { return {
            searching : !prevState.searching
        }
      });
      this._performRequest();
        }
      }

    render() {

        return (            
            <EuiFieldSearch
            placeholder="https://indeed etc"
            fullWidth={true}
            value={this.value}
            onChange={e => {e.persist(); this.onChange(e)}}
            onKeyDown={this._handleKeyDown}
            isClearable={this.isClearable}
          />
        )
    }
}