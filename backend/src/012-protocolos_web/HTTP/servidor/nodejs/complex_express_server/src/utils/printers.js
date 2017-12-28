
import colors from "colors";

export function success(msg) {
	console.log(msg.green);
}

export function fail(msg) {
	console.log(msg.red);
}

export function warning(msg) {
	console.log(msg.yellow);
}

export function info(msg) {
	console.log(msg.cyan);
}