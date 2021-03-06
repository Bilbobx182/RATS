import "@elastic/eui/dist/eui_theme_light.css";
import React from 'react';
import { Doughnut } from 'react-chartjs-2';
import { EuiFlexItem, EuiFlexGroup } from "@elastic/eui";
import { EuiCard } from '@elastic/eui';
export class CardedDonutChart extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div className="cardedDonutChart">
                <EuiFlexGroup justifyContent="flexEnd">
                    <EuiFlexItem>
                        <EuiCard
                            textAlign="Center"
                            title="Word frequency analysis of jobs in Dublin"
                            description={
                                <span>
                                    <div className="ChartStyle">
                                        <Doughnut data={this.props.graphData} />
                                    </div>
                                </span>
                            } />
                    </EuiFlexItem>
                </EuiFlexGroup>

            </div>
        )
    }
}