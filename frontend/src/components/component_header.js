import "@elastic/eui/dist/eui_theme_light.css";
import { EuiIcon, EuiFlexGroup, EuiFlexItem,EuiButton } from "@elastic/eui";
import React from 'react';

class NavBar extends React.Component {

    state = {
        button_options: [
            {
                id: 1,
                button_text: "Button 1"
            },
            {
                id: 2,
                button_text: "Button 2"
            }
        ]
    }

    render() {
        return (
            <EuiFlexGroup gutterSize="s" alignItems="stretch">

                {this.state.button_options.map(state_button =>
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

export class HeaderBar extends React.Component {

    state = {
        title: "Rats Job Finder"
    }

    render() {
        return (
            <header className='header_banner'>
                {/* TODO There must be a cleaner way of doing the href here */}
                <a href='https://github.com/bilbobx182'><EuiIcon type="logoGithub" /></a>
                <h1>{this.state.title}</h1>
                <a href='https://www.linkedin.com/in/onuallainc'><EuiIcon type="accessibility" /></a>
            </header>
        );
    }
};