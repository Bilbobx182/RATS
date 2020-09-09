import "@elastic/eui/dist/eui_theme_light.css";
import { EuiFieldSearch } from '@elastic/eui';
import React from 'react';
import { DropdownComponent } from './component_dropdown.js';

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

    _updateGraphRequest(content) {

        const backgroundColor = [
            '#42a5f5','#ffca28', '#ff7043', '#ab47bc', '#26c6da', '#66bb6a', '#ec407a'
        ]
        const hoverBackgroundColor = [
            '#90caf9','#fff59d', '#ffab91', '#ce93d8', '#80deea', '#a5d6a7', '#f48fb1'
        ]
    
    content.datasets[0].backgroundColor = (backgroundColor);
    content.datasets[0].hoverBackgroundColor = (hoverBackgroundColor);
    console.log(content);
    this.props.changeValue(content);

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
            this._updateGraphRequest(content);
        })();
    }

    updateSearchWords = (e) => {
        console.log(e.target.value);
        this.setState(() => {
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
                    placeholder="Enter Job Title here!"
                    fullWidth={true}
                    value={this.value}
                    onChange={e => { e.persist(); this.updateSearchWords(e) }}
                    onKeyDown={this._handleKeyDown}
                    isClearable={this.isClearable} />
                <DropdownComponent> </DropdownComponent>
            </div>
        )
    }
}