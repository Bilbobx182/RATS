import "@elastic/eui/dist/eui_theme_light.css";
import React from 'react';
import {Doughnut} from 'react-chartjs-2';

export class CardedDonutChart extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        return (
          <div className="cardedDonutChart">
                <Doughnut data={this.props.graphData} />
          </div>
        )
    }
}