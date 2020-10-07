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
            '#EF5350','#EC407A', '#AB47BC', '#7E57C2', '#5C6BC0', '#42A5F5', '#29B6F6', '#26C6DA','#26A69A','#66BB6A','#9CCC65','#D4E157','#FFEE58','#FFCA28','#FFA726','#FF7043','#8D6E63','#BDBDBD'
        ]
        const hoverBackgroundColor = [
            '#FFCDD2','#F8BBD0', '#E1BEE7', '#D1C4E9', '#C5CAE9', '#BBDEFB', '#B3E5FC', '#B2EBF2','#B2DFDB','#C8E6C9','#DCEDC8','#F0F4C3','#FFF9C4','#FFECB3','#FFE0B2','#FFCCBC','#D7CCC8','#F5F5F5'
        ]
    
    content.datasets[0].backgroundColor = (backgroundColor);
    content.datasets[0].hoverBackgroundColor = (hoverBackgroundColor);
    console.log(content);
    this.props.changeValue(content);

    }


    _performRequest() {
        console.log("PERFORMING REQUEST");

        (async () => {
            const rawResponse = await fetch('https://onuallainc.dev:5000/get_job_words', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ title: this.state.value })
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
                    placeholder="Enter job title for frequency analysis here!"
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