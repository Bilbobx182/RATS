import "@elastic/eui/dist/eui_theme_light.css";
import { EuiButton, EuiFlexGroup, EuiFlexItem } from "@elastic/eui";
import { EuiFieldSearch, EuiSwitch } from '@elastic/eui';
import React from 'react';

const NavBar = ()  => {
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

export const HeaderBar = () => {
    return (
       <header className='header_banner'>
           <h1>Rats Job finder</h1>
           <NavBar></NavBar>
       </header>
   );
   };