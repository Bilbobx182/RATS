import "@elastic/eui/dist/eui_theme_light.css";
import { EuiButton, EuiFlexGroup, EuiFlexItem } from "@elastic/eui";
import { EuiFieldSearch, EuiSwitch } from '@elastic/eui';
import React from 'react';

class NavBar extends React.Component {

    state = {
        button_options : [
            {
                id: 1,
                button_text : "Button 1"
            },

                {
                    id: 2,
                    button_text : "Button 2"
                }
        ]
    }

    render() {
        return (

    <EuiFlexGroup gutterSize="s" alignItems="stretch">

{this.state.button_options.map( state_button =>
        <EuiFlexItem grow={false} key={state_button.id}>
            <EuiButton fill onClick={() => window.alert("Button clicked")}>
                {state_button.button_text}
            </EuiButton>

             </EuiFlexItem>
        )}
    </EuiFlexGroup>
    )
}
}

export class  HeaderBar extends React.Component {

    state = {
        title : "Rats Job Finder",
        button_options : [
            {
                id: 1,
                button_text : "Button 1"
            },

                {
                    id: 2,
                    button_text : "Button 2"
                }
        ]
    }

    render() {
        return (
            <header className='header_banner'>
                <h1>{this.state.title}</h1>
                <NavBar item></NavBar>

            </header>
        );
    }


   };