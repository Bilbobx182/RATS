import React, { useState } from 'react';

import {
    EuiButton,
    EuiContextMenu,
    EuiPopover
} from '@elastic/eui';

export class DropdownComponent extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            isPopoverOpen: false,
            setPopover: false,
        }
    }

    onButtonClick = () => {


        this.setState(prevState => {
            return {
                setPopover: !prevState.setPopover
            }
        });
    };

    closePopover = () => {
        this.setState(() => {
            return {
                setPopover: false
            }
        });
    };


    getButton = () => {
        return (<EuiButton
            iconType="arrowDown"
            iconSide="right"
            onClick={this.onButtonClick}>
            Menu
        </EuiButton>)


    }
    render() {
        return (
            <div id='dropDownComponent'>
                <EuiPopover
                    id="contextMenuExample"
                    button={this.getButton}
                    isOpen={this.state.isPopoverOpen}
                    closePopover={this.closePopover}
                    panelPaddingSize="none"
                    withTitle
                    anchorPosition="downLeft">
                    <EuiContextMenu initialPanelId={0} panels={this.props.panels} />
                </EuiPopover>
            </div>
        )
    }

};