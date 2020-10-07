import "@elastic/eui/dist/eui_theme_light.css";
import React from 'react';

class AppBody extends React.Component {
    render() {
        return (
          <main className="AppBody">
            <HeaderBar></HeaderBar>
            <Search changeValue={this.changeValue}></Search>
            <AppBody></AppBody>
            <h1>Items</h1>
          </main>
        )
    }
}