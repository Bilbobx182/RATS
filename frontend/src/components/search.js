import "@elastic/eui/dist/eui_theme_light.css";
import { EuiButton, EuiFlexGroup, EuiFlexItem } from "@elastic/eui";
import { EuiFieldSearch, EuiSwitch } from '@elastic/eui';
import React from 'react';

export class Search extends React.Component  {


    state = {
        isClearable : true,
        value : ""
    }

    onChange= (e) => {
        console.log(e.target.value);
        this.setState(prevState => { return {
            value: e.target.value
        }
      });
      }

    render() {

        return (            
            <EuiFieldSearch
            placeholder="https://indeed etc"
            fullWidth={true}
            value={this.value}
            onChange={e => {e.persist(); this.onChange(e)}}
            isClearable={this.isClearable}
          />
        )
    }
}