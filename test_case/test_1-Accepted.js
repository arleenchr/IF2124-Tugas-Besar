import "package";
import {function} from "package1";
import {function1, function2} from "package1";

// This is a sample single-line comment

function function4(param1,param2) {
    for (let i = 0; i < param1; i++) {
        console.log(param2);
        if (i == param1) {
            break;
        } else {
            continue;
        }
    }
}

// This
// Is
// A
// Multiline
// Comment

x = 'ABCDEFGJIJ' + 1 + null;

if (!false){
    function4(3,x);
} else if (true){
    console.log('True');
} else {
    console.log('Not True');
}

// End of program