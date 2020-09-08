import "@elastic/eui/dist/eui_theme_light.css";
import { EuiFieldSearch } from '@elastic/eui';
import React from 'react';
import {DropdownComponent}  from './component_dropdown.js';

export class Search extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            isClearable: true,
            value: "",
            searching: false,
            searchResult: ""
        };
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
                body: JSON.stringify({ title: "JOB TITLE HERE" })
            });
            const content = await rawResponse.json();
            console.log("Setting Content")
            this.props.changeValue(content);
            console.log("Content set");
            console.log(content);
        })();
    }

    updateSearchWords = (e) => {
        console.log(e.target.value);
        this.setState( () => {
            return {
                value: e.target.value
            }
        });
    }

    _handleKeyDown = (e) => {

        if (e.key === 'Enter') {
            this._performRequest()
            this.setState(prevState => {
                return {
                    searching: !prevState.searching
                }
            });
        }
    }

    render() {
        return (
            <div className='SearchComponent'> 
                <EuiFieldSearch
                placeholder="Placeholder"
                fullWidth={true}
                value={this.value}
                onChange={e => { e.persist(); this.updateSearchWords(e) }}
                onKeyDown={this._handleKeyDown}
                isClearable={this.isClearable}/>
                <DropdownComponent> </DropdownComponent>
            </div>       
        )
    }
}