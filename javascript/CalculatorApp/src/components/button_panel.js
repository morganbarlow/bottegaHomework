from React import "react";
import "./style/button_panel.css"

export default class Button_panel extends Component {
    render() {
        return(
            <div>
                C +/- % /
                7  8  9 *
                4  5  6 -
                1  2  3 +
                   0  . =
            </div>
        )
    }
}