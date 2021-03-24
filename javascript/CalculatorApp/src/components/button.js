import React from "react";
import PropTypes from "prop-types";
import "./style/button.css"

export default class Button extends Component {
    render (){
        return(
            <div>
                <div className = {operators} >
                    clear +/- % / * - +
                </div>
                <div className = {numbers} >
                    0 1 2 3 4 5 6 7 8 9
                </div>
            </div>
        )
    }
}